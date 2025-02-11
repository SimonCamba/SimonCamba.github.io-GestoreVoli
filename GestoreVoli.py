import csv

nomeFile='Piano_voli_Aeroporto_di_Cagliari.csv'

def listaDliste(var):
    with open(var, 'r') as miocsv:
        testo=csv.reader(miocsv)
        foglio=[]
        for row in testo:
            foglio.append(row)
        return foglio
      
Voli_Cagliari=listaDliste(nomeFile)

with open("voli_operativi_GIOVEDI.csv", 'w') as miocsv:
    riga = csv.writer(miocsv, delimiter=";")
    for lista in Voli_Cagliari:
        if "GIOVEDI" in lista[18]:
            riga.writerow(lista)
