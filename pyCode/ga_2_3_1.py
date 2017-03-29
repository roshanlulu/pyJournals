import sqlite3
import pandas as pd

# Common for all parts
sqlite_db = './datasets/test_db.sqlite'
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()

# # 1
# c.execute('CREATE TABLE houses (field1 INTEGER PRIMARY KEY, sqft INTEGER, bdrms INTEGER, age INTEGER, price INTEGER);')
#
# # Save (commit) the changes
# conn.commit()
#
# # 2
# last_sale = (None, 4000, 5, 22, 0)
# c.execute('INSERT INTO houses VALUES (?,?,?,?,?)', last_sale)
#
# # Remember to commit the changes
# conn.commit()
#
# recent_sales = [
#   (None, 2390, 4, 34, 319000),
#   (None, 1870, 3, 14, 289000),
#   (None, 1505, 3, 90, 269000),
# ]
#
# c.executemany('INSERT INTO houses VALUES (?, ?, ?, ?, ?)', recent_sales)
#
# conn.commit()
#
# # 3
# from numpy import genfromtxt
#
# # import into nparray of ints, then convert to list of lists
# data = (genfromtxt('datasets/housing-data.csv', dtype='i8',
#                     delimiter=',', skip_header=1)).tolist()
#
# # append a None value to beginning of each sub-list
# for d in data:
#     d.insert(0, None)
#
# # loop through data, running an INSERT on each record (i.e. sublist)
# for d in data:
#     c.execute('INSERT INTO houses VALUES (?, ?, ?, ?, ?)', d)
#
# conn.commit()
#
# # 4
#
# # similar syntax as before
# results = c.execute("SELECT * FROM houses WHERE bdrms = 4")
#
# # here results is a cursor object - use fetchall() to extract a list
# print(results.fetchall())
# conn.commit()
#
# 5
data = pd.read_csv('./datasets/housing-data.csv', low_memory=False)  # lower_memory = gets rid of ambigious warning.. nothing to see here
data.head()
data.to_sql('houses_pandas',             # Name of the table
            con=conn,                    # The handle to the file that is setup
            if_exists='replace',         # Overwrite, append, or fail
            index=False)                 # Add index as column

# 6
data.to_sql('houses_pandas',             # Name of the table
            con=conn,                    # The handle to the file that is setup
            if_exists='replace',         # Overwrite, append, or fail
            index=False)                 # Add index as column

conn.commit()

# 7
df = pd.read_sql('SELECT * FROM houses_pandas LIMIT 10', con=conn)
print(df)