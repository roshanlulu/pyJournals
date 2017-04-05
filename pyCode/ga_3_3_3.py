# Introduction to bootstrapping


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from scipy.stats import t

plt.style.use('fivethirtyeight')


starcraft = './datasets/Starcraft_sample.csv'

# Load the dataset
def load_data(path):
    df = pd.read_csv(path)
    return df

data = load_data(starcraft)

# Extract APM vector from the dataset
data_apm = data['APM']
# print(data_apm)

# Plot APM data with histogram
plt.hist(data_apm)
plt.show()

# Function for non parametric bootstrap procedure and get the bootstrap interva;
def bootstrap(sample, stat_func, iters=1000):
    boots = []
    for i in range(iters):
        random_sample = np.random.choice(sample, replace = True, size = len(sample))
        stat = stat_func(random_sample)
        boots.append(stat)
    return boots


apm_boot = bootstrap(data_apm,np.mean)
apm_lower = stats.scoreatpercentile(apm_boot, 2.5)
apm_upper = stats.scoreatpercentile(apm_boot, 97.5)

print("Bootstrap Confidence Interval\n", apm_lower, np.mean(data_apm), apm_upper)


# Get the confidence interval and compare it with the bootstrap interval
# In the solutions they ve used a different formulae for calculating confidence interval
def get_CI(sample_arr, alpha):
    print('Confidence Interval ', alpha *100, '%:')
    print(t.interval(alpha,
                     len(sample_arr) - 1,
                     loc = np.mean(sample_arr),
                     scale = stats.sem(sample_arr)))

get_CI(data_apm, 0.95)

# Plot the distribution of APM with a vertical line
median_apm = np.median(data_apm)
ax = sns.distplot(data_apm, bins = 25, kde = False)
ax.axvline(median_apm, lw = 2.5, ls = 'dashed', color = 'black')
plt.show()
