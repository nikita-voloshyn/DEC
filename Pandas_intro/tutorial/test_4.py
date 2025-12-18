import pandas as pd


calories = {"day1": 12220, "day2": 1344, "day3": 12210,}

df = pd.Series(calories, index = ["day1", "day3"])
print(df)