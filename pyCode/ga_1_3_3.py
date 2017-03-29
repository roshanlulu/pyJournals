import numpy as np
from scipy.stats import mode

'''
samples = [1,2,3,4,5,6,7,8,9,5.3,55.22]

meanofsamples = np.mean(samples)
medianofsamples = np.median(samples)
modeofsamples = mode(samples)

print (meanofsamples, medianofsamples, modeofsamples)
'''

# measures-of-central-tendency-practice
dist = [33.3, 8.0, 2.7, 7.0, 11.3, 10.2, 38.4, 14.7, 46.9, 6.6, 38.6, 41.1, 20.4, 19.5,
        102.6, 111.5, 21.8, 27.0, 30.3, 9.3, 19.6, 31.1, 48.8, 8.9, 11.4, 0.6, 23.5,
        8.0, 27.5, 69.7, 11.5, 15.5, 1.4, 7.0, 4.6, 6.0, 16.0, 17.2, 6.3, 26.2, 23.9,
        45.9, 55.4, 100.8, 22.9, 75.5, 115.5, 58.9, 10.5, 92.6, 12.4, 102.7, 10.2, 167.6,
        143.6, 132.3, 134.2, 39.4, 49.7, 12.0, 27.0, 1.3, 4.7, 5.0, 24.1, 21.5, 33.1,
        45.6, 46.3, 15.8, 30.7, 15.7, 6.8, 64.6, 39.1, 2.9, 8.0, 5.4, 33.4, 40.0, 22.7,
        24.2, 25.7, 85.0, 26.2, 3.3, 20.7, 117.4, 66.8, 44.3, 37.9, 71.8, 161.4, 45.9,
        4.6, 6.6, 12.6, 24.4, 21.4, 33.6, 33.7, 18.8, 7.6, 36.3, 1.8, 83.2, 75.1, 71.3,
        32.9, 30.6, 16.0, 6.9, 11.0, 9.4, 11.7, 13.8, 39.4, 4.3, 38.1, 60.1, 78.2, 49.6,
        14.3, 8.0, 19.3, 30.8, 32.5, 29.6, 28.3, 32.4, 35.7, 36.7, 10.0, 8.5, 12.2, 22.6,
        32.1, 25.7, 14.1, 20.9, 23.8, 29.5, 2.9, 42.3, 19.9, 47.5, 15.9, 6.0, 19.3, 38.2,
        23.5, 2.7, 27.0, 49.9, 43.5, 31.7, 39.1, 15.1, 18.0, 33.8, 32.1, 50.7, 28.8, 11.6,
        74.8, 16.2, 8.3, 36.3, 44.0, 15.6, 48.9, 7.3, 8.2, 29.8, 38.7, 3.9, 7.2, 5.1, 23.7,
        48.4, 92.0, 64.3, 97.4, 99.1, 18.0, 7.1, 14.7, 47.1, 41.3, 44.2, 6.5, 44.4, 9.7,
        15.5, 23.7, 34.5, 19.9, 58.6, 35.0, 66.1, 74.5, 45.2]

meanofdist = np.mean(dist);
medianofdist = np.median(dist);
roundofdist = sorted(np.round(dist, 0))
modeofdist = mode(dist)

print(meanofdist, medianofdist, roundofdist, modeofdist)

# Check skewed
skewtype = ''
if (meanofdist < medianofdist):
    skewtype = 'negative or left skewed'
elif (meanofdist > medianofdist):
    skewtype = 'positive or right skewed'
else:
    skewtype = 'symmetric'

print('The data is ' + skewtype)

rangeofdist = np.ptp(dist)
print(rangeofdist)

varianceofdist = np.var(dist)
print(varianceofdist)

stddevofdist = np.std(dist)
print(stddevofdist)

for n in dist: