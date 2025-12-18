import pandas as pd
pd.options.display.max_rows = 9999

df = pd.read_csv("Data.csv")

print(df)

# print(pd.options.display.max_columns) // to see settings