#'print()' and working with strings

name = 'Joao Borges'
age = 20

print('\n')
print(name.upper()) 
print(name.lower())
print(f"My name is {name}, and I'm {20}")
print('\n', 15*'=-','\n')
print(f'{name:^30}')
print('\n', 15*'=-','\n')

print("Here are the programing languages I'm working on -> ", end=' ')
print('Python3, ', end=' ')
print('SQL, ', end=' ')
print('R (statistics), ', end=' ')
print('M (PowerQuery) ', end=' ')
print('\n')

a1 = 'TEXT'
print(a1.ljust(20,'.'))
print(a1.center(20,'.'))
print(a1.rjust(20,'.'))
print('\n')
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

# print(numbers_3.index(65)) #error because not in the tuple
print(numbers_3.index(9)) #the first time it appears
print(numbers_3.count(9))




#Lists


#Dictionaries


#DataFrame