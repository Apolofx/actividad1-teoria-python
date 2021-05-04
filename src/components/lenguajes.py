from src.windows import lenguajes as window_lenguajes
from src.handlers import lenguajes
import PySimpleGUI as sg
def start():
    window = loop()
    window.close()

def loop():
    window = window_lenguajes.build()

    while True:
        event, values = window.read()

        if event == '-SALIR-':
            break
        if event == '-LENGUAJE_POR_ANIO-':
            lenguajes.lenguajes_mas_usados_por_anio(values[event])
            sg.Popup("Se agregó un nuevo dato a datos_procesados/lenguajes.json")
    return window