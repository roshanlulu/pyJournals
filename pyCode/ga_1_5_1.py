import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

'''%config InlineBackend.figure_format = 'retina'
%matplotlib inline'''

'''
# 1 plot the Normal distribution N(100, 15) using scipy.

# generate points on the x axis:
xpoints = np.linspace(40, 160, 500)

# use stats.norm.pdf to get values on the probability density function for the Normal distribution
ypoints = stats.norm.pdf(xpoints, 100, 15)

# initialize a matplotlib "figure"
fig = plt.figure(figsize=(8,5))

# get the current "axis" out of the figure
ax = fig.gca()

# plot the lines using matplotlib's plot function:
ax.plot(xpoints, ypoints, linewidth=3, color='darkred')
# plt.show()

# 2
# initialize a matplotlib "figure"
fig = plt.figure(figsize=(8,5))
ax = fig.gca()

# 68%:
ax.axvline(85, ls='dashed', lw=3, color='#333333', alpha=0.7)
ax.axvline(115, ls='dashed', lw=3, color='#333333', alpha=0.7)

ax.axvline(70, ls='dashed', lw=3, color='#666666', alpha=0.7)
ax.axvline(130, ls='dashed', lw=3, color='#666666', alpha=0.7)

ax.axvline(55, ls='dashed', lw=3, color='#999999', alpha=0.7)
ax.axvline(145, ls='dashed', lw=3, color='#999999', alpha=0.7)

ax.plot(xpoints, ypoints, linewidth=3, color='darkred')
# plt.show()
'''
# 3 Calculate the z-scores for a simple vector of values:
values = np.array([2,3,4,5,6])
print(stats.zscore(values))
