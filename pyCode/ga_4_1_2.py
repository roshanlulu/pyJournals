import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

sac_csv = './datasets/sacramento_real_estate_transactions.csv'

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
    print(sac.isnull().sum())

def study_unique(data):
    for col in data.columns:
        print(col, data[col].unique())

def drop_column(data, col_name):
    data.drop([col_name], axis=1, inplace=True)
    print(data.columns)

# def drop_row(data, )
###########################################################


sac = pd.read_csv(sac_csv)

''' Step 1: Study the data '''
# explore_data(sac)
# examine_data(sac)
# summarize_data(sac)
# sort_data(sac)
# check_null(sac)
# study_unique(sac)

# Data findings for the next step
# States - 2 CA and AC
# Type - 3 types and 1 Unknown (clean that data)
# Sale dates - 5 dates. Can check for any pattern there


''' Step 2: Based on any specific finding in Step 1, dig further into data '''
# Since there are 2 States, it would be interesting to split the data into 2 tables
# mask = [sac.state == 'CA']
sac_state_AC = sac[sac.state == 'AC']
# explore_data(sac_state_AC)
# State AC has only 1 data point and mostly is a typo. Hence we can drop the state column from the sac dataset.
drop_column(sac, 'state')

# Check the no of houses in each city
print(sac.city.value_counts())
# 50% of data points are in Sacramento, followed by Elk Grove, then Lincoln

# Check the no of types of houses
print(sac.type.value_counts())
# Check the data that is unknown type
unknown = (sac[sac.type == 'Unkown'])
print(unknown)
# This is not a valid data as the house description is not valid
sac.drop(sac.index[unknown.index], axis=0, inplace=True)
print(sac.type.value_counts())
# Majority of the housing is residential, with ~ 5 % Condos and ~1.5% Multi-family

# Check if the house information is valid or not
print(sac.beds.value_counts())
print(sac.baths.value_counts())
print(sac.sq__ft.value_counts())

zero_area = sac[sac.sq__ft == 0]
sac.drop(sac.index[zero_area.index], axis=0, inplace=True)

# 3
# sqft , beds and baths maybe good predictors for determining the pricing.
# Plot the predictors against the pricing

# beds against price
sns.pairplot(sac, hue = 'city', x_vars='beds', y_vars='price', kind="scatter", size = 8)
sns.pairplot(sac, hue = 'city', x_vars='baths', y_vars='price', kind="scatter", size = 8)
sns.pairplot(sac, hue = 'city', x_vars='sq__ft', y_vars='price', kind="scatter", size = 8)
plt.show()


sns.lmplot(x='beds', y='price', data=sac)
sns.lmplot(x='baths', y='price', data=sac)
sns.lmplot(x='sq__ft', y='price', data=sac)
plt.show()


