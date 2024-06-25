import pandas as pd
import os


# print("current working directory: ", os.getcwd())

csv = 'datasets_copy/Standings.csv'
df = pd.read_csv(csv)
print(df.head())