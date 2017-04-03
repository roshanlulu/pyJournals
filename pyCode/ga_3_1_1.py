import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style('darkgrid')


def print_header(df):
    print('Header\n', df.columns)
    print('Shape\n', df.shape)
    print('Data head\n', df.head())
    return df.columns

def read_from_csv(filepath):
    df = pd.read_csv(filepath, encoding = 'utf-8')
    # print(df)
    return df

# # 1. Load data(messy data with missing info) in wide format
# messy_wide_data = read_from_csv('./datasets/NPAS_parsed_trunc_wide_missing.csv')
#
# # Print the header
# header =  print_header(messy_wide_data)
#
# # Check number of null values
# null_count = [[col,pd.isnull(messy_wide_data[col]).sum()] for col in header]
# print(null_count)
#
# # Set missing values 'nan' in "major" to 'unknown'
# # messy_wide_data.loc[messy_wide_data.major.isnull(), 'major'] = 'unknown'
# # print(messy_wide_data.major.isnull().sum())
#
# messy_wide_data.major.fillna('unknown', inplace = True)
# print(messy_wide_data.major.isnull().sum())


# 2. Load data(messy data with missing info) in long format
messy_long_data =read_from_csv('./datasets/NPAS_parsed_trunc_long_missing.csv')
# get and print header
header = print_header(messy_long_data)
# Get unique values in the 'variable' column
print(' Unique Variable IDs \n',[messy_long_data['variable'].unique()])
print(' Unique Subject IDs \n', [len(messy_long_data.subject_id.value_counts())])

print(messy_long_data[messy_long_data.variable == 'major'].isnull().sum())

major_mask = (messy_long_data.variable == 'major') & (messy_long_data.value.isnull())
messy_long_data.loc[major_mask, 'value'] = 'unknown'
print(messy_long_data[messy_long_data.variable == 'major'].isnull().sum())


# Below code doesn't work
# messy_long_data[messy_long_data.variable == 'major'].value.fillna('unknown', inplace = True)
# print(messy_long_data[messy_long_data.variable == 'major'].value.isnull().sum())

# 3. Pivot Data
# Convert the long data to wide data

def select_item_or_nan(x):
    x = x.iloc[0]
    if len(x) == 0:
        return np.nan
    else:
        return x


messy_wide_new = pd.pivot_table(messy_long_data, values = 'value', index = ['subject_id'], columns = ['variable'], aggfunc = select_item_or_nan ,fill_value = np.nan)
# print_header(messy_wide_new)

# Use reset index to move subject ID to column name
messy_wide_flat = messy_wide_new.reset_index()
# print_header(messy_wide_flat)

# Remove the label of the index columns to avoid confusion
messy_wide_flat.columns.name = None
# print_header(messy_wide_flat)

# Drop the null values
messy_wide_flat.dropna(inplace = True)
# Count unique subject_ids
print('Unique Subject IDs\n', len(messy_wide_flat.subject_id.unique()))
# print_header(messy_wide_flat)

