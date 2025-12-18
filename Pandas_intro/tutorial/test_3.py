import pandas as pd

my_dataset = [ 1 , 3 , 6, 9 , 12 ]
df = pd.Series(my_dataset, index=['a', 'b', 'c', 'd', 'e'])
print(df)
print(df["c"])
