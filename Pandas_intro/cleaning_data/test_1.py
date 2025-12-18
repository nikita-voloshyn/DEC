import pandas as pd

df = pd.read_csv("data.csv")

x = df["Maxpulse"].mean()

df.fillna({"Maxpulse": x}, inplace=True)

print(df)