
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

sales_data = pd.read_csv("./datasets/sales_info.csv")
sales_df = pd.DataFrame(sales_data)
print(sales_df)

def plot_data(plt_type, val):
    sales_df[:val].plot('volume_sold', '2015_q1_sales', kind = plt_type)
    plt.ylabel('2015 Q1 sales')
    plt.xlabel('Volume Sold')

# 1, 2
print(len(sales_df))
plot_data('scatter', len(sales_df))
plot_data('line', 10)
plot_data('bar', 10)

# 3
sales_df['2015_margin'].plot.hist()

# 4
sns.pairplot(sales_df)

# 5
sns.boxplot(sales_df)

sns.heatmap(sales_df.corr())
plt.show()