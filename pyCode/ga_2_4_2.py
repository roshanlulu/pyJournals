import numpy as np
import pandas as pd
#
# vector1 = np.array([1,2,3,4])
# vector2 = np.array([5,6,7,8])
#
# print("Vector 1\n", vector1)
# print(vector1.shape)
# print("Vector 2\n", vector2)
# print(vector1.shape)
# vector_cat = (np.concatenate((vector1, vector2), axis=0))
# print("Concatenated Vector\n", vector_cat)
#
# # Add a new axis in axis = 0
# vector1_2d = vector1[:,np.newaxis]
# print("2 Dimensional Vector 1, axis = 0 \n", vector1_2d)
# print(vector1_2d.shape)
#
# # Add a new axis in axis = 1
# vector1b_new = vector1[np.newaxis, :]
# print("2 Dimensional Vector 1, axis = 1\n", vector1b_new)
# print(vector1b_new.shape)
#
# vector2_2d = vector2[:, np.newaxis]
# print("2 Dimensional Vector 2\n", vector2_2d)
# print(vector2_2d.shape)
#
# # Concatenate 2D vector 1 and 2 D vector 2 vertically
# vector_vstack = (np.concatenate((vector1_2d, vector2_2d), axis = 0))
# print("Vertical stack of 2D Vectors\n", vector_vstack)
# print(vector_vstack.shape)
# # Concatenate 2D vector 1 and 2 D vector 2 horizontally
#
# vector_hstack = (np.concatenate((vector1_2d, vector2_2d), axis = 1))
# print("Horizontal stack of 2D Vectors\n", vector_hstack)
# print(vector_hstack.shape)
#
#
# # Concatenation using pandas
# '''Note: If you add along axis = 0, the column dimension changes. axis = 1, row dimension changes'''
# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
#                     'B': ['B0', 'B1', 'B2', 'B3'],
#                     'C': ['C0', 'C1', 'C2', 'C3'],
#                     'D': ['D0', 'D1', 'D2', 'D3']},
#                     index=[0, 1, 2, 3])
#
# df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
#                     'B': ['B4', 'B5', 'B6', 'B7'],
#                     'C': ['C4', 'C5', 'C6', 'C7'],
#                     'D': ['D4', 'D5', 'D6', 'D7']},
#                     index=[4, 5, 6, 7])
#
# print(pd.concat([df1, df2], axis = 0))
# print(pd.concat([df1, df2], axis = 1))
# print(pd.concat([df1, df2.reset_index(drop=True)], axis=1))
#


# Left , Right , Inner Outer joins using Panda
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data)
print(df_a)

raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data)
print(df_b)

raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data)
print(df_n)


print(pd.merge(df_a, df_b, on='subject_id', how='left'))

print(pd.merge(df_a, df_b, on='subject_id', how='right'))

print(pd.merge(df_a, df_b, on='subject_id', how='outer'))

print(pd.merge(df_a, df_b, on='subject_id', how='inner'))


df = pd.merge(df_a, df_b, on='subject_id', how='outer')
df = pd.merge(df, df_n, on='subject_id', how='outer')
print(df)


df = pd.merge(df_a, df_b, on='subject_id', how='inner')
df = pd.merge(df, df_n, on='subject_id', how='inner')
print(df)