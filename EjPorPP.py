import csv
archivo = open("D:/Facultad/Seminario Python/appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')
encabezado = next(csvreader)
print(encabezado)
lista = []
listaDeValoraciones = []
for linea in csvreader:
    if linea[7] == '0' and linea[12] == "ES":
        lista.append(linea[2])
    listaDeValoraciones.append(linea[6])
listaDeValoraciones.sort(reverse=True)
archivo.close()
print(lista)
for i in range(10):
    print(listaDeValoraciones[i])
