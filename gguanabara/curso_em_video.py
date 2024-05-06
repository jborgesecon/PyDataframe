from models import dataValid as dv
from mundo3 import *

dv.header('Welcome to the program!')
dv.sepper('Bellow are the options:', ' ')
print('\n')

# main -> modules -> eps -> tasks
# list -> list -> dict -> function

ep_16 = {
    'Number Names (e72)': number_names,
    'Standings (e72)': standings,
    'Five Random Numbers': fv_randNums,
    'fourth task': ''
}

ep_list = list(ep_16.keys())

while True:
    for i in range(len(ep_list)):
        print(f'0{i + 1} -> {ep_list[i]}')
    print('\n')

    while True:
        try:
            choice = int(input('Enter the desired task: '))
            if 1 <= choice <= len(ep_list):
                break
            else:
                print('Type a number within the range.')
        except ValueError:
            print('Type a valid answer.')
    
    choice -= 1
    while True:
        print(ep_list[choice])
        chosen = ep_16[ep_list[choice]]
        print('\n')
        if callable(chosen):
            chosen()
        else:
            print(chosen)
        print('\n')
        nav1 = dv.yn_valid(input('Want to try this task again? [y/n]: '))
        if nav1 == 'n':
            break

    
    
    print('\n')
    nav1 = dv.yn_valid(input('Would you like to keep going? [y/n]: ').lower().strip())

    if nav1 == 'n':
        break
    print('\n')


print('Thanks for trying this code!')