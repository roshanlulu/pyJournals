
# Necessary Libraries
import pandas as pd
import sqlite3
from pandas.io import sql



# 1 Reading CSV to Dataframe
orders = pd.read_csv('./datasets/EuroMart-ListOfOrders.csv', encoding = 'utf-8')
OBD =  pd.read_csv('./datasets/EuroMart-OrderBreakdown.csv', encoding = 'utf-8')
sales_targets =  pd.read_csv('./datasets/EuroMart-SalesTargets.csv', encoding = 'utf-8')


# 2
orders.columns = [col.replace(' ', '')  for col in orders.columns]
OBD.columns = [col.replace(' ', '').replace('-', '')  for col in OBD.columns]
sales_targets.columns = [col.replace(' ', '')  for col in sales_targets.columns]

# 3
OBD.Sales = [float(val.replace('$', '').replace(',','')) for val in OBD.Sales]
OBD.Profit = [float(val.replace('$', '').replace(',','')) for val in OBD.Profit]
# 4
# Establishing Local DB connection
db_connection = sqlite3.connect('./sql/EuroMart.db.sqlite')
c = db_connection.cursor()

# Function definitions
def db_query(text, conn = db_connection):
    result = sql.read_sql(text, conn)
    return result

orders.to_sql(name = 'orders', con = db_connection, if_exists = 'replace', index = False)
OBD.to_sql(name = 'OBD', con = db_connection, if_exists = 'replace', index = False)
sales_targets.to_sql(name = 'sales_targets', con = db_connection, if_exists = 'replace', index = False)

# 5
orders_by_cust = orders.groupby('CustomerName').OrderID.describe()

sql_query1 = '''
SELECT "CustomerName", COUNT('OrderID') as NoofOrders
FROM orders
GROUP BY "CustomerName"
'''



# 6
sql_query = '''
SELECT "City", "Country", "Region"
FROM orders
GROUP BY "CustomerName"
'''

print(db_query(sql_query))

# 7
sql_query = '''
SELECT "OrderID", "Profit"
FROM OBD
WHERE "Profit" < 0
'''

print(db_query(sql_query))

# 8
sql_query = '''
SELECT o."OrderID", o."CustomerName", b."ProductName"
FROM orders as o
LEFT JOIN OBD as b
ON o."OrderID" = b."OrderID"
'''

print(db_query(sql_query))

# 9
sql_query = '''
SELECT o."OrderID", b."Category", o."Country"
FROM orders as o
LEFT JOIN OBD as b
ON o."OrderID" = b."OrderID"
WHERE o."Country" = 'Sweden' and b."Category" = "Office Supplies"
'''

print(db_query(sql_query))

print(db_query(sql_query1))