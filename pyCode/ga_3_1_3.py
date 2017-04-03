import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sqlalchemy import create_engine

# DSN format for database connections:  [protocol / database  name]://[username]:[password]@[hostname / ip]:[port]/[database name here]
engine = create_engine('postgresql://dsi_student:gastudents@dsi.c20gkj5cvu3l.us-east-1.rds.amazonaws.com:5432/northwind')

# Function to run sql commands
def run_sql(sql_cmd):
    return(pd.read_sql(sql_cmd, engine))


sql_select_table = '''
    SELECT tablename 
    FROM pg_catalog.pg_tables 
    WHERE schemaname='public' 
    LIMIT 5
'''
# print(run_sql(sql_select_table))


sql_inspect_db = '''
    SELECT tablename 
    FROM pg_catalog.pg_tables 
    WHERE schemaname='public'
'''

# print(run_sql(sql_inspect_db))

sql_print_schema = '''
    SELECT table_name, data_type, table_schema
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE "table_schema" = 'public' 
'''

# print(run_sql(sql_print_schema))

sql_table_peek_states = '''
    SELECT *
    FROM usstates
    LIMIT 3
'''

sql_table_peek_orders = '''
    SELECT *
    FROM orders
    LIMIT 3
'''

sql_table_peek_products = '''
    SELECT *
    FROM products
    LIMIT 3
'''

sql_table_peek_categories = '''
    SELECT *
    FROM categories
    LIMIT 3
'''
# print(run_sql(sql_table_peek_states))
# print(run_sql(sql_table_peek_orders))
# print(run_sql(sql_table_peek_products))
# print(run_sql(sql_table_peek_categories))

sql_category_products = '''
    SELECT DISTINCT "CategoryID" , "CategoryName"
    FROM categories
'''

# print(run_sql(sql_category_products))

sql_products_per_category = '''
    SELECT "CategoryID", COUNT("ProductName") AS "Products Per Category"
    FROM products
    GROUP BY "CategoryID"
'''

# print(run_sql(sql_products_per_category))

sql_disc_products = '''
    SELECT "CategoryID", COUNT(*) AS "Products Per Category"
    FROM products
    WHERE "Discontinued" != 1
    GROUP BY "CategoryID"
'''

# print(run_sql(sql_disc_products))

sql_top_five = '''
    SELECT "ProductName", "UnitPrice", "Discontinued"
    FROM products
    WHERE "Discontinued" != 1
    ORDER BY "UnitPrice" DESC 
    LIMIT 5
'''

print(run_sql(sql_top_five))