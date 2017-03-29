
import pandas as pd
import numpy as np


    # # 1
    # test_data = dict(
    #     A = np.random.randint(3),
    #     B = 1,
    #     C = 'foo',
    #     D = pd.Timestamp('20010102'),
    #     E = pd.Series([1.0]*3).astype('float32'),
    #     F = False,
    #     G = pd.Series([1]*3,dtype='int8')
    # )
    #
    # print(test_data)
    #
    # dft = pd.DataFrame(test_data)
    # print(dft)
    #
    # # 2
    # print(dft.dtypes)
    #
    # # 3
    # print(pd.Series([1, 2, 3, 4, 5, 6.]))
    #
    # # 4
    # print(pd.Series([1, 2, 3, 'foo']))
    #
    # # 5
    # print(dft.get_dtype_counts().astype(list))
    #
    #
    # lst = [1, 3, 9, .33, False, '03-20-1978', np.arange(22)]
    # print(lst)
    # dft = pd.DataFrame(lst)
    # # print(dft.dtypes)
    # #
    # # print(lst.apply())
    #
    # # 6 # Create some more test data
    # df = pd.DataFrame(np.random.randn(5, 4), columns=['a', 'b', 'c', 'd'])
    # print(df)
    #
    # # 7
    # # square root ALL CELLS (NaN == Not a Number)
    # print(df.apply(np.sqrt))
    #
    # # 8
    # print(df.apply(np.mean, axis=0))
    #
    # # 9
    # print(df.apply(np.mean, axis=1))
    #
    # # 10
    # data = np.random.randint(0, 7, size = 50)
    # print(data)
    #
    # # 11
    # s = pd.Series(data)
    # print(s.head())
    #
    # print(pd.value_counts(s))



    # Independent practise

    # sales_data = pd.read_csv('./datasets/sales.csv')
    # sales_dframe = pd.DataFrame(sales_data)

sales_dframe = pd.DataFrame.from_csv('/Users/roshanlulu/Documents/GA/pyJournals/pyCode/datasets/sales.csv')

print(sales_dframe.head(5))
sales_dtypes = sales_dframe.dtypes
print(sales_dtypes)
print((sales_dframe.apply(lambda x: x + 1)).head(5))

#
# dft = pd.DataFrame(dict(A = np.random.rand(3),
#                         B = 1,
#                         C = 'foo',
#                         D = pd.Timestamp('20010102'),
#                         E = pd.Series([1.0]*3).astype('float32'),
#                                 F = False,
#                                 G = pd.Series([1]*3,dtype='int8')))
#
# print(dft)
# print(dft.dtypes)
# print(pd.Series([1, 2, 3, 4, 5, 6.]))
# print(pd.Series([1, 2, 3, 6., 'foo']))
# print(dft.get_dtype_counts())
# df = pd.DataFrame(np.random.randn(5, 4), columns=['a', 'b', 'c', 'd'])
# print(df)
# print(df.apply(np.sqrt))
# # Mean of columns; axis = 0; rows; axis = 1
# print(df.apply(np.mean, axis=0))
# print(df.apply(np.mean, axis=1))
# data = np.random.randint(0, 7, size = 50)
# print(data)
# s = pd.Series(data)
# pd.value_counts(s)