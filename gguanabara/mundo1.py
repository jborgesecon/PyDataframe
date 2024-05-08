import mundo3 as md
from menu_gguanabara import *
import datasets_copy as dc
import pandas as pd

item_name = 'Standings.csv'

path = '../datasets_copy'

if item_name in path:
    df = pd.read_csv('..datasets_copy/Stangings')
    print(df.head(5))
else:
    print('error')