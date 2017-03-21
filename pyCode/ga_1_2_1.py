
# 1
student_names = []

for item in range(20):
    student_names.append('S'+str(item + 1))

# 3 and 4
print(student_names)
print(student_names[0])
print(student_names[len(student_names) - 1])

# 5
for index in range(0, 5):
    print(student_names[index])
# print(student_names[:5])

# 6
nineandten = student_names[8] + ' ' + student_names[9]
print(nineandten)

# 7 and 8
animals = ['duck', 'rat', 'boar', 'slug', 'mammoth', 'gazelle']
animals.append('kangaroo')
print ('Length of the list animals = ', len(animals))

# 9 and 10
lenanimal_fifth = len(animals[4])
lenanimal_second = len(animals[1])
print ('Length of 5th animal/2nd animal = ', (lenanimal_fifth)//lenanimal_second)
print ('Length of 5th animal/2nd animal = ', (lenanimal_fifth)/lenanimal_second)


#11
numbers = [0., 0.1, 1., 10., 100., 1000.]
print (animals + numbers)
#print animals.extend(numbers)


# 12
names = ['doug', 'billy', 'kiefer', 'kian', 'sam']
your_name = input("What is your name?")
name_index = names.index(your_name)
names[name_index] = 'roshan'
print(names)

#13
mix = [['billy', 'sam'], {'key':'value'}, 12.999, 12, 'flower', 'a', (1, 2, 3)]
#mix.sort() 
''' Does not work '''
print(mix)

#14
'''Does not work '''
#print(mix[0] > mix[1])

#15
print (mix.index('a'))

#16
print (mix.reverse())

#17
var = mix.pop()
print (var)

#18
binary = [0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1]
print(binary.count(0))

#19
zipcode = {
'sunset':94122,
'presidio':94129,
'soma':94105,
'marina':94123
}

#20
value = zipcode['soma']
print (value)

#21
zipcode_keys = zipcode.keys()
zipcode_values = zipcode.values()
print (zipcode_keys)

#22
zipcode_pairs = zipcode.items()
print (zipcode_pairs)

#23
zipcode['castro'] = 94114
print (zipcode)

#24
small = {'outer_richmond':94121, 'dogpatch':94107}
zipcode.update(small)
print (zipcode)

#25
sunset = zipcode.pop('sunset')
print (sunset)

#26
print('dogpatch' in zipcode)


