# with open("./requirements.txt", "r") as file:
#     contenuto = file.readlines()

# contenuto_pulito=[]
# for nome_lib in contenuto:
#     nome_lib_pul= nome_lib.strip("\n")
#     contenuto_pulito.append(nome_lib_pul)


# print(f"il contenuto del file è:\n{contenuto}\nIl tipo della variabile è: {type(contenuto)}")

# print(f"il contenuto del file è:\n{contenuto_pulito}\nIl tipo della variabile è: {type(contenuto)}")


import logging
import json
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

with open("./commedia.txt","r", encoding="utf-8") as file:
    testo_commedia =file.read()


testo_commedia=testo_commedia.replace("\n", " ")
testo_commedia=testo_commedia.split()
print({len(testo_commedia)})
def cleaning_parole(parola):
    return parola.replace(" ", "").replace(".","").replace(",","").replace("'","")

lista_pulita=[cleaning_parole(x) for x in testo_commedia]
count_delle_parole:dict={}
for parola in lista_pulita:
    if parola in count_delle_parole.keys():
        count_delle_parole[parola]+=1
    else:
        count_delle_parole[parola]=1

dizionario_ordinato=dict(sorted(count_delle_parole.items(), key=lambda item: item[1]))
# print(dizionario_ordinato)

logging.debug('info')


with open("risultati_count.json", "w", encoding="utf-8") as files:
    json.dump(dizionario_ordinato, files, indent=4)

with open("risultati_count.json","r") as file:
    json_caricato=json.load(file)
    logging.debug('Verifica')
    _, estensioneFile = os.path.splitext('risultati_count.json')
    print(estensioneFile)