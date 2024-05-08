from models import dataValid as dv
import pandas as pd
import random as rd

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
