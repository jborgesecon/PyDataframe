import pandas as pd


csv = 'C:\\Users\\joao.santos\\Desktop\\Projects\\CODING\\Repository\\PyDataframe\\gguanabara\\Standings.csv'
df = pd.read_csv(csv)
print(df.head(5))