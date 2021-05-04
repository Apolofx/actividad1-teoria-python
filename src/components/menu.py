import PySimpleGUI as sg
from src.windows import menu
from src.components import delitos, lenguajes
sg.theme("Material1")

def start():
    window = loop()
    window.close()

def loop():
    window = menu.build()

    while True:
        event, values = window.read()

        if event == "-SALIR-":
            break
        if event == "-DELITOS-":
            window.hide()
            delitos.start()
            window.un_hide()

        if event == "-LENGUAJES-":
            window.hide()
            lenguajes.start()
            window.un_hide()
    return window
