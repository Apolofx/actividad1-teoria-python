import PySimpleGUI as sg

def build():
    layout = [
        [sg.Button("Analizar datos de delitos en CABA",size=(50,3), key="-DELITOS-", font="Helvetica 14")],
        [sg.Button("Analizar datos de lenguajes de progamacion",size=(50,3), key="-LENGUAJES-",font="Helvetica 14")],
        [sg.Button("Salir",size=(50,3), key="-SALIR-",font="Helvetica 14") ]
    ]
    return sg.Window("Analisis de datos").layout(layout)