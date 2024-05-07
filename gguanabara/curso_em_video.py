from models import dataValid as dv
import menu_gguanabara as mg

dv.header('Welcome to the Program!')

while True:
    dv.sepper('MAIN MENU', '.')
    print('\n')

    for i in range(len(mg.dict_n1['lvl zero'])):
        print(f'0{i + 1} -> {mg.dict_n1["lvl zero"][i]}')

    print('\n')
    nav1 = dv.intValid(input('Choose the desired class: '))
    dv.sepper('EPISODES', '.')
    print('\n')
    for i in range(len(mg.dict_n2[f'lvl{nav1}'])):
        print(f'{i + 1} -> ', mg.dict_n2[f'lvl{nav1}'][i])
    
    print('\n')
    nav2 = dv.intValid(input('Choose the desired Episode: '))
    dv.sepper('FUNCTION', '.')
    print('\n')