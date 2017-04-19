import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')




################### My EDA Functions ######################
def explore_data(data):
    # Get first 5 rows in the dataframe
    print(data.head())
    # Get last 5 items in the dataframe
    print(data.tail())
    # Get no of rows and columns in the dataframe
    print(data.shape)
    # Get the column names
    print(data.columns)
    # # Access a specific column as a series
    # print(data['colname'].head())
    # # Access single or multiple columns as a dataframe
    # print(data[['col1name', 'col2name']].head())

def examine_data(data):
    print(data.info())
    print(data.dtypes)
    # print(data.colname.unique())

def summarize_data(data):
    print(data.describe())
    # print(data['colname'].describe())
    # print(data[['col1name', 'col2name']].describe())

def sort_data(data):
    # print(data.sort_values('col name', ascending = False).head())
    return 0

def check_null(data):
    print(data.isnull().sum())

def study_unique(data):
    for col in data.columns:
        print(col, data[col].unique())

def drop_column(data, col_name):
    data.drop([col_name], axis=1, inplace=True)
    print(data.columns)

# Plot distribution of height and weight
sns.pairplot(baseball, hue = 'team', x_vars='height_in', y_vars='weight_lb', kind="scatter", size = 7)

# Plot distribution of height and weight
sns.distplot(baseball['height_in'], bins = 7, kde = False, color = 'r', vertical = False)

sns.jointplot(baseball.height_in.values, baseball.weight_lb.values)
###########################################################


file_path = './datasets/baseball_height_weight.csv'
baseball = pd.read_csv(file_path)
explore_data(baseball)
examine_data(baseball)
study_unique(baseball)
# Plot distribution of height and weight
sns.pairplot(baseball, hue = 'team', x_vars='height_in', y_vars='weight_lb', kind="scatter", size = 7)
plt.show()

# Plot distribution of height and weight
sns.distplot(baseball['height_in'], bins = 7, kde = False, color = 'r', vertical = False)

