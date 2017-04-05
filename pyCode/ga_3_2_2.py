import pandas as pd
import numpy as np

currencies = pd.read_csv("./datasets/currencies_and_assets.csv")
exchanges = pd.read_csv("./datasets/exchanges_and_markets.csv")


print(exchanges.head())
print(currencies.head())