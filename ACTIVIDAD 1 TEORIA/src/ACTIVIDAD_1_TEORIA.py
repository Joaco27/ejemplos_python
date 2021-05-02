
import csv
import json




def Apps():
    arch = open('D:/Facultad/Seminario Pythonga/common_apps.csv', 'r')
    csvreader = csv.reader(arch, delimiter=',')
    encabezado = next(csvreader)
    print(encabezado)





from src.components import menuInicio

def start():
    """
    Iniciar menu principal
    """
    menuInicio.start()