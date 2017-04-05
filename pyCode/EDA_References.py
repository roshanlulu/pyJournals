# Reference - Intro to pandas : 2.1.2, 2.1.3
import pandas as pd
import matplotlib.pyplot as plt


# Import data from csv
data = pd.read_csv('Relative path to dataset')

# What is the difference between a pandas Series and DataFrame object?
# - Essentially, a Series object contains the data for a single column of your data, and the DataFrame is a matrix-like container for those Series objects that comprise your data.
# - If your column names have no spaces or other special characters , yu can access it as a property of the datafram
#   preferred way is df['my_column'] over df.my_column .


# Exploring data using DataFrames
def explore_data(data):
    # Get first 5 rows in the dataframe
    print(data.head())
    # Get last 5 items in the dataframe
    print(data.tail())
    # Get no of rows and columns in the dataframe
    print(data.shape)
    # Get the column names
    print(data.columns)
    # Access a specific column as a series
    print(data['colname'].head())
    # Access single or multiple columns as a dataframe
    print(data[['col1name', 'col2name']].head())

# Typical problems when working with new datasets:
# Missing values
# Unexpected types (string/object instead of int/float)
# Dirty data (commas, dollar signs, unexpected characters, etc)
# Blank values that are actually "non-null" or single white-space characters
def examine_data(data):
    print(data.info())
    print(data.dtypes)
    print(data.colname.unique())

def summarize_data(data):
    print(data.describe())
    print(data['colname'].describe())
    print(data[['col1name', 'col2name']].describe())

new_index_values = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
def index_data(data):
    # Update the index
    data.index = new_index_values
    # Using the .loc indexer, we can pull out the rows and the columns
    subset = data.loc[['B', 'C', 'D', 'E', 'F'], ['marijuana-use', 'marijuana-frequency']]
    subset = data.iloc[[1, 2, 3, 4, 5], [4, 5]]
    subset = data.ix[[1, 2, 3, 4, 5], ['marijuana-use', 'marijuana-frequency']]

# The simplest way to create your own dataframe when not importing from a file is to give the pd.DataFrame() instantiator a dictionary.
data_dict = {'Letters':['A','B','C'], 'Integers':[1,2,3], 'Floats':[2.2, 3.3, 4.4]}
def create_dataframe(dict):
    data = pd.Dataframe(dict)

def rename_data(data):
    # Rename one column name
    data.rename(columns = {data.columns[1]:'new_name'}, inplace = True)
    # Rename every column name - assign a new column name to .columns property
    data.columns = ['A', 'B','C']
    # We can assign values using indexing [row, columns]
    data.ix[1, 'B'] = 100
    # Assign multiple values at once
    data.ix[:, 'A'] = 0
    data.ix[0, ['B', 'C']] = [-1000, 'newstring']

def plot_data(data):
    data.plot(x='col name1', y='col name2')
    data.hist('col name')
    data['col name'].hist()
    plt.show()

def filter_data(data):
    print(data[data['col name'] > 20])
    print(data[(data['col name1'] > 20) & (data['col name 2'] > 4000)])

def sort_data(data):
    print(data.sort_values('col name', ascending = False).head())
