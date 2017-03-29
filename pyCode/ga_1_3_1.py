# list-comprehensions-practice
import numpy as np
import pytest
import string

# 1
strings = ['black', 'Yellow', 'ReD', 'GreeN', 'BLUe']

for index in range(0, len(strings)):
    strings[index] = strings[index].upper()
print(strings)

strings = ['black', 'Yellow', 'ReD', 'GreeN', 'BLUe']

strings = [item.upper() for item in strings]
print(strings)

# 2
numbers = range(0, 20)

evennumbers = [x for x in numbers if x % 2 == 0 in numbers]
print(evennumbers)

# 3
alphabet = list(string.ascii_lowercase)
vowels = list('aeiou')

characters = ['a', 'f', None, 'k', 'l', '1', 12, 'e', 'e', -1, 'i', 'b', 'p']

new_char = ['?' if char not in alphabet
            else 'v' if char in vowels
            else 'c' for char in characters]
print(converted)

# 4
number_sets = [[1, 50, -40, 20, 90], [1004, 1002, 101, -90, 40, 34],
               [-1, -2, 34, 55, 77, 109]]

mean_set = [np.mean(newset) for newset in number_sets]
print(mean_set)

# ListandDictionaryComprehensionss
# 1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lc_numbers = [n + 1 for n in numbers]


# 2
n = [1, 2, 7, 21, 3, 1, 62, 3, 34, 12, 73, 44, 12, 11, 9]
meanofn = np.mean(n)
lc_n = [1 if x > meanofn else 0 for x in n]

# 3


new = []