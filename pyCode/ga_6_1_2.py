import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')

df = pd.read_csv('./datasets/titanic_train.csv')
print(df.head(2))
print(df.dtypes)
print(df.isnull().sum())

# Print unique in each column
for item in df:
    print(item)
    print(df[item].nunique())

df.Cabin.unique()

# Create dummy coded variables
cabin_letter = df.Cabin.map(lambda x: 'Z' if pd.isnull(x) else x.split()[0][0])
print(cabin_letter.value_counts())
print(cabin_letter.head())

cabin_dummy = pd.get_dummies(cabin_letter, prefix='cabin')
print(cabin_dummy.head())


# Drop redundant cabin variable
cabin_dummy.drop('cabin_Z', axis = 1, inplace = True)

def cabin_numberer(x):
    try:
        return int(x.split()[0][1:])
    except:
        return 0

cabin_num = df.Cabin.map(cabin_numberer)
print(cabin_num.unique())

df['cabin_number'] = cabin_num
df = pd.concat([df, cabin_dummy], axis=1)

# Remove least useful columns
# Keep passengerid in for the sake of example
# Remove name, ticket, and cabin
df.drop('PassengerId', inplace=True, axis=1)
df.drop('Name', inplace=True, axis=1)
df.drop('Ticket', inplace=True, axis=1)
df.drop('Cabin', inplace=True, axis=1)

# Impute values for age
df.Age.fillna(df.Age.median(), inplace = True)

# Create dummy variables for embarked/droppig etc
df = pd.concat([df, pd.get_dummies(df.Embarked)], axis = 1)
df.drop('S', inplace=True, axis=1)
df.drop('Embarked', inplace=True, axis=1)

# instead of sex, create a column called 'male' with a binary value
df['Male'] = df.Sex.apply(lambda x: 'female' not in str(x))

# drop the original Sex column
df.drop('Sex', inplace=True, axis=1)

# Cleaned data
df.head()

# PART 2
# Setup predictor and target matrices

predictors = list(df.columns)
predictors.remove('Survived')

X = df[predictors]
y = df.Survived.values

# Feature Selection
from sklearn.feature_selection import SelectKBest, f_classif, chi2


# What are the top 5 features for X using KBest?
# KBest removes all but the highest scoring features

# The objects that take as input a scoring fn and returns univaroate scores
# For classification - chi1/f_classif/mutualinfo_classif


# What are the top 5 features for X using f_classif?
# What are the top 5 features for X using chi2?

skb_f = SelectKBest(f_classif, k = 5)
skb_chi2 = SelectKBest(chi2, k = 5)


# Train the data
skb_f.fit(X, y)
skb_chi2.fit(X, y)

# examine results
# examine the scores
print(skb_f.scores_)
print(skb_chi2.scores_)

# Create a dataframe for the results

kbest = pd.DataFrame([predictors, list(skb_f.scores_), list(skb_chi2.scores_)],
                     index = ['feature', 'f_classif', 'chi2 score']).T.sort_values('f_classif', ascending=False)
print(kbest)

# 4 RECURSIVE FEATURE ELIMINATION(RFE)
# RFECV is used for recursive feature elimination along with logistic regression model

from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
selector = RFECV(lr, step = 1,cv = 5, verbose = 0)
selector = selector.fit(X, y)

print(selector.support_)
print(selector.ranking_)
print(selector.grid_scores_)

# The selected columns names after feature elimination are:
rfecv_features = np.array(predictors)[selector.support_]
print(rfecv_features)

# 5. FEATURE ELIMINATION USING LASSO PENALTY (L1)
from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import StandardScaler

# Standardize predictor matrix
ss = StandardScaler()
Xs = ss.fit_transform(X)

lrcv = LogisticRegressionCV(penalty='l1', Cs=100,solver='liblinear', cv=10)

lrcv.fit(Xs, y)
print(lrcv.coef_)
print(lrcv.C_)
# print(lrcv.scores_)

lassobest = pd.DataFrame(lrcv.coef_, columns = predictors)
lassobest = lassobest.transpose()
lassobest.columns = ['lasso_coeff']
lassobest_abs = lassobest.abs().sort_values('lasso_coeff', ascending = False)

print(lassobest_abs)

# 6 COMPARE FEATURE SETS AND SELECT THE BEST MODEL

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# kbest_features = kbest.feature.values[0:5] THIS IS NOT WORKING
lassobest_features = lassobest_abs.index[lassobest.lasso_coeff != 0]

# lr = LogisticRegressionCV(Cs=lrcv.C_[0], solver = 'liblinear', penalty='l1')
lr = LogisticRegression(C=lrcv.C_[0], penalty='l1', solver='liblinear')

def score(X):
    scores = cross_val_score(lr, X, y, cv=5)
    return(scores.mean(), scores.std())

all_scores = [
    # score(X[kbest_features]),
    score(X[rfecv_features]),
    score(X[lassobest_features]),
    score(X)]

# #putting results into a dataframe
result_df = pd.DataFrame(all_scores, columns=['mean score', 'std score'], index = ['rfecv', 'lr', 'all'])
print(result_df)

lassobest.sort_values('lasso_coeff').plot(kind='bar')
plt.show()