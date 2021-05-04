import PySimpleGUI as sg

def build():
    layout=[
        [sg.Button("Analizar delitos por barrio",size=(50,3),font="Helvetica 14", key="-MAX_DELITOS-")],
        [sg.Button("Analizar delitos por tipo", size=(50,3),font="Helvetica 14",key="-TIPOS_DELITOS-")],
        [sg.Button("Volver", size=(50,3),font="Helvetica 14",key="-SALIR-")]
    ]

    return sg.Window("Delitos CABA desde 2016").layout(layout)
