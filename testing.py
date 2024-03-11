import main_utils as mu
import pandas as pd
import random as rd

df = pd.read_csv('Standings.csv')
ranking = list(df['TEAM'])
a1 = ranking.index('NEW YORK KNICKS')

print('\nThe top 5 teams were:')
for i in range(0,5):
    print(f'{i+1}° - {ranking[i]}')

ranking.reverse()
print('\nThe bottom 5 were:')
o=0
for i in range(0,5):
    print(f'{len(ranking)-o}° - {ranking[i]}')
    o+=1
print('\nThe top 5 in alphabetical order is:\n')
ranking.sort()
i = 1
while i < 6:
    print(ranking[i])
    i+=1
print('\n')

print(f'The team "NEW YORK KNICKS" is in position: {a1}°\n')


=SE(
E(
$I2 <> "";
ANO($I2)<2020);
"ANTIGO";

SE(
E(
$G2 < $U$1;
 $I2 = "");
"ATIVO";

SE(
E(
MÊS($G2)>MÊS($U$1);
ANO($G2)>=ANO($U$1));
"NÃO CONTRATADO";

SE(
$I2<$U$1;
"DEMITIDO";

SE(
E(
MÊS($G2)=MÊS($U$1);
ANO($G2)=ANO($U$1);
MÊS($I2)=MÊS($U$1);
ANO($I2)=ANO($U$1));
"ADMITIDO E DEMITIDO";

SE(
E(
MÊS($I2) = MÊS($U$1);
ANO($I2) = ANO($U$1));
"DEMITIDO NO MÊS";

SE(
E(
MÊS($G2)=MÊS($U$1);
ANO($G2)=ANO($U$1);
$I2="");
"ADMITIDO NO MÊS";)))))))