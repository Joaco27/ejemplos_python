import PySimpleGUI as sg 

def Ventana():
    """Creacion de la ventana dolar"""
    layout = [
        [sg.Text('Que quieres saber??')],
        [sg.Button('Valor del dolar actual', size=(50,2), key='-actual-')],
        [sg.Button('Aumento del dolar desde comienzo de anio', size=(50,2), key='-inc-')],
        [sg.Button('Fecha con menor aumento', size=(50,2), key='-menor-')],
        [sg.Button('Volver', size=(50,2), key='-exit-')],

    ]

    window = sg.Window('Menu Valor del Dolar', no_titlebar=True).Layout(layout)

    return window