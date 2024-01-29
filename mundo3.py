import main_utils as mu

#This will be the new 'mundo_3.py'

#Creating compound object for navigation
general = {
    'Episode 16 (Tuples)':{
        'Number Name (e72)': mu.numberName,
        'Basketball Ranking (e73)': mu.Standings,
        'Five Random Numbers (e74)':mu.fiveRandNum,
        'Input Five Values (e75)': mu.inputFiveValues,
        'Market Catalog (e76)': mu.groceriesCatalog,
        'Finding Vowels (e77)': mu.findVowels,
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
    mu.print_menu('MAIN', eps)

    #Answer Validation (I need help creating a def for it)
    nav = mu.rangevalid(eps)

    while True:
        mu.print_menu(eps[nav - 1], general[eps[nav - 1]])
        functions = list(general[eps[nav - 1]].keys())

        nav2 = mu.rangevalid(general[eps[nav - 1]])
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

