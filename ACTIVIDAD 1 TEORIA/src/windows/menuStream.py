import PySimpleGUI as sg 

def Ventana():
    """Creacion de la ventana streamer"""
    layout = [
        [sg.Text('Que quieres saber??')],
        [sg.Button('Top 5 mas famosos', size=(50,2), key='-fame-')],
        [sg.Button('Top 7 mas vistos', size=(50,2), key='-view-')],
        [sg.Button('Top 3 streamers hispanohablantes', size=(50,2), key='-spain-')],
        [sg.Button('Volver', size=(50,2), key='-exit-')],

    ]

    window = sg.Window('Menu Streamers de Twitch', no_titlebar=True).Layout(layout)

    return window