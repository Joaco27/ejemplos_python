import csv
import json

def leerCSV():
    """Devuelve el archivo .csv"""
    arch = open('D:/Facultad/Seminario Python/ACTIVIDAD 1 TEORIA/twitchdata-update.csv', 'r', encoding='utf-8-sig')
    csvreader = csv.reader(arch, delimiter=',')
    return csvreader

def recorrer(pos, csvreader, ok):
    l1 = []
    l2 = []
    for linea in csvreader:
        if ok == True:
            if linea[10] == 'Spanish':
                l1.append(linea[0])
                l2.append(linea[pos])
        else:
            l1.append(linea[0])
            l2.append(linea[pos])
    lista = list(zip(l1,l2))
    lista = sorted(lista, key=lambda lista : lista[1], reverse=True)
    return lista

def cargarDicc(pos, palabra, lista):
    dicc = {}
    for i in range(pos):
        tupla = (lista[i][1],palabra)
        dicc[lista[i][0]] = tupla
    return dicc

def famosos():
    """Carga en un archivo json los 5 streamers mas famosos"""
    archivo = open("archivo.json","w")
    csvreader = leerCSV()
    encabezado = next(csvreader)
    #print(encabezado)
    lista = recorrer(5, csvreader, False)
    dicc = cargarDicc(5, 'seguidores', lista)
    archivo.write(json.dumps(dicc))
    

def vistos():
    """Carga en un archivo json los 7 streamers mas vistos (en minutos)"""
    archivo = open("archivo.json","w")
    csvreader = leerCSV()
    encabezado = next(csvreader)
    #print(encabezado)
    lista = recorrer(1, csvreader, False)
    dicc = cargarDicc(7, 'minutos', lista)
    archivo.write(json.dumps(dicc))

def hispanohablantes():
    """Carga en un archivo json los 3 streamers hispanohablantes mas famosos"""
    archivo = open("archivo.json","w")
    csvreader = leerCSV()
    encabezado = next(csvreader)
    #print(encabezado)
    lista = recorrer(5, csvreader, True)
    dicc = cargarDicc(3, 'seguidores', lista)
    archivo.write(json.dumps(dicc))
