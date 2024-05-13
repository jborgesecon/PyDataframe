import pandas as pd


df_main = pd.read_csv('razao_jan.csv', sep=';', encoding='latin1', na_values=['NA', ''], decimal='.')
df_lanc = pd.read_csv('lanc2.csv', sep=';', encoding='latin1', na_values=['NA', ''], decimal='.')
df_mnth = pd.read_csv('to_row.csv', sep=';', encoding='latin1', na_values=['NA', ''], decimal='.')

campos = ('class')
df_mnth_col = df_mnth.melt(id_vars=campos, var_name='month', value_name='value')
# print(df_mnth_col.head(30))
print(df_mnth_col.info())

df_lanc_filled = df_lanc.fillna(method='ffill')
# print(df_lanc_filled.head(30))

n_count = (df_main.isnull().sum()/len(df_main))*100

filtered = df_main[df_main['idpartida'] == 2930353]
# print(filtered.head())
# print(len(df_main))
# print(n_count)
# print(df_main.head(5))


# Assuming 'df_months' is your DataFrame

# Select columns containing month data (excluding 'class')
data_cols = df_mnth.columns[1:]

# Reshape the DataFrame using 'set_index' and 'stack'
# df_transformed = df_mnth[['class']].set_index('class').stack().rename_axis(['month', 'value']).reset_index()
# print(df_transformed)
# Print the transformed DataFrame
# print(df_mnth.info())
