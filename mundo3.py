import main_utils as mu

#This will be the new 'mundo_3.py'

#Creating compound object for navigation
general = {
    'Episode 16 (Tuples)':{
        'Number Name (e72)': mu.numberName,
        'Go Back': 'break'
    },
    'Episode 17': {
        'List of Lists': 'Not yet done',
        'Go Back': 'break'
    }
    }

#Creating a list for the episodes
eps = list(general.keys())

#Function Main Loop
while True:
    mu.print_menu(eps, 'MAIN')

    #Answer Validation (I need help creating a def for it)
    while True:
        nav = mu.intvalid(input('Choose your Episode: '))
        if nav > 0 and nav <= len(eps):
            break
        else:
            print('\nType a value within the range')

    while True:
        mu.print_menu(general[eps[nav - 1]], eps[nav - 1])
        functions = list(general[eps[nav - 1]].keys())

        #Answer Validation again
        while True:
            nav2 = mu.intvalid(input('Choose the desired function: '))
            if nav2 > 0 and nav2 <= len(functions):
                break
            else:
                print('\nType a value within the range')

        value = general[eps[nav - 1]][functions[nav2 - 1]]
        if value == 'break':
            break
        while True:
            if callable(value):
                value()
            else:
                print(value)
            if not mu.tryAgain():
                break