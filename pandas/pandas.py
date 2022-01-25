import json
import pandas as pd

with open('sentence_dataset.csv') as f_input:
    df = pd.read_json(f_input)

df = df.bfill(axis='columns')
df.iloc[:, 0].to_csv('some.csv', encoding='utf-8', header=False)