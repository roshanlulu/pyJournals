import matplotlib
import numpy as np
import scipy.stats as stats
import csv
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

csv_rows = []
with open('./sales_info.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        csv_rows.append(row)
f.close()
header = csv_rows[0]
data = csv_rows[1::]

plt.show()
# get each column as a list

