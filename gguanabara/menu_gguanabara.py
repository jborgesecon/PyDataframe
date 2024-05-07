from models import dataValid as dv
from mundo3 import *


# Defining main menu:
Main = {
    'Mundo 1': None,
    'Mundo 2': None,
    'Mundo 3': None
}

# Defining Sublevels:
mundo_1 = {
    'Episode 1': None,
    'Episode 2': None,
    'Episode 3': None,
    'Episode 4': None,
    'Episode 5': None,
    'Episode 6': None,
    'Episode 7': None,
    'Episode 8': None,
    'Episode 9': None,
    'Episode 10': None,
    'Episode 11': None
}

mundo_2 = {
    'Episode 12': None,
    'Episode 13': None,
    'Episode 14': None,
    'Episode 15': None,
}

mundo_3 = {
    'Episode 16': None,
    'Episode 17': None,
    'Episode 18': None,
    'Episode 19': None,
    'Episode 20': None,
    'Episode 21': None,
    'Episode 22': None,
    'Episode 23': None
}


# Defining Episodes:
ep_1 = {
    'Number Names (e1)': number_names,
    'Standings (e2)': standings,
    'Five Random Numbers (e3)': fv_randNums
}

ep_2 = {
    'Number Names (e4)': number_names,
    'Standings (e5)': standings,
    'Five Random Numbers (e6)': fv_randNums
}

ep_3 = {
    'Number Names (e7)': number_names,
    'Standings (e8)': standings,
    'Five Random Numbers (e9)': fv_randNums
}

ep_4 = {
    'Number Names (e10)': number_names,
    'Standings (e11)': standings,
    'Five Random Numbers (e12)': fv_randNums
}

ep_5 = {
    'Number Names (e13)': number_names,
    'Standings (e14)': standings,
    'Five Random Numbers (e15)': fv_randNums
}

ep_6 = {
    'Number Names (e16)': number_names,
    'Standings (e17)': standings,
    'Five Random Numbers (e18)': fv_randNums
}

ep_7 = {
    'Number Names (e19)': number_names,
    'Standings (e20)': standings,
    'Five Random Numbers (e21)': fv_randNums
}

ep_8 = {
    'Number Names (e22)': number_names,
    'Standings (e23)': standings,
    'Five Random Numbers (e24)': fv_randNums
}

ep_9 = {
    'Number Names (e25)': number_names,
    'Standings (e26)': standings,
    'Five Random Numbers (e27)': fv_randNums
}

ep_10 = {
    'Number Names (e28)': number_names,
    'Standings (e29)': standings,
    'Five Random Numbers (e30)': fv_randNums
}

ep_11 = {
    'Number Names (e31)': number_names,
    'Standings (e32)': standings,
    'Five Random Numbers (e33)': fv_randNums
}

ep_12 = {
    'Number Names (e34)': number_names,
    'Standings (e35)': standings,
    'Five Random Numbers (e36)': fv_randNums
}

ep_13 = {
    'Number Names (e37)': number_names,
    'Standings (e38)': standings,
    'Five Random Numbers (e39)': fv_randNums
}

ep_14 = {
    'Number Names (e40)': number_names,
    'Standings (e41)': standings,
    'Five Random Numbers (e42)': fv_randNums
}

ep_15 = {
    'Number Names (e43)': number_names,
    'Standings (e44)': standings,
    'Five Random Numbers (e45)': fv_randNums
}

ep_16 = {
    'Number Names (e72)': number_names,
    'Standings (e73)': standings,
    'Five Random Numbers (e74)': fv_randNums
}

ep_17 = {
    'Number Names (e46)': number_names,
    'Standings (e47)': standings,
    'Five Random Numbers (e48)': fv_randNums
}

ep_18 = {
    'Number Names (e49)': number_names,
    'Standings (e50)': standings,
    'Five Random Numbers (e51)': fv_randNums
}

ep_19 = {
    'Number Names (e52)': number_names,
    'Standings (e53)': standings,
    'Five Random Numbers (e54)': fv_randNums
}

ep_20 = {
    'Number Names (e55)': number_names,
    'Standings (e56)': standings,
    'Five Random Numbers (e57)': fv_randNums
}

ep_21 = {
    'Number Names (e58)': number_names,
    'Standings (e59)': standings,
    'Five Random Numbers (e60)': fv_randNums
}

ep_22 = {
    'Number Names (e61)': number_names,
    'Standings (e62)': standings,
    'Five Random Numbers (e63)': fv_randNums
}

ep_23 = {
    'Number Names (e64)': number_names,
    'Standings (e65)': standings,
    'Five Random Numbers (e66)': fv_randNums
}

# Unify all objects:
mundo_1['Episode 1'] = ep_1
mundo_1['Episode 2'] = ep_2
mundo_1['Episode 3'] = ep_3
mundo_1['Episode 4'] = ep_4
mundo_1['Episode 5'] = ep_5
mundo_1['Episode 6'] = ep_6
mundo_1['Episode 7'] = ep_7
mundo_1['Episode 8'] = ep_8
mundo_1['Episode 9'] = ep_9
mundo_1['Episode 10'] = ep_10
mundo_1['Episode 11'] = ep_11

mundo_2['Episode 12'] = ep_12
mundo_2['Episode 13'] = ep_13
mundo_2['Episode 14'] = ep_14
mundo_2['Episode 15'] = ep_15

mundo_3['Episode 16'] = ep_16
mundo_3['Episode 17'] = ep_17
mundo_3['Episode 18'] = ep_18
mundo_3['Episode 19'] = ep_19
mundo_3['Episode 20'] = ep_20
mundo_3['Episode 21'] = ep_21
mundo_3['Episode 22'] = ep_22
mundo_3['Episode 23'] = ep_23

Main['Mundo 1'] = mundo_1
Main['Mundo 2'] = mundo_2
Main['Mundo 3'] = mundo_3

# Create dictionaries for list Navigation:
dict_n1 = {
    'lvl zero': list(Main.keys())
}

dict_n2 = {}
dict_n3 = {}

o = 1
for i, section in enumerate(Main.keys(), start= 1):     
    dict_n2[f'lvl{i}'] = list(Main[section].keys())
    for section2 in Main[section].keys():
        dict_n3[f'lvl{o}'] = list(Main[section][section2].keys())
        o += 1

# Main['Mundo 1']['Episode 1']['Number Names (e1)']()