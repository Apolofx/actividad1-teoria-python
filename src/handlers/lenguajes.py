import json
import csv
import math
from functools import reduce
#Sumar todos los porcentajes que 
#Mientras la clave date no cambie, 
    #sumo a cada lenguaje el porcentaje de la fila actual

def lenguajes_mas_usados_por_anio(anio):
    with open('datasets/most-popular-programming-languages-since-2004.csv') as csvfile:  
        reader = csv.DictReader(csvfile)
        filtrado_por_anio = list(filter(lambda x: x['Date'].split()[1] == str(anio), reader))
        #elimino columna de fecha y sumo todos los meses
        suma_mensuales = reduce(lambda a,b: {key: float(a[key])+float(b[key]) for key in a.keys() if key != 'Date'}, filtrado_por_anio)
        #promedio anual por lenguaje
        promedio_anual = {k: v / 12 for k,v in suma_mensuales.items()}
        new_json_file = {}
        with open('datos_procesados/lenguajes.json', "r") as json_file:
            new_json_file = json.load(json_file)
            new_json_file[f'promedios_anio_{anio}'] = promedio_anual
        with open('datos_procesados/lenguajes.json', "w") as json_file:
            json.dump(new_json_file, json_file, indent=4)

