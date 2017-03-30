# import standard modules
import pandas as pd
from pandas.io import sql


# import sqlite modules
import sqlite3

# Connect to sqlite3 database for cars
connection = sqlite3.connect('./sql/Cars.db.sqlite')
c = connection.cursor()

# Function definitions
def db_query(text, conn):
    result = sql.read_sql(text, conn)
    return result


# # 1
# # If you don't specify the type encoding as 'utf-8' you're going to have a bad time when you try to convert to SQL
# cars = pd.read_csv('./datasets/car-names.csv', encoding = 'utf-8')
# print(cars)
#
#
# # Convert the csv file to an sql file
# cars.to_sql(name = 'car_names', con = connection, if_exists = 'replace', index = False)
#
# # 2 - Create a table for car_makers
#
# c.execute('CREATE TABLE car_makers (field1 INTEGER PRIMARY KEY, maker INTEGER);')
# connection.commit()
# cars = pd.read_csv('./datasets/car-makers.csv', encoding = 'utf-8')
# cars.to_sql(name = 'car_makers', con = connection, if_exists = 'replace', index = False)
# connection.commit()
#
# # 3 Create a table for car_data
# c.execute('CREATE TABLE car_data (field1 INTEGER PRIMARY KEY, maker SUBSTRING , make SUBSTRING);')
# connection.commit()
#
# cars = pd.read_csv('./datasets/cars-data.csv', encoding = 'utf-8')
# cars.to_sql(name = 'car_data', con = connection, if_exists = 'replace', index = False)
# connection.commit()
#
# # 4 Read the car names from database to data frame
# cars = sql.read_sql('SELECT * FROM car_names', con = connection)
# print(cars)
#
# # 5 Query a database using Pandas and return a dataframe
#

#
# print(db_query(("SELECT MODEL FROM car_names"), connection))
#
# # 6
# print(db_query(("SELECT * FROM car_names LIMIT 5"), connection))
#
# # 7
#
# ferrari = (None, 'Ferrari','The Ferrari')
# tesla = [None, 'Tesla', None]
#
# # connection.execute('INSERT INTO car_names VALUES (?, ?, ?)', ferrari)
# connection.execute('INSERT INTO car_names VALUES (?, ?, ?)', tesla)
# connection.commit()

# 8
print(db_query('SELECT * FROM car_names WHERE car_names."Model" = "Tesla"', connection))

# 9
print(db_query('SELECT * FROM car_makers LIMIT 5', connection))

# 10
print(db_query('SELECT * FROM car_data LIMIT 5', connection))

# 11

inner_join = db_query('SELECT car_names."Make", car_data."MPG", car_data."Horsepower", car_data."Year" '
'FROM car_names '
'INNER JOIN car_data '
'ON car_names."Id"=car_data."Id"', connection)

# print(inner_join.tail())
print(inner_join.info())
# 12

left_join = db_query('SELECT car_names."Make", car_data."MPG", car_data."Horsepower", car_data."Year" '
                     'FROM car_names '
                     'LEFT JOIN car_data '
                     'ON car_names."Id" = car_data."Id"', connection)


# print(left_join.tail())
print(left_join.info())