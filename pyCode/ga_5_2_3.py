import numpy as np
import pandas as pd
import patsy

from sklearn.linear_model import Ridge, Lasso, ElasticNet, LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from sklearn.cross_validation import cross_val_score

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

kobe = pd.read_csv('./datasets/kobe_superwide_games.csv')

kobe_n = kobe.drop(kobe.columns[22:], axis = 1, inplace = False)

# A:
data = kobe
fold_num = 10
# Target
y = data.SHOTS_MADE.values
# Predictor
X = data.iloc[:,1:]

# Initialize the StandardScaler object
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

# use the "fit_transform" function to standardize the X design matrix
Xs = ss.fit_transform(X)

# A:
linreg = LinearRegression()

lin_reg_scores = cross_val_score(linreg, Xs, y, cv = fold_num)
print(lin_reg_scores)
print(np.mean(lin_reg_scores))

# A:
ridge_alphas = np.logspace(0, 5, 200)
optimal_ridge = RidgeCV(alphas = (ridge_alphas), cv = fold_num)
optimal_ridge.fit(Xs, y)
print(optimal_ridge.alpha_)

# A:
ridge = Ridge(alpha=optimal_ridge.alpha_)

ridge_scores = cross_val_score(ridge, Xs, y, cv = fold_num)
print(ridge_scores)
print(np.mean(ridge_scores))

# A:
optimal_lasso = LassoCV(n_alphas=500, cv=fold_num, verbose=1)
optimal_lasso.fit(Xs, y)
optimal_lasso.alpha_

# A:
lasso = Lasso(alpha=optimal_lasso.alpha_)

lasso_scores = cross_val_score(lasso, Xs, y, cv = fold_num)
print(lasso_scores)
print(np.mean(lasso_scores))

lasso.fit(Xs, y)

lasso_coefs = pd.DataFrame({'variable':X.columns,
                            'coef':lasso.coef_,
                            'abs_coef':np.abs(lasso.coef_)})

lasso_coefs.sort_values('abs_coef', inplace=True, ascending=False)

lasso_coefs.head(20)

print('Percent variables zeroed out:', np.sum((lasso.coef_ == 0))/float(X.shape[0]))

l1_ratios = np.linspace(0.01, 1.0, 25)

optimal_enet = ElasticNetCV(l1_ratio=l1_ratios, n_alphas=100, cv=10,
                            verbose=1)
optimal_enet.fit(Xs, y)

print(optimal_enet.alpha_)
print(optimal_enet.l1_ratio_)

enet = ElasticNet(alpha=optimal_enet.alpha_, l1_ratio=optimal_enet.l1_ratio_)

enet_scores = cross_val_score(enet, Xs, y, cv=10)

print(enet_scores)
print(np.mean(enet_scores))


# Need to fit the ElasticNet and Ridge outside of cross_val_score like i did with the ridge
ridge.fit(Xs, y)
lasso.fit(Xs, y)


# model residuals:

ridge_resid = y - ridge.predict(Xs)
lasso_resid = y - lasso.predict(Xs)

sns.jointplot(ridge_resid, lasso_resid)
plt.show()
