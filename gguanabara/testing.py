import pandas as pd
import os
import random as rd
import dataValid as dv
import time


m_list = list()
par = ['(', ')']
obj = input('Type any expression containing parentheses: ')
for i in range(len(obj)):
    if obj[i] in par:
        m_list.append(obj[i])
print('Extracting parentheses:', '\n', m_list)
openning = list()
closing = list()

for i in range(len(m_list)):
    if m_list[i] == par[0]:
        openning.append(m_list[i])
    elif m_list[i] == par[1]:
        closing.append(m_list[i])
    else:
        print('Error!')

print('Opening Parentheses:', openning)
print('Closing Parentheses:', closing)
print('\n')
print('Checking if balanced...')

for i in range(6):
    print('.')
    time.sleep(1)


if len(openning) != len(closing):
    print('Unbalanced!')

((())()(()(()))(()(()))(()()(())()()())()())))(()()()))(())(