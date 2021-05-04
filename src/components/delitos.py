import PySimpleGUI as sg
from src.windows import delitos as window_delitos
from src.handlers import delitos 
def start():
    window = loop()
    window.close()

def loop():
    window = window_delitos.build()

    while True:
        event, values = window.read()
        if event == "-SALIR-":
            break
        if event == "-MAX_DELITOS-":
            delitos.get_barrio_max_delitos()
            sg.Popup("Se agregó un nuevo dato a datos_procesados/delitos.json")

        if event == "-TIPOS_DELITOS-":
            delitos.get_delitos_por_tipo()
            sg.Popup("Se agregó un nuevo dato a datos_procesados/delitos.json")

    return window