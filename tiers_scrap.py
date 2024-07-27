import pandas as pd
from bs4 import BeautifulSoup
import requests

from main import getsoup, soup2htmlSave

url = "https://little-alchemy.fandom.com/wiki/Elements_(Little_Alchemy_2)"

soup = getsoup(url)
div = soup.find('div', class_='mw-parser-output')
titles =div.find_all('h3')
tables =div.find_all('table', class_ = "list-table")
tier_dict = {'Starting elements[]': 'start',
            'Special element[]': 'special',             
            'Tier 1 elements[]': 'tier1',
            'Tier 2 elements[]': 'tier2',
            'Tier 3 elements[]': 'tier3',
            'Tier 4 elements[]': 'tier4',
            'Tier 5 elements[]': 'tier5',
            'Tier 6 elements[]': 'tier6',
            'Tier 7 elements[]': 'tier7',
            'Tier 8 elements[]': 'tier8',
            'Tier 9 elements[]': 'tier9',
            'Tier 10 elements[]': 'tier10',
            'Tier 11 elements[]': 'tier11',
            'Tier 12 elements[]': 'tier12',
            'Tier 13 elements[]': 'tier13',
            'Tier 14 elements[]': 'tier14',
            'Tier 15 elements[]': 'tier15',}
mydict = {
          }

for title, table in zip(titles, tables):         
    rows = table.find_all('tr')
    for row in rows[1:]: # saltar el header        
        element = row.find('td').find_all('a')[1].text  
        print(element)
        # limpiar el texto
        element = element.strip()
        element = element.replace('\n', '')
        #minusculas
        element = element.lower()
        mydict[element] = tier_dict[title.text]

print(mydict)
# Guardar diccionario en un archivo pickle
import pickle

with open('tiers.pkl', 'wb') as f:
    pickle.dump(mydict, f)

