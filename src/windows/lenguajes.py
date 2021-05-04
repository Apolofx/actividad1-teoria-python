import PySimpleGUI as sg

def build():
    layout = [
        [sg.Text("Lenguajes mas utilizados por año:",size=(50,1),font="Helvetica 14")],
        [sg.Combo([anio for anio in range(2004,2021)],size=(50,1), key='-LENGUAJE_POR_ANIO-', enable_events=True)],
        [sg.Button("Volver", size=(50,3),font="Helvetica 14",key="-SALIR-")]
    ]

    return sg.Window('Lenguajes de Programación').layout(layout)