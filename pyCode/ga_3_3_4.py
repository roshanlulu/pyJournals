# Pandas Data Munging Full Overview

import pandas as pd
import numpy as np
###########################################################################
# Loading data table from remote location

path = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
data = pd.read_table(path)
print(data.head())

data = pd.read_table(path, sep = '|', na_filter=False)
print(data.head())


###########################################################################
# Basic examination of data frames
print('Table type: ', type(data))

print(data.head(10))
print(data.tail(2))

print('Index: \n', data.index)
print('Columns: \n', data.columns)

print('Data types: \n', data.dtypes)
print('Dimensionns of data frame: \n', data.shape)

# Get the data as an array
data_array = data.values
print('New array \n', data_array.shape, type(data_array))

###########################################################################
# Selecting columns

gender_data = data.gender
print('Printing gender column\n', gender_data.head())
print('Type of gender column', type(gender_data))

gen_occ_data = data[['gender', 'occupation']]
print('Printing gender and occupation column\n', gen_occ_data.head())
print('Type of gender and occupation column', type(gen_occ_data))

###########################################################################
# Describing the data
print('Data description of numeric values\n')
print(data.describe())

print('Data description of object\n')
print(data.describe(include = ['object']))

print('Data description of all columns\n')
print(data.describe(include = 'all'))

print('Description of gender series\n', data.gender.describe())

print('Mean age(column): ', data.age.mean())

print('Distinct count of gender:\n', data.gender.value_counts())
print('Distinct count of age:\n', data.age.value_counts())

###########################################################################

# Exercise 1
drinks_csv = 'https://raw.githubusercontent.com/josephnelson93/GA-DSI/master/example-lessons/plotting-with-pandas/drinks.csv'
user_file = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user_original'

# drinks_csv
data = pd.read_table(drinks_csv, sep=',')
print(data.head())
print(data.tail())
print(data.index)
print(data.columns)
print(data.dtypes)
print(data.shape)
print(data.beer_servings.describe())
print(data.beer_servings.median())
print(data.continent.value_counts())

# user_file
data = pd.read_table(user_file, sep='|')
user_column = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
data.columns = user_column
print(data.head())
print(data.shape)
print(data.occupation.value_counts()[0:3])


# Filtering and sorting dataframes and series
# Boolean filtering
mask = data.age < 20
print(data[mask].occupation.value_counts())
mask = (data.age < 20) & (data.gender == 'M')
mask = (data.age < 10) | (data.age > 70)
print(data[mask])

# Sorting
# Sort and return the age column
print(data.age.sort_values())
# Sort the whole dataframe based on age column ascending
print(data.sort_values('age'))
# Sort the whole dataframe based on age column descending
print(data.sort_values('age', ascending=False))


###########################################################################

###########################################################################

###########################################################################

###########################################################################

###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################