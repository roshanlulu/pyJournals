from sqlalchemy import create_engine
import psycopg2

import pandas as pd

conn_str = "host='dsi.c20gkj5cvu3l.us-east-1.rds.amazonaws.com' dbname='northwind' user='dsi_student' password='gastudents'"
conn = psycopg2.connect(conn_str)


def get_from_db(sql_query, db = conn):
    return(pd.read_sql(sql_query, db))

# 1
SQL_STRING = '''

SELECT "ProductID" as PID, "ProductName", "SupplierID", "UnitPrice"
FROM Products as P
WHERE P."UnitPrice" > 25
ORDER BY "SupplierID" DESC,"UnitPrice" DESC

'''


# 2
SQL_STRING = '''
SELECT "CompanyName" as "Company Name", "SupplierID" as "Supplier No."
FROM Suppliers as s
ORDER BY "Company Name" ASC

'''

# 3
SQL_STRING = '''
SELECT "ProductName" as "Ch Products"
FROM Products as P
WHERE "ProductName" LIKE '%ch%'
ORDER BY "ProductName" DESC

'''

# 4
SQL_STRING = '''
SELECT "City" as "S cities"
FROM Suppliers as S
WHERE "City" LIKE 'S%'
ORDER BY "City" ASC

'''


# 5
SQL_STRING = '''
SELECT DISTINCT "SupplierID", "ProductName", "UnitPrice"
FROM Products as P
ORDER BY "UnitPrice" ASC

'''

# 6
SQL_STRING = '''

SELECT sub."Top 5 A Products", sub."UnitPrice"
FROM 
    (SELECT "ProductName" as "Top 5 A Products", "UnitPrice" 
    FROM Products
    WHERE "ProductName" LIKE  '%a%'
    ORDER BY "UnitPrice" DESC
    LIMIT 5) AS sub
ORDER BY 1 ASC

'''

# 7
SQL_STRING = '''
SELECT "OrderID", COUNT("OrderID"), SUM("UnitPrice" * "Quantity")
FROM order_details
GROUP BY "OrderID"
ORDER BY 3 DESC
'''

# 8
SQL_STRING = '''


'''


print(get_from_db(SQL_STRING))
