#Python3 test code
#Roshan Lulu
#20 March 2017

import numpy as np
import random
''' 
#First part of exercise
print("This is working")
weight = float(input("How many pounds does your suitcase weigh? "))
if weight > 50:
    print("It is over 50 pounds, In fact it is",weight)
else:
    print("It is not over 50 pounds, In fact it is",weight)
'''
'''
#Second part of exercise
temperature = float(input('What is the temperature? '))
weather = raw_input('What is the weather? (rain or shine) ')

if temperature > 60:
    if weather == 'rain':
        print 'Bring an umbrella'
    else:
        print 'Wear a t-shirt'
else:
    if weather == 'rain':
        print 'Bring an umbrella and jacket'
    else:
        print 'Bring a jacket'
'''

'''
#Third part of exercise
for item in range(16):
    print (item)
'''
'''
animals = ['duck', 'rat', 'boar', 'slug', 'mammoth', 'gazelle']

print(filter(lambda item: item.upper(), animals))
'''

# Part 13 of exercise

# Load the dataset
with open('./coffee-preferences.csv', 'r') as f:
    lines = f.readlines()

# Iterate through the lines
for line in lines:
    line = line.replace("\n", "")
    #print(line)

header = lines[0]
data = lines[1::]

print (header.split(','))
print (data)

