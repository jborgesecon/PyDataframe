#this file will contain the main Functions I will call on all the other .py documents

import random as rd
import unicodedata
import pandas as pd

error = ('type a valid answer: ')
yes_or_no = ('type "y" for YES and "n" for NO: ')
n_or_p = 'type "n" for NEXT and "p" for PREVIOUS: '
range1 = '\nType a value within the range!\n'
consonants = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
vowels = ('a','e','i','o','u')

#Input Validation

def strvalid(text):
    while True:
        try:
            m1 = str(text).strip()
            break
        except ValueError:
            text = input(error)
    return m1
        
def intvalid(text):
    while True:
        try:
            m2 = int(text)
            break
        except ValueError:
            text = input(error)
    return m2

def positive_intvalid(text):
    while True:
        try:
            m2 = int(text)
            if m2 >= 0:
                break
            else:
                text = input(error)
        except ValueError:
            text = input(error)
    return m2

def floatvalid(text):
    while True:
        try:
            m2 = float(text)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            text = input(error)
    return m2

def isprime(text):
    t01 = 0
    for i in range(1, text+1):
        if text % i == 0:
            t01 += 1
    # if t01 > 2:
    #     m03 = ('FALSE')
    # elif t01 == 2:
    #     m03 = ('TRUE')
    # else:
    #     m03 = t01
    
    # m03 = t01 > 2 ? ('FALSE') : t01 == 2 ? ('TRUE') : t01

    m03 = False if t01 > 2  else True if t01 == 2 else t01
    
    return m03

def iseven(text):
    m8 = text % 2
    if m8 == 0 and text != 0:
        m81 = True
    else:
        m81 =False
    return m81

def ynvalid(text):
    while True:
        m04 = text.lower().strip()
        if m04 == 'y' or m04 == 'n':
            break
        else:
            text = input(yes_or_no)
    return m04

def npvalid(text):
    while True:
        m04 = text.lower().strip()
        if m04 == 'n' or m04 == 'p':
            break
        else:
            text = input(n_or_p)
    return m04

def rangevalid(eps):
    while True:
        nav = intvalid(input('Choose your Episode: '))
        if nav > 0 and nav <= len(eps):
            break
        else:
            print(range1)
    return nav

def tryAgain():
    m1 = ynvalid(input('Would you like to try again? [y/n]: '))
    if m1 == 'y':
        return True
    else:
        return False

def charValid(text):
    m1 = text
    while True:
        ll1 = list(m1)
        for i in range(len(ll1)):
            if ll1[i].lower() in consonants or ll1[i].lower() in vowels:
                m2 = True
            else:
                m2 = False
                break
        if not m2:
            print('\nOnly text, no special characters allowed!\n')
            m1 = input('Type the new value: ')
        else:
            break
    return m1

#Special defs

def print_menu(index, options):
    a1 = 'MENU: '
    print('\n', 30*'-')
    print(f'{(a1 + index):^30}')
    print(30*'-','\n')

    for i, option in enumerate(options, start=1):
        print(f'[{i}] - ', option)

    print('\n', 30*'-')
    return

def s_triangle():
    while True:
        t01 = []
        for i in range(0,3):
            b25 = rd.randint(1,100)
            t01.append(b25)
        t01.sort()
        a10 = t01[0] + t01[1]
        a11 = t01[2]
        if a10 > a11:
            break
    return t01

def normalize_text():
    
    #normalize the textto NFKD format
    text = unicodedata.normalize("NFKD", text)
    #encode using only ascii characters
    text = text.encode('ascii', 'ignore')
    #decode the textback to string, in the desired standard, in this case 'utf-8'
    text = text.decode('utf-8')
    #transform all characters in uppercase
    text = text.upper()

    return text

def specialint(text):
    while True:
        try:
            m2 = int(text)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            if text.strip().isalpha():
                m2 = npvalid(text)
                break
            else:
                text = input(error)
    return m2

#Mundo 3

#Tuples
def numberName():
    tp1 = (
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten'
    )

    while True:
        number = positive_intvalid(input('\nType a number between 0 and 10: '))
        if number not in range(len(tp1)):
            print(range1)
        else:
            break
    
    print(f'\nYour number was {tp1[number]}!\n')
    return

def Standings():
    df = pd.read_csv('Standings.csv')
    ranking = list(df['TEAM'])
    a1 = ranking.index('NEW YORK KNICKS')

    print('\nThe top 5 teams were:')
    for i in range(0,5):
        print(f'{i+1}° - {ranking[i]}')

    ranking.reverse()
    print('\nThe bottom 5 were:')
    o=0
    for i in range(0,5):
        print(f'{len(ranking)-o}° - {ranking[i]}')
        o+=1
    print('\nThe top 5 in alphabetical order is:\n')
    ranking.sort()
    i = 1
    while i < 6:
        print(ranking[i])
        i+=1
    print('\n')

    print(f'The team "NEW YORK KNICKS" is in position: {a1}°\n')

def fiveRandNum():
    tp1 = (
        rd.randint(0,100),
        rd.randint(0,100),
        rd.randint(0,100),
        rd.randint(0,100),
        rd.randint(0,100),
        )

    print(f'Your values were: ', end=' ')
    for i in range(len(tp1)):
        print(tp1[i], end=' ')
    print('\n')
    print(f'The highest value was {sorted(tp1)[-1]} and the lowest value was {sorted(tp1)[0]}\n')
    return

def inputFiveValues():
    print('\n')
    tp1 = (
        intvalid(input('Type the 1° Value: ')),
        intvalid(input('Type the 2° Value: ')),
        intvalid(input('Type the 3° Value: ')),
        intvalid(input('Type the 4° Value: ')),
        intvalid(input('Type the 5° Value: '))
    )
    print(f'\nThe value 9 appered {tp1.count(9)} times')
    if 3 in tp1:
        print(f'\nThe first value 3 is in position {tp1.index(3)+1}°')
    else:
        print('\nThe value "3" was not added')
    
    evens = list()
    for i in range(len(tp1)):
        if iseven(tp1[i]):
            evens.append(tp1[i])
    
    print(f'\nThe even numbers typed were: {evens}\n')
    return

def groceriesCatalog():
    catalog = (
        'bread', '1.75',
        'tomato', '2.00',
        'ham', '4.20',
        'cheese', '9.99',
        'meat', '15.90',
        'wine', '120.32',
        'spices', '25.00',
        'olive oil', '22.30',
        'ice cream', '34.90'
    )
    
    ctlg = "MARKET'S CATALOG"    
    print('\n', 30*'=')
    print(f'{ctlg:^30}')
    print(30*'=', '\n')

    for i in range(len(catalog)):
        a1 = i % 2
        if a1 == 0:
            print(f'{catalog[i].ljust(23, ".").title()}', '$', str(catalog[i+1]).rjust(7, ' '))
    print('\n', 30*'=', '\n')

    return

def findVowels():
    print(("""\nIn this code,\
 your are going to input 5 words\
 (no special characters allowed).\
 Then, it will return how many vowels were\
 in each word, and what were the vowels.\n"""))
    
    words = (
        charValid(input('Choose the 1° word: ')),
        charValid(input('Choose the 2° word: ')),
        charValid(input('Choose the 3° word: ')),
        charValid(input('Choose the 4° word: ')),
        charValid(input('Choose the 5° word: '))
    )

    print('\n')
    for o in range(len(words)):
        a1 = list(words[o].lower())
        empty_list = list()
        for i in range(len(a1)):
            if a1[i] in vowels:
                empty_list.append(a1[i])
        print(f'{words[o]} -> contains {len(empty_list)} vowels = {empty_list}')
    print('\n')
    return

#Lists (1)
def findTopBottom():
    ll1 = list()
    for i in range(5):
        ll1.append(intvalid(input(f'type the {i+1}° value: ')))

    o = ll1[0]
    for n in range(len(ll1)):
        if o > ll1[n]:
            break
        elif o == ll1[n]:
            break
        elif o < ll1[n]:
            break
