import pandas as pd
import string
import numpy as np
import matplotlib.pyplot as plt


cast_data_csv = './datasets/mad-men-cast-show-data.csv'

# 1
cast = pd.read_csv(cast_data_csv, encoding = 'latin1')
'''
# 2
cast_head = cast.head()
print('Data head\n',cast_head)

cast_tail = cast.tail()
print('Data tail\n',cast_tail)

'''

# 3
cast_columns = cast.columns
print('Column Names from the dataset\n',cast_columns)

# 4
# Function to clean a string of spaces and special characters
def clean_string(name):
    letters = string.punctuation
    space = string.whitespace
    special_chars = letters + space
    pure_name = ''
    for ch in name:
        if ch not in special_chars:
            pure_name += ch
    return pure_name

cast_new_columns = [clean_string(col) for col in cast_columns]
# Assign new column
cast.columns = cast_new_columns
print('Modified Column Names from the dataset\n',cast.columns)

# 5

exclude = ('End','END')
subset = cast.query('Status not in @exclude')

print(subset)
'''
cast_subset = cast[(cast['Status'] != 'END') & (cast['Status'] != 'End')]
print(cast_subset)

#subset` = cast[[col for col in cast.columns if not col.lower().endswith('end')]]
#print(' %%%%%%%%%%\n', subset)

# 6
cast_subset = cast[(cast['ShowStart'] > 2005) & (cast['Score'] > 7)].Performer.unique()
print(' Performer unique', cast_subset)
#subset = cast.ix[['ShowStart' > 2005], ['Performer']]
#print(subset)
'''
