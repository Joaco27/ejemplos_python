import csv
import json

def leerCSV():
    """Devuelve el archivo .csv"""
    arch = open('D:/Facultad/Seminario Python/ACTIVIDAD 1 TEORIA/Datos históricos USD_ARS.csv', 'r', encoding='utf-8-sig')
    csvreader = csv.reader(arch, delimiter=',')
    return csvreader



def actual():
    """Carga en un archivo json el valor del dolar actual"""
    archivo = open("archivo.json","w")
    csvreader = leerCSV()
    encabezado = next(csvreader)
    #encabezado = [item.replace('"','').replace('','') for item in encabezado]
    #print(encabezado)
    linea = next(csvreader)
    dicc =  {"Fecha: ":linea[0],
              "Valor: ":linea[1]
            }
    archivo.write(json.dumps(dicc))

def incremento():
    """Carga en un archivo json el incremento en % del valor del dolar desde junio del 2019 hasta abril del 2021"""
    archivo = open("archivo.json","w")
    csvreader = leerCSV()
    encabezado = next(csvreader)
    #encabezado = [item.replace('"','').replace('','') for item in encabezado]
    #print(encabezado)
    total = 0
    for linea in csvreader:
        nro = linea[5].replace('"','').replace('%','').replace(',','.')
        total += float(nro)
    dicc = {"Porcentaje de aumento" : total}
    archivo.write(json.dumps(dicc))

def menor():
    """Carga en un archivo json el porcentaje de aumento mas bajo del valor del dolar"""
    archivo = open("archivo.json","w")
    csvreader = leerCSV()
    encabezado = next(csvreader)
    #encabezado = [item.replace('"','').replace('','') for item in encabezado]
    #print(encabezado)
    lista = []
    for linea in csvreader:
        nro = linea[5].replace('"','').replace('%','').replace(',','.')
        lista.append(nro)
    lista.sort()
    dicc = {"Porcentaje de aumento mas bajo" : lista[0]}
    archivo.write(json.dumps(dicc))
