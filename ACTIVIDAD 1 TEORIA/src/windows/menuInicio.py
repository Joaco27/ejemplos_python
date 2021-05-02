import PySimpleGUI as sg 

def Ventana():
    """Creacion de la ventana inicio"""
    layout = [
        [sg.Text('Que datos analizamos??')],
        [sg.Button('Valor del dolar Jun2019-Actualidad', size=(50,2), key='-dolar-')],
        [sg.Button('Streamers de twitch', size=(50,2), key='-twitch-')],
        [sg.Button('Salir', size=(50,2), key='-exit-')],

    ]

    window = sg.Window('Actividad 1 por Python PLus -TEORIA-', no_titlebar=True).Layout(layout)

    return window