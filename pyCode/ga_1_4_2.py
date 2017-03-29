# Practise loading and describing data

# 1
''' The url library does not work. Check it up'''

# 2 - Loading the housing file

names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
         "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]

data = []
with open('./datasets/housing.data', 'rU') as housing:
    rows = housing.readlines()
    # data.append(names)
    for row in rows:
        row = [float(x) for x in row.split()]
        data.append(row)
housing.close()

print(data[0:2])

d = {k: [row[i] for row in data] for i, k in enumerate(names)}
print(d.keys())

# 3
