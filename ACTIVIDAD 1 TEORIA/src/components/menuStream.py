import PySimpleGUI as sg 
from src.windows import menuStream
from src.handlers import guardarStreamer as gs

def start():
    """
    Ejecucion del menu stream
    """
    window = loop_menuStream()
    window.close()


def loop_menuStream():
    """
    Loop del menu stream
    """
    window = menuStream.Ventana()

    while True:
        event, value = window.read()

        if event in ('Volver', '-exit-'):
            break

        if event == '-fame-':
            window.hide()
            gs.famosos()
            window.un_hide()

        if event == '-view-':
            window.hide()
            gs.vistos()
            window.un_hide()

        if event == '-spain-':
            window.hide()
            gs.hispanohablantes()
            window.un_hide()

        
    
    return window
