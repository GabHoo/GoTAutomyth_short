import spacy
from spacy import displacy
import json
import numpy as np
import nltk
from nltk import word_tokenize
from spacy import displacy
from datasets import load_dataset
#nltk.download('averaged_perceptron_tagger')
#nltk.download('universal_tagset')

NER = spacy.load('en_core_web_sm')

def entity_counter(path):
    f = open(path)
    data = json.load(f)
    intersection = []
    count_intersection = []
    for i in range(len(data)-1):
        gen = [str(i) for i in NER(data[i]["Generated text"]).ents] 
        ref = [str(i) for i in NER(data[i]["Reference text"]).ents] 
        intersection.append(list(set(gen) & set(ref)))
        count_intersection.append(round(len(list(set(gen) & set(ref)))/len(list(set(ref))),2))
    print('experiment from' + path +'\n','mean', np.mean(count_intersection), 'std',np.std(count_intersection))
    return intersection,count_intersection

def main():
    entity_counter('final_data/fromRephrased3/Instances _text_from_rephrased3.json')
    entity_counter('final_data/fromRephrased3/Ontology _text_from_rephrased3.json')
    entity_counter('final_data/fromNoRephrased3/Instances _text_from_Norephreased3.json')
    entity_counter('final_data/fromNoRephrased3/Ontology _text_from_Norephrased3.json')
    

if __name__ == "__main__":
    main()   