import PySimpleGUI as sg 
from src.windows import menuDolar
import src.handlers.guardarDolar as gd 


def start():
    """
    Ejecucion del menu dolar
    """
    window = loop_menuDolar()
    window.close()


def loop_menuDolar():
    """
    Loop del menu dolar
    """
    window = menuDolar.Ventana()

    while True:
        event, value = window.read()

        if event in ( 'Volver', '-exit-'):
            break
        
        if event == '-actual-':
            window.hide()
            gd.actual()
            window.un_hide()

        if event == '-inc-':
            window.hide()
            gd.incremento()
            window.un_hide()
        
        if event == '-menor-':
            window.hide()
            gd.menor()
            window.un_hide()
    
    return window
