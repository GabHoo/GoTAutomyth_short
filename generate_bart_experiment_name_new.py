
how = 'Instances '
#how = 'Types '
#how = 'Class '

#how = 'Event '
#how = 'Range '
experiment_name = 'reborn_events_community' 
method = 'community'


 #range, event, baseline instances, baseline class
#experiment_name = '' and here you put baseline instance, baseline class etc etc 
#[event1_relation_all, events12_community_types, events12_community_range, events12_community_all]
#for event1_relation_all need old version

### start with installing libraries

### import libraries

import transformers
from datasets import load_dataset, load_metric

import numpy as np
import os
import nltk
import torch
import evaluate
nltk.download('punkt')


### connect to the drive

#%cd /content/gdrive/Shareddrives/GOT/Building_Narratives_Game_of_Thrones/data

### upload the data
Working_Dir ='/Users/macoftraopia/Documents/GitHub/GoTAutomyth_short'

train_file = Working_Dir + '/generated_output/' + experiment_name + '/' + method +'_train.json'
dev_file = Working_Dir + '/generated_output/' +  experiment_name + '/' + method + '_val.json'
test_file = Working_Dir + '/generated_output/' + experiment_name + '/' + method + '_test.json'

dataset = load_dataset('json', data_files={'train': train_file, 'valid': dev_file, 'test': test_file})

### let's check the data

print(len(dataset['valid'][0]['story']))
print(dataset['test'][0][f'{how}Knowledge Graph'])

print(dataset['test'][0][f'{how}Knowledge Graph'])

lenn = []
lenval = [] 
for i in range(50): 
  #print(len(dataset['test'][i]['story']))
  lenn.append(len(dataset['test'][i]['story']))
  lenval.append(len(dataset['valid'][i]['story']))
#s = (dataset['valid'][0]['story'])
print('test max',np.max(lenn))
print('val max',np.max(lenval))

### data looks OK, let's continue with the tokenizer
max_input = np.max(lenval) #number of tokens we expect -DEPENDS ON size of inputs (for the tensor) - sentence and then it pads the rest - 
#such that tensors equal in shape (no pads when training bc we alreasy have same shape) - batches of same size
max_target = np.max(lenval)
model_checkpoints = 'facebook/bart-base'
tokenizer = transformers.AutoTokenizer.from_pretrained(model_checkpoints)

def preprocess_data(data_to_process):
  #get the dialogue text
  inputs = [graph for graph in data_to_process[f'{how}Knowledge Graph']]
  #tokenize text
  model_inputs = tokenizer(inputs,  max_length=max_input, padding='max_length', truncation=True)

  #tokenize labels
  #with tokenizer.as_target_tokenizer():
  targets = [target for target in data_to_process['story']]
  model_targets = tokenizer(targets, max_length=max_target, padding='max_length', truncation=True)
    
  model_inputs['labels'] = model_targets['input_ids']
  #reuturns input_ids, attention_masks, labels
  return model_inputs

tokenize_data = dataset.map(preprocess_data, batched = True) 

print(tokenize_data['test']['story'][3])
print(tokenize_data['test'][f'{how}Knowledge Graph'][3])

### let's drop the columns that we won't need
tokenize_data = dataset.map(preprocess_data, batched = True, remove_columns=['story','Instances Knowledge Graph','Class Knowledge Graph', 'Types Knowledge Graph', 'Event Knowledge Graph', 'Range Knowledge Graph','Ontology Knowledge Graph'])
#print(tokenize_data)

#print(tokenize_data['train']['attention_mask'][0])

### load model
model = transformers.AutoModelForSeq2SeqLM.from_pretrained(model_checkpoints)
#batch_size = 4 #we dont use htis 
#collator to create batches. It preprocess data with the given tokenizer
collator = transformers.DataCollatorForSeq2Seq(tokenizer, model=model)

#####################
# metrics
# compute rouge for evaluation 
#####################
metric = load_metric('rouge')

def compute_rouge(pred):
  predictions, labels = pred
  #decode the predictions
  decode_predictions = tokenizer.batch_decode(predictions, skip_special_tokens=True)
  #decode labels
  decode_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

  #compute results
  res = metric.compute(predictions=decode_predictions, references=decode_labels, use_stemmer=True)
  #get %
  res = {key: value.mid.fmeasure * 100 for key, value in res.items()}

  pred_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in predictions]
  res['gen_len'] = np.mean(pred_lens)

  return {k: round(v, 4) for k, v in res.items()}

args = transformers.Seq2SeqTrainingArguments(
    'output',
    evaluation_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=1,
    per_device_eval_batch_size= 1,
    gradient_accumulation_steps=2, #compute gradient on 2 examples KG story 
    weight_decay=0.01, #regularization
    save_total_limit=2,
    num_train_epochs=3,
    predict_with_generate=True, #since we use validation (bc during validation we generate and compare to gold ) - backprpop error on rouge
    generation_max_length = 1000, #max number of tokens per generation 
    generation_num_beams=5, #decoding strategy! greedy search, beam search 
    eval_accumulation_steps=1, #backprop  
    fp16=False #memory management 
    )
#only CUDA available -> fp16=True

### almost training time
trainer = transformers.Seq2SeqTrainer(
    model, 
    args,
    train_dataset=tokenize_data['train'],
    eval_dataset=tokenize_data['valid'],
    data_collator=collator,
    tokenizer=tokenizer,
    compute_metrics=compute_rouge
)

### check GPU


### training time - takes around 15 mins

trainer.train()
### save the model for later use
#os.mkdir(Working_Dir + '/generated_text/by_BART/' + experiment_name + how )
trainer.save_model(Working_Dir + "/tuned_models/BART_models/" + experiment_name + how )

### let's have a look at the predictions

preds, labels, metrics = trainer.predict(tokenize_data['test'], num_beams=5, min_length=50, max_length=128, no_repeat_ngram_size=2, early_stopping=True)

pred = []
lab = []
for gen, gold in zip(preds, labels):
  gen = tokenizer.decode(gen, skip_special_tokens=True)
  gen = str(gen)
  gen = gen
  pred.append(gen)
  #print(pred)
  #print(f'Generated text: {gen}')
  gold = tokenizer.decode(gold, skip_special_tokens=True)
  gold = str(gold)
  gold = [gold]
  lab.append(gold)
  #results = bleu.compute(predictions=gen, references=gold)
  #print(results)
  #print(f'Reference text: {gold}')
print(len(pred))  
print(len(lab))

bleu = evaluate.load("bleu")
result_bleu= bleu.compute(predictions=pred, references=lab)
print(result_bleu)

google_bleu = evaluate.load("google_bleu")
result_google_bleu = google_bleu.compute(predictions=pred, references=lab)
print(result_google_bleu)

preds

os.mkdir(Working_Dir + '/generated_text/by_BART/' + experiment_name + how )
outfile_path = Working_Dir + '/generated_text/by_BART/' + experiment_name + how + '/generated_text_with_refs_bleu.txt'

outfile = open(outfile_path, "a", encoding='utf-8')

scores = metrics.items()
print(f'Results: {scores}')
print(f'Bleu Results: {result_bleu}')
print(f'Google Bleu Results: {result_google_bleu}')

outfile.write(f'Test Results: {scores}\n\n')
outfile.write(f'Bleu Results: {result_bleu}\n\n')
outfile.write(f'Google Bleu Results: {result_google_bleu}\n\n')

for gen, gold in zip(preds, labels):
  gen = tokenizer.decode(gen, skip_special_tokens=True)
  print(f'Generated text: {gen}')
  outfile.write(f'Generated text: {gen}\n')

  gold = tokenizer.decode(gold, skip_special_tokens=True)
  print(f'Reference text: {gold}')
  outfile.write(f'Reference text: {gold}\n\n')


  
outfile.close()

for i in metrics.items():
  print(i)