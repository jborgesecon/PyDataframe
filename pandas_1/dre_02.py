import pandas as pd

df_mnth = pd.read_csv('to_row.csv', sep=';', encoding='latin1', na_values=['NA', ''], decimal='.')

print(df_mnth.melt(10))