import main_utils as mu
import pandas as pd
import random as rd

vowels = ('a','e','i','o','u')

words = (
    mu.charValid(input('Choose the 1° word: ')),
    mu.charValid(input('Choose the 2° word: ')),
    mu.charValid(input('Choose the 3° word: ')),
    mu.charValid(input('Choose the 4° word: ')),
    mu.charValid(input('Choose the 5° word: '))
)

print('\n')
for o in range(len(words)):
    a1 = list(words[o].lower())
    empty_list = list()
    for i in range(len(a1)):
        if a1[i] in vowels:
            empty_list.append(a1[i])
    print(f'{words[o]} -> contains {len(empty_list)} vowels = {empty_list}')

