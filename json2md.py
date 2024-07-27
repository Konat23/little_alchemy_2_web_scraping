import json
import time

# cargar tiers
import pickle
with open('tiers.pkl', 'rb') as f:
    tiers = pickle.load(f)

def reordenar(data):
    # Poner primero las que no se hacen con nada
    data = sorted(data, key=lambda x: tier_order(x['name']))
    return data

def tier_order(name):
    tier_dict = {'start':0,
            'special':1,             
            'tier1':2,
            'tier2':3,
            'tier3':4,
            'tier4':5,
            'tier5':6,
            'tier6':7,
            'tier7':8,
            'tier8':9,
            'tier9':10,
            'tier10':11,
            'tier11':12,
            'tier12':13,
            'tier13':14,
            'tier14':15,
            'tier15':16
            }
    if name in tiers:
        return tier_dict[tiers[name]]
    else:
        return 17
    

with open('data.json', 'r') as f:
    data = json.load(f)

with open("basics.csv", 'r') as f:
    basics = f.read().split('\n')


data = reordenar(data)

for i, item in enumerate(data):
    time.sleep(1)
    #Crea archivo markdown con la informacion de cada elemento
    with open(f"Alchemy_2/items/{item['name']}.md", "w", encoding="utf-8") as archivo:
        print("-"*50)
        print(i, item['name'])
                
        archivo.write("## Makes\n")
        for make in item['makes']:
            archivo.write(f"- [[{make}]]\n")

        # Si el nombre esta en basics
        if item['name'] in basics:
            archivo.write(f"\n#Basic\n")
        
        # Si makes esta vacio poner etiqueta de final
        if len(item['makes']) == 0:
            archivo.write(f"\n#Final\n")
        archivo.write("\n")

        # Escritura de los tiers
        if item['name'] in tiers:
            archivo.write(f"#{tiers[item['name']]} \n")
        else:
            archivo.write(f"#Myths_and_Monsters\n")
    
    
        
    