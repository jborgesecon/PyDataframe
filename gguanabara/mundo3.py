from models import dataValid as dv
import pandas as pd
import random as rd



def generic_print():
    print('ok')

# # ep 16

# e72
def number_names():
    nnames = (
        'Zero', 'One', 'Two', 'Three',
        'Four', 'Five', 'Six', 'Seven', 
        'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
        'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
        'Seventeen', 'Eighteen', 'Nineteen', 'Twenty'
    )
    while True:
        chosen_num = dv.intValid(input('Enter a number between 0 and 20: '))
        if 0 <= chosen_num <= 20:
            break
        else:
            print('Please enter a number between 0 and 20.')
    print(f'You chose number {nnames[chosen_num]}!')

# e73
def standings():
    df = pd.read_csv('datasets_copy/Standings.csv')
    
    dv.sepper('Top 5:', ' ')
    print('\n')
    top_5 = df['TEAM'].head(5).tolist()
    o = 1
    for i in top_5:
        print(f'{o}° - {i}')
        o += 1
    
    print('\n')
    dv.sepper('Last 4:', ' ')
    print('\n')
    last_4 = top_5 = df['TEAM'].tail(5).tolist()
    last_4 = reversed(last_4)
    o = len(df['TEAM']) + 4
    for i in last_4:
        print(f'{o - 4}° - {i}')
        o -= 1
    
    print('\n')
    dv.sepper('Alphabetically: ', ' ')
    print('\n')
    s_standings = sorted(df['TEAM'].tolist())
    print(s_standings)

    print('\n')
    dv.sepper('Choose your Team!', ' ')
    print('\n')
    standings2 = df['TEAM'].tolist()
    while True:
        usr_team = input('Desired Team: ').upper().strip()
        if usr_team in standings2:
            break
        else:
            print('Type an available team!')
    position = standings2.index(usr_team)
    print(f'The {usr_team} are in position {position + 1}°')

    
# e74
def fv_randNums():
    m_tp = (
        rd.randint(0,9),
        rd.randint(0,9),
        rd.randint(0,9),
        rd.randint(0,9),
        rd.randint(0,9)
    )
    # m_tp.pop()
    print(m_tp)
    print(f'The highest number is {max(m_tp)}')
    print(f'The lowest number is {min(m_tp)}')


# e75
def tuple_values():
    m_tp = (
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: '))
    )
    print(f'The number 9 appeared {m_tp.count(9)} times.')
    if 3 in m_tp:
        print(f'The number 3 appeared in position {m_tp.index(3) + 1}')
    else:
        print('The number 3 did not appear.')
    print('The even numbers are: ', end='')
    for i in m_tp:
        if i % 2 == 0:
            print(i, end=' ')
    print('\n')

# e76
def shopping_list():
    m_list = (
        'Pencil', 1.75,
        'Eraser', 2.00,
        'Notebook', 15.90,
        'Pencilcase', 25.00,
        'Ruler', 4.20,
        'Compass', 9.99,
        'Backpack', 120.32,
        'Pen', 22.30,
        'Book', 34.90
    )
    print(38* '-')
    msg = 'SHOPPING LIST'
    print(f'{msg:^38}')
    print(38* '-')
    print('\n')
    for i in range(0, len(m_list), 2):
        print(f'{m_list[i]:.<30}$ {m_list[i + 1]:>7.2f}')
    print(38* '-')
    print('\n')

# e77
def tuple_vowels():
    m_tp = (
        "application", 
        "revolutionary", 
        "consideration", 
        "misunderstanding", 
        "organization", 
        "preoccupation", 
        "interpretation", 
        "exaggeration", 
        "circumstances", 
        "representation", 
        "collaboration", 
        "multiplication"
    )
    vowels = ('a', 'e', 'i', 'o', 'u')
    print('\n')

    for i in range(len(m_tp)):
        print(f'In the word {m_tp[i].upper()} the vowels are: ', end='')
        for o in m_tp[i]:
            if o in vowels:
                print(f'{o} ', end='')
        print('')

# # Episode 17

# e78
def list_num_order():
    l1 = [
        dv.intValid(input('Choose a number: ')),
        dv.intValid(input('Choose a number: ')),
        dv.intValid(input('Choose a number: ')),
        dv.intValid(input('Choose a number: ')),
        dv.intValid(input('Choose a number: '))        
    ]

    l2 = l1[:]
    l2 = sorted(l2)

    mx = max(l1)
    mn = min(l1)
    tot_mx = l1.count(mx)
    tot_mn = l1.count(mn)

    print('\n')
    print(f'The highest number was {mx}')
    print(f'The lowest number was {mn}')

    if tot_mx == 1:
        cod = l1.index(mx)
        print(f'The number {mx} is in position: {cod + 1}° ')
    else:
        positions = [index for index, value in enumerate(l1, start= 1) if value == mx]
        print(f'The number {mx} is at positions: ', end='')
        for i in range(len(positions)):
            print(f'{positions[i]}... ', end='')
        print('')


    if tot_mn == 1:
        cod = l1.index(mn)
        print(f'The number {mn} is in position: {cod + 1}° ')
    else:
        positions2 = [index for index, value in enumerate(l1, start= 1) if value == mn]
        print(f'The number {mn} is at positions: ', end='')
        for i in range(len(positions2)):
            print(f'{positions2[i]}... ', end='')
        print('')

    
    print('\n')

# e79
def list_get_nums():
    msg = 'y'
    org_list = list()
    while msg == 'y':
        num = dv.intValid(input('Chose a number: '))
        if not org_list:
            org_list.append(num)
        else:
            inserted = False
            for index in range(len(org_list)):
                if num in org_list:
                    print(f"{num} is already on the list and won't be added")
                    inserted = True
                    break
                elif num < org_list[index]:
                    org_list.insert(index, num)
                    break
            if not inserted:
                org_list.append(num)

        msg = dv.yn_valid(input('Wanna choose another number? [y/n]: '))
    
    print('\n')
    print(org_list)
    print('\n')
    return

def zero_to_hundred_sorted():
    organized_list = list()
    while len(organized_list) < 101:
        number = rd.randint(0, 100)
        if not organized_list:
            organized_list.append(number)
            print('\n')
            print(organized_list)
        else:
            inserted = False
            for index in range(len(organized_list)):
                if number in organized_list:
                    print(f"{number} is already in list, won't be added")
                    inserted = True
                    break
                elif organized_list[index] > number:
                    organized_list.insert(index, number)
                    print('\n')
                    print(organized_list)
                    inserted = True
            if not inserted:
                organized_list.append(number)
                print('\n')
                print(organized_list)
    print('\n')
    print(organized_list)
