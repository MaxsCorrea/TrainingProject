import pandas as pd
import json

#set up json file
def get_data():
    with open('services.json') as f:
        data = json.load(f)
        return data
data = get_data()


df = pd.DataFrame(data["services"])
print(df)

