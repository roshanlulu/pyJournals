import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

house_csv = './datasets/housing-data.csv'

house = pd.read_csv(house_csv)
print(house.dtypes)
house.price = [float(price/1000) for price in house.price]
print(house.head())

# Define target and predictor
price= house.price.values
sqft = house.sqft.values

def calculate_yhat(x, b0, b1):
    return b0 + b1*x


def plot_regression(x, y, b0, b1):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.gca()

    yhat = calculate_yhat(x, b0, b1)

    ax.scatter(x, y, color='steelblue', s=70)
    ax.scatter(x, yhat, color='darkred', s=70, alpha=0.3)

    min_x, max_x = np.min(x), np.max(x)
    min_yhat = calculate_yhat(min_x, b0, b1)
    max_yhat = calculate_yhat(max_x, b0, b1)

    ax.plot([min_x, max_x], [min_yhat, max_yhat], color='darkred',
            linewidth=2.0, alpha=0.7)

    plt.show()

b0 = 0
b1 = 1
plot_regression(sqft, price, b0, b1)

def calculate_residuals(y, yhat):
    return y - yhat


# R2
# Calculate the R^2 of the multiple regression model.
def calc_r2(price,yhat):
   r2 = calculate_r2(price, yhat)
   if r2 >= 0.8 and r2 <= 1.0:
       print('Multiple regression R^2 is %s. This is a STRONG correlation! ' % r2)
   elif r2 >= 0.5 and r2 <= 0.8:
       print('Multiple regression R^2 is %s. This is a MODERATE correlation! ' % r2)
   elif r2 >= 0 and r2 <= 0.5:
       print('Multiple regression R^2 is %s. This is a WEAK correlation! ' % r2)
   return r2

calc_r2(price,yhat)