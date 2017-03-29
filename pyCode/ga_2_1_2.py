import pandas as pd
import matplotlib.pyplot as plt

# 1
# Use panda to read your csv file, encoding is for python2 compatibility
drug = pd.read_csv('./datasets/drug-use-by-age.csv', encoding = 'utf8')

print('Get head', drug.head())
print('Get tail', drug.tail())
print ('Drug shape', drug.shape)
print('Drug Columns', drug.columns)
print('Get specific column', drug['crack-use'].head())
print('Access multiple columns with list of strings', drug[['age', 'crack-use']].head())


# Data frame vs Series
# Series is to get 1 column - single []
# Data frame is a container with multiple columns - double [[]]
# Better to access pandas series column as['my_column'] and not pandas.my_column

# .info - Understand the dataset by checking the info


print(drug.info())
# Caveat - large datasets > given computer memory
# - Sample a part of the large DS
# Distributed computing env like Hadoop, Starcluster, spark

print(' Describe dataset statistics', drug.describe())
print(' Describe dataset statistics', drug[['crack-use', 'alcohol-frequency']].describe())
print('Get mean of all columns', drug.mean())



# 2 - Diamonds

diamonds = pd.read_csv('./datasets/diamonds.csv', encoding = 'utf8')
print('Info', diamonds.info())
print('Describe', diamonds.describe())
print('Head', diamonds.head())
print('Get tail', diamonds.tail())
print ('Drug shape', diamonds.shape)
print('Get specific column\n', diamonds['carat'].head())

# 3 Pandas Indexing - Changes your index files

new_index_values = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
drug.index = new_index_values

print('Get head', drug.head())
# Get specific location and rows based on names
subset = drug.loc[['B','C','D','E','F'], ['marijuana-use','marijuana-frequency']]
print('Subset', subset)
# Get specific location and rows based on indexes
subset = drug.iloc[[1,2,3,4,5], [4,5]]
print('Subset', subset)
# Get specific rows and columns based on integers and string row name
subset = drug.ix[[1,2,3,4,5], ['marijuana-use','marijuana-frequency']]
print('Subset', subset)
# Reorder your subset data tooo!! using IX
subset = drug.ix[['F','E','D'], ['marijuana-frequency','marijuana-use']]
print('Subset', subset)

# Create your own dataframe when not importing from a file
mydata = pd.DataFrame({'Letters':['A','B','C'], 'Integers':[1,2,3], 'Floats':[2.2, 3.3, 4.4]})
print('MY own Data frame', mydata)
# Examining datatypes
print('Check data types', mydata.dtypes)
# Rename and assign column 1 name to int
mydata.rename(columns={mydata.columns[1]:'int'}, inplace=True) # inplace = True updates mydata
print('My new integer column',mydata.columns)
# Rename all columns by assigning to a list of new names
mydata.columns = ['A','B','C']
print('My new data head',mydata.head())
# Reassign a value
mydata.ix[1, 'B'] = 100
print('Reassigned my valu base din row and column no/name', mydata.head())
# Reassigned multiple values with lists
mydata.ix[:, 'A'] = [0,0,0]
print('Updated Column A', mydata.head())

mydata.ix[0, ['B','C']] = [-1000, 'newstring']
print('Updated column B and C row 0', mydata.head())

# 4 - Basic plotting using Dataframes
# Plot 2 parameters using matplotlib pyplot
drug.plot(x='age', y='marijuana-use')
plt.show()

drug.hist('marijuana-use')
plt.show()

# 5 Filtering logic
marijuana_filt = (drug[drug['marijuana-use'] > 20])
print ('Marijuana Filter \n', marijuana_filt)

marijuana_20_filt = drug[(drug['marijuana-use'] > 20) & (drug.n > 4000)]
print ('Marijuana and age = 20 Filter \n', marijuana_20_filt)