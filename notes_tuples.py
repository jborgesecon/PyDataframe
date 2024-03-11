#Tuples

tuples1 = (
    'tuples',
    'are',
    'immutable',
    'compound',
    'objects',
    'in',
    'python'
)

for i in range(len(tuples1)):
    print(tuples1[i].capitalize(), end=' ')
print('\n')

numbers_1 = (
    2,
    4, 
    11,
    9,
    0,
    23
)

numbers_2 = (
    1,
    72,
    82,
    14,
    9,
    4,
    61
)

print(numbers_1)
print(numbers_2)
print(numbers_1 + numbers_2)
print(numbers_2 + numbers_1)

numbers_3 = numbers_1 + numbers_2
print(sorted(numbers_3))
print((sorted(numbers_3)).reverse()) #returns 'None'
print(reversed(numbers_3)) #Investigate
print('\n')

#slicing method
sub_tuple1 = numbers_3[0:6]

sub_tuple2 = numbers_3[6:13]
print(numbers_3)
print(sub_tuple1)
print(numbers_1)
print(sub_tuple2)
print(numbers_2)

if sub_tuple1 == numbers_1 and sub_tuple2 == numbers_2:
    print('OK')
else:
    print('False')

print('\n')

# print(numbers_3.index(65)) #error because not in the tuple
print(numbers_3.index(9)) #the first time it appears
print(numbers_3.count(9))

