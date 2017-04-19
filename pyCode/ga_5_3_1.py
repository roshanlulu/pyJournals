import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import re
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

import imp
plotter = imp.load_source('plotter', './knn_plotter.py')
from plotter import KNNBoundaryPlotter


bcw = pd.read_csv('./datasets/wdbc.data', header=None, index_col=None)



column_names = ['id','malignant',
                'nucleus_mean','nucleus_se','nucleus_worst',
                'texture_mean','texture_se','texture_worst',
                'perimeter_mean','perimeter_se','perimeter_worst',
                'area_mean','area_se','area_worst',
                'smoothness_mean','smoothness_se','smoothness_worst',
                'compactness_mean','compactness_se','compactness_worst',
                'concavity_mean','concavity_se','concavity_worst',
                'concave_pts_mean','concave_pts_se','concave_pts_worst',
                'symmetry_mean','symmetry_se','symmetry_worst',
                'fractal_dim_mean','fractal_dim_se','fractal_dim_worst']

bcw.columns = column_names



def checkforstring(substring, string):
    return (re.search(substring, string))


remove_cols = [col for col in bcw.columns if((checkforstring('_worst', col) != None) or (checkforstring('_se', col) != None))]
bcw = bcw.drop(remove_cols, axis = 1)
print(bcw.head())

bcw['malignant'] = bcw['malignant'].map(lambda x: 0 if x == "B" else 1)

print(bcw.malignant.value_counts())


# Plot heat map for correlation
mean_corr = bcw.drop('id', axis=1).corr()

# Set the default matplotlib figure size:
fig, ax = plt.subplots(figsize=(9,7))

# Generate a mask for the upper triangle (taken from seaborn example gallery)
mask = np.zeros_like(mean_corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Plot the heatmap with seaborn.
# Assign the matplotlib axis the function returns. This will let us resize the labels.
ax = sns.heatmap(mean_corr, mask=mask, ax=ax)

# Resize the labels.
ax.set_xticklabels(ax.xaxis.get_ticklabels(), fontsize=14)
ax.set_yticklabels(ax.yaxis.get_ticklabels(), fontsize=14)

# If you put plt.show() at the bottom, it prevents those useless printouts from matplotlib.
# plt.show()

# pair plot to visualize all variables
# set the seaborn style to have a white background
sns.set(style="ticks", color_codes=True)


# This function does a pairplot across your variables with the color
# set as the outcome "malignant" class variable
def bcw_pairplotter(df, variables, sample_frac=0.3):
    # sample_frac lets you specify an amount of the data to sample for the plot.
    # this speeds up the function which can take awhile with the full data.

    # get the number of rows/data points:
    rows = df.shape[0]

    # get downsample indicies for the data, if specified
    if sample_frac < 1.0:
        sample_inds = np.random.choice(range(0, rows),
                                       size=int(round(rows * sample_frac)),
                                       replace=False).astype(int)

    # make the pairplot for the variables:
    pairs = sns.pairplot(df.iloc[sample_inds, :],
                         vars=variables,
                         hue="malignant",
                         palette=sns.xkcd_palette(['windows blue', 'amber']))

# get out the column variable names to put into the pairplotter function
colvars = [x for x in bcw if x not in ['id','malignant']]

bcw_pairplotter(bcw, colvars)
# plt.show()

# Set your target and predictor
y = bcw['malignant'].values
X = bcw[['nucleus_mean','texture_mean','perimeter_mean']]

# Standardize predictor matrix

ss = StandardScaler()
Xs = ss.fit_transform(X)

skf = StratifiedKFold(n_splits=5)
cv_indices = skf.split(Xs, y)
cv_indices = [[tr,te] for tr,te in cv_indices]


# Function to crossvalidate accuracy of a knn model acros folds
def accuracy_crossvalidator(X, y, knn, cv_indices):
    # list to store the scores/accuracy of folds
    scores = []

    # iterate through the training and testing folds in cv_indices
    for train_i, test_i in cv_indices:
        # get the current X train & test subsets of X
        X_train = X[train_i, :]
        X_test = X[test_i, :]

        # get the Y train & test subsets of Y
        Y_train = y[train_i]
        Y_test = y[test_i]

        # fit the knn model on the training data
        knn.fit(X_train, Y_train)

        # get the accuracy predicting the testing data
        acc = knn.score(X_test, Y_test)
        scores.append(acc)

        print('Fold accuracy:', acc)

    print('Mean CV accuracy:', np.mean(scores))
    return scores

baseline = 1. - np.mean(y)
print('baseline:', baseline)

# Cross-validate the mean accuracy for a KNN model with 5 neighbors

knn5 = KNeighborsClassifier(n_neighbors=5, weights='uniform')

scores = accuracy_crossvalidator(Xs, y, knn5, cv_indices)

print(scores)

# Cross-validate the mean accuracy for a KNN model with 1 neighbor

knn1 = KNeighborsClassifier(n_neighbors=1, weights='uniform')

scores = accuracy_crossvalidator(Xs, y, knn1, cv_indices)

print(scores)

kbp = KNNBoundaryPlotter(bcw, 'area_mean', 'symmetry_mean', 'malignant', nn_range=range(1,101))

# This part works only in notebook
kbp.knn_mesh_runner()
# kbp.knn_interact()

plt.show()
