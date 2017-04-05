import urllib.request
data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
urllib.request.urlretrieve(data_url, "./datasets/housing.data")

names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]

import pandas as pd
data = pd.read_csv("./datasets/housing.data", header=None, names=names, delim_whitespace=True)

NOX = data['NOX'].values
AGE = data['AGE'].values

import numpy as np
import scipy.stats as stats
from scipy.stats import t
import matplotlib.pyplot as plt

# 1

def get_stats(sample_arr):
    mean_sample = np.mean(sample_arr)
    stddev_sample = np.std(sample_arr)
    stderr_sample = stats.sem(sample_arr)
    print('Mean:\n', mean_sample)
    print('Std Deviation:\n', stddev_sample)
    print('Standard Error of Mean(SEM):\n', stderr_sample)

get_stats(AGE)

# 2
def get_CI(sample_arr, alpha):
    print('Confidence Interval ', alpha *100, '%:')
    print(t.interval(alpha,
                     len(sample_arr) - 1,
                     loc = np.mean(sample_arr),
                     scale = stats.sem(sample_arr)))
                     # scale = np.std(sample_arr, ddof = 1)/(len(sample_arr))**0.5))



get_CI(AGE, 0.9)
get_CI(AGE, 0.95)
get_CI(AGE, 0.99)
# As the confidence interval increases the Confidence increases that the mean value lies int he confidence range

# 3
def plot_histogram(sample_arr):
    plt.hist(sample_arr)
    plt.show()

# plot_histogram(AGE)

# 4
get_CI(NOX, 0.95)

# 5

def get_tstats(ctrl_sample, exp_sample):
    t_stat = stats.ttest_ind(exp_sample, ctrl_sample)
    print('t-statistics( is:\n', t_stat)
    # return(t_stat)


# # Step 1: Define your hypotheis
# # H0 - Mean NOX = Median NOX
# # H1 - Mean NOX != Median NOX
#
# # Step 2: Set your alpha
# alpha = 0.05
#
# # Step 3: Calculate point estimate --> Mean of NOX
# sample_mean = np.mean(NOX)
#
# # Step 4: Calculate test statistic
# sample_median = np.median(NOX)
# sample_std = np.std(NOX)
# sample_sem = stats.sem(NOX)
# t_statistic = (sample_mean - sample_median)/sample_std/sample_sem
# p_value =
