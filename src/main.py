from src.components import menu
import json
import os
def start():
    if not os.path.exists('datos_procesados/delitos.json'):
        new_file = open('datos_procesados/delitos.json', "w")
        json.dump({},new_file)
        new_file.close()
    if not os.path.exists('datos_procesados/lenguajes.json'):
        new_file = open('datos_procesados/lenguajes.json', "w")
        json.dump({},new_file)
        new_file.close()

    menu.start()