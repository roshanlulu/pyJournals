# Hypothesis testing using Frequentist methods: a drug efficacy experiment

import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

control = np.array([166, 165, 120,  94, 104, 166,  98,  85,  97,  87, 114, 100, 152,
                    87, 152, 102,  82,  80,  84, 109,  98, 154, 135, 164, 137, 128,
                    122, 146,  86, 146,  85, 101, 109, 105, 163, 136, 142, 144, 140,
                    128, 126, 119, 121, 126, 169,  87,  97, 167,  89, 155])

experimental = np.array([ 83, 100, 123,  75, 130,  77,  78,  87, 116, 116, 141,  93, 107,
                         101, 142, 152, 130, 123, 122, 154, 119, 149, 106, 107, 108, 151,
                         97,  95, 104, 141,  80, 110, 136, 134, 142, 135, 111,  83,  86,
                         116,  86, 117,  87, 143, 104, 107,  86,  88, 124,  76])


# Calculate sample mean
def get_mean_diff(ctrl_sample, exp_sample):
    mean_ctrl = np.mean(ctrl_sample)
    mean_exp = np.mean(exp_sample)
    print('Mean of control group \n', mean_ctrl)
    print('Mean of exp group \n', mean_exp)
    mean_diff = mean_exp - mean_ctrl
    print('Mean Difference between groups: \n', mean_diff)

get_mean_diff(control, experimental)


# Calculate t-statistic - quantify the difference between groups
def get_tstats(ctrl_sample, exp_sample):
    t_stat = stats.ttest_ind(exp_sample, ctrl_sample)
    print('t-statistics( is:\n', t_stat)
    return(t_stat)


def plot_tdist(t_stat_value):
    xpoints = np.linspace(-4, 4, 1000)
    ypoints = stats.t.pdf(xpoints, (50+50+2), 0, 1)
    fig = plt.figure(figsize=(8,5))
    ax = fig.gca()
    ax.plot(xpoints, ypoints, linewidth = 3, color = 'darkred')
    ax.axvline(t_stat_value[0], color='black', linestyle='--', lw=5)
    plt.show()

t_stat = get_tstats(control, experimental)
plot_tdist(t_stat)

lower_tail = stats.t.cdf(-1.89, (50+50-2), 0, 1)
upper_tail = 1. - stats.t.cdf(1.89, (50+50-2), 0, 1)
p_value = lower_tail+upper_tail
print('p-value\n',p_value)


# Generate your random number group
def generate_group(mean, std, n):
    return np.random.normal(mean, std, size=n)


def plot_sns(group1, group2):
    fig = plt.figure(figsize=(10, 5))
    # get the current axis out of the figure
    ax = fig.gca()
    # create a distribution plot with seaborn's distplot, passing in the axis and also returning it:
    # first plot group 1:
    ax = sns.distplot(g1, bins=20, color='steelblue', ax=ax)
    # create another distribution on the same axis for group 2:
    sns.distplot(g2, bins=20, color='darkred', ax=ax)
    plt.show()


g1 = generate_group(100, 5, 50)
g2 = generate_group(110, 5, 50)
plot_sns(g1, g2)
# calculate the p-value
print(stats.ttest_ind(g1, g2))

g1 = generate_group(100, 50, 50)
g2 = generate_group(110, 50, 50)