import csv
archivo = open("D:/Facultad/Seminario Python/appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')
encabezado = next(csvreader)
print(encabezado)
lista = []
listaDeValoraciones = []
for linea in csvreader:
    if linea[8] == "free" and linea[13] == "es":
        lista.append(linea[3])
    listaDeValoraciones.append(linea[7])
listaDeValoraciones.sort(reverse=True)
archivo.close()
print(lista)
for i in range(10):
    print(listaDeValoraciones[i])
