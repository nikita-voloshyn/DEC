import pandas as pd

my_dataset = {
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9],
    'd': [10, 11, 12],
    'e': [13, 14, 15],
    'f': [16, 17, 18],
    'g': [19, 20, 21],
    'h': [22, 23, 24],
    'i': [25, 26, 27],
    'j': [28, 29, 30],
}

#
# my_var = pd.DataFrame(my_dataset)
# print(my_var)
my_var = pd.Series(my_dataset)
print(my_var)

