import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

def get_FinBERT_sentiment(text_list):
    np.random.shuffle(text_list)
    headlines_list = list(text_list)

    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    inputs = tokenizer(text_list, padding = True, truncation = True, return_tensors='pt')

    outputs = model(**inputs)

    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

    model.config.id2label
    #Headline #Positive #Negative #Neutral
    positive = predictions[:, 0].tolist()
    negative = predictions[:, 1].tolist()
    neutral = predictions[:, 2].tolist()

    table = {'Text':headlines_list,
            "Positive":positive,
            "Negative":negative, 
            "Neutral":neutral}
        
    df = pd.DataFrame(table, columns = ["Text", "Positive", "Negative", "Neutral"])
    return df