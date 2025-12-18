import pandas as pd

data = pd.read_csv("data.csv")

# data["Date"] = pd.to_datetime(data["Date"], format='mixed' )

# data.dropna(subset=["Date"], inplace=True)
data.loc[37, "Duration"] = data.mode().loc[0, "Duration"]
print(data.to_string())