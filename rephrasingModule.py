from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def rephrase(sentence,tokenizer,model):

    text = "paraphrase: " + sentence + " </s>"

    encoding = tokenizer.encode_plus(text, padding=True, return_tensors="pt")
    #input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")
    input_ids, attention_masks = encoding["input_ids"], encoding["attention_mask"]

    outputs = model.generate(   #model.to("cuda").generate!!!
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=128,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=1
    )

    for output in outputs:
        line = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)

    return line

