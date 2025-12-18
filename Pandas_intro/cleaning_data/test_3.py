import pandas as pd

df = pd.read_csv("data.csv")

for i in df.index:
    try:
        value = pd.to_numeric(df.loc[i, "Duration"])
        if pd.notna(value) and value > 120:
            df.loc[i, "Duration"] = 120
    except:
        df.drop(i, inplace=True)


print(df)
