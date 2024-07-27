import pandas as pd
from bs4 import BeautifulSoup
import requests
import random
import time 
import tqdm



def getsoup(url):
        """Obtiene el soup de una pagina web con requests y beautifulsoup"""
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        return soup

def soup2htmlSave(soup, filname="landing.html"):
    html = soup.prettify()
    # Guardar Html de la pagina de grupos
    with open(filname, "w", encoding="utf-8") as archivo:
        archivo.write(html) 

def get_make(url):
    make_list = []
    soup = getsoup(url)
    table = soup.find("table", class_="c-combo-list")
    if table == None:
        return make_list
    items = table.find_all('td', class_='c-combo-list__item-use--target')
    items = [item.text.split(' + ') for item in items] # separar los items con +
    items_all = [item for sublist in items for item in sublist] # unir todos los items en una lista
    items = set(items_all)
    make_list = list(items)    
    return make_list
     
def get_main():
    url = "https://littlealchemy2.gambledude.com/"     
    soup = getsoup(url)
    section = soup.find_all('section', class_='wrapper')[2]
    elements = section.find_all('li', class_='c-element-list__item')

    data  = []
    
    for element in tqdm.tqdm(elements):
        name = element.text
        url = element.find('a')['href']
        makes = get_make(url)
        data.append({'name': name,'url': url, 'makes': makes})
        # Esperar de 1 a 3 segundos para no saturar el servidor
        #time.sleep(random.randint(2, 5))
    return data


if __name__ == "__main__":        
    data = get_main()
    # Exportar como json sin pandas
    import json
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)



    




