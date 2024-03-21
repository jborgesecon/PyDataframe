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