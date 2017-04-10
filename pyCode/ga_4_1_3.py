import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

house_csv = './datasets/housing-data.csv'

house = pd.read_csv(house_csv)
house.head()