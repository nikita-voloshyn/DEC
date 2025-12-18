import pandas as pd

my_dataset = {
    "calories": [123, 254, 2453],
    "duration": [134, 3434, 234],
}

df = pd.DataFrame(my_dataset)

# print(df)
print(df.loc[[0, 2]])