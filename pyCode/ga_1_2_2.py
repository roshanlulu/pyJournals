# Practise python functions

import pytest
import string

#1
def area_square(side):
    return (side ** 2)

#2
def area_triangle(height, width):
    return (height * width)/2

#3
def convert(text):
    print (tuple(text))
    print (len(text))

#4
def math(a, b):
    a = int(a)
    b = int(b)
    return tuple(a + b, a - b, a * b)

#5
def modify(lst):
    return tuple(lst.reverse(), [lst[index] for index in range(0, len(list) and index % 2 != 0)])

#Challenge
def challenge(word):
    alphabets = list(string.ascii_lowercase)
    word = word.lower()
    score = 0
    for item in word:
        score += alphabets.index(item) + 1
    return score



def test_area_square():
    assert area_square(5) == 25