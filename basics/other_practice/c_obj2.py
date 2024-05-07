from models import dataValid as dv

# # My Second Menu

# levels: Main -> Mundo -> Class -> Tasks:1
# I imagine: list, list, dict

# Definint Top Level

Main = {
    'Statistics': None,
    'Economics': None,
    'Machine Learning': None,
    'DashBoards': None
}

# Defining Second Level

statistics = {
    'Measures of Tendency': lambda: print('statistics OK'),
    'Measures of Dispersion': lambda: print('statistics OK'),
    'Probability': lambda: print('statistics OK')
}

economics = {
    'Econometrics': lambda: print('economics OK'),
    'Phillips Curve': lambda: print('economics OK'),
    'Hicks-Hansen': lambda: print('economics OK')
}

machineLearning = {
    'KNN': lambda: print('machineLearning OK'),
    'Random Forest': lambda: print('machineLearning OK'),
    'Naive Bayes': lambda: print('machineLearning OK')
}

dashboards = {
    'Django': lambda: print('dashboards OK'),
    'Pygame': lambda: print('dashboards OK'),
    'StreamLit': lambda: print('dashboards OK')
}

# ...Add other levels


# Unify the Main dictionary with all the sublevels:

Main['Statistics'] = statistics
Main['Economics'] = economics
Main['Machine Learning'] = machineLearning
Main['DashBoards'] = dashboards

# Create new dictionary for the lists for each level

level_lists1 = {
    'lvl zero': list(Main.keys())
}

level_lists2 = {}

for i, section in enumerate(Main.keys(), start= 1):
    slevel_list = list(Main[section].keys())
    level_lists2[f'lvl{i}'] = slevel_list

# for key, value in level_lists1.items():
#     print(f'{key} => {value}')

# for key, value in level_lists2.items():
#     print(f'{key} => {value}')


welcome = 'Welcome to the program!'
print('\n')
print(welcome.center(30, '='))

while True:
    print('\n')
    m_menu = 'main menu:'
    print(f'{m_menu:^30}')
    print('\n')

    for i in range(len(level_lists1['lvl zero'])):
        print(f'0{i + 1} - {level_lists1["lvl zero"][i]}')

    print('\n')

    nav1 = dv.intValid(input('Choose a task to navigate: '))
    print('\n')

    for i in range(len(level_lists2[f'lvl{nav1}'])):
        print(f'0{i + 1} - ', level_lists2[f'lvl{nav1}'][i])

    print('\n')

    nav2 = dv.intValid(input('Now choose a function to call: '))
    print('\n')

    Main[level_lists1['lvl zero'][nav1 - 1]][level_lists2[f'lvl{nav1}'][nav2 - 1]]()
    print('\n')

    print('The program is working fine so far...')