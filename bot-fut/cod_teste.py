import pandas as pd
import json

with open('json_teste.json', 'r') as f:
    json_data = json.load(f)

df = pd.json_normalize(json_data, record_path=['telefones'], meta=['nome', 'idade', ['endereco', 'cidade']])


print(df)