import pandas as pd
import matplotlib.pyplot as plt
import json

#set up json file
def get_data():
    with open('services.json') as f:
        data = json.load(f)
        return data
data = get_data()


df = pd.DataFrame(data["services"])
print(df)

df["disk usage"] = df["disk usage"].str[:-1].astype(float)
df["du>60"] = df["disk usage"].where(df["disk usage"].between(60, 100), None)
df["40<du<60"] = df["disk usage"].where(df["disk usage"].between(40, 60), None)
df["du<40"] = df["disk usage"].where(df["disk usage"].between(0, 40), None)

#setting the graph
ax = df.plot(x="name", y="du<40", kind="bar", color="royalblue")
df.plot(x="name", y="40<du<60", kind="bar", color="gold", ax=ax)
df.plot(x="name", y="du>60", kind="bar", color="tomato", ax=ax)

plt.xlabel('Services')
plt.ylabel('Disk Usage in %')
plt.title('Disk Usage Report')
plt.show()