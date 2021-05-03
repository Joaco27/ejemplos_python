import PySimpleGUI as sg 
from src.windows import menuInicio
from src.components import menuStream
from src.components import menuDolar


def start():
    """
    Ejecucion del menu principal
    """
    window = loop_menuInicio()
    window.close()


def loop_menuInicio():
    """
    Loop del menu principal
    """
    window = menuInicio.Ventana()

    while True:
        event, value = window.read()

        if event in ('Salir', '-exit-'):
            break

        if event == '-dolar-':
            window.hide()
            menuDolar.start()
            window.un_hide()
        
        if event == '-twitch-':
            window.hide()
            menuStream.start()
            window.un_hide()
    
    return window
