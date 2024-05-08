from gguanabara.mundo3 import *
import pandas as pd

fv_randNums()

df = pd.read_csv('datasets_copy/Standings.csv')
print(df.head(5))