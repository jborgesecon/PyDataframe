import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_wiki_table(url):
    response1 = requests.get(url)
    soup1 = BeautifulSoup(response1.content, 'html.parser')
    table1 = soup1.find('table', class_='wikitable')
    return pd.read_html(str(table1.prettify()))[0]

url = "https://en.wikipedia.org/wiki/2022%E2%80%9323_NBA_season"

table_data1 = get_wiki_table(url)

print(table_data1)








# url = 'https://www.espn.com/nba/standings/_/season/2022/group/league'
# 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

# response = requests.get(url)
# tables = pd.read_html(response.text)
# first_table = tables[0]
# print(first_table.head())

