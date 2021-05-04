import json


def get_delitos():
    """Devuelve una lista de diccionarios con la informacion de
    los delitos cometidos en CABA desde 2016
    """
    with open('datasets/delitos.json') as json_file:
        data_delitos = json.load(json_file)
        return data_delitos



def get_delitos_por_barrio():
    """Retorna una lista donde cada clave-valor corresponde
    al nombre de un barrio de CABA y la cantidad de delitos cometidos en el mismo,
    ordenada de menor a mayor por cantidad de delitos.
    
    Ademas agrega dicha lista al archivo JSON datos_procesados/delitos.json en el campo
    delitos_por_barrio 
    """

    lista_delitos = get_delitos()
    delitos_por_barrio = {}
    for delito in lista_delitos:
        barrio = delito["barrio"]
        if not barrio in delitos_por_barrio:
            delitos_por_barrio[barrio] = 1
        else:
            delitos_por_barrio[barrio] += 1
    lista_ordenada = [{k:v} for (k,v) in sorted(delitos_por_barrio.items(),key=(lambda item: item[1]))]
    update_json_delitos("delitos_por_barrio", lista_ordenada)
    return lista_ordenada

def get_barrio_max_delitos():
    """Retorna un diccionario con el nombre del barrio con mayor delitos,
    y el numero de delitos cometidos en dicho barrio.
    """
    delitos_por_barrio = get_delitos_por_barrio()
    return delitos_por_barrio[-1]

def get_delitos_por_tipo():
    lista_delitos = get_delitos()
    delitos_por_tipo = {}
    for delito in lista_delitos:
        tipo = delito["tipo_delito"]
        if not tipo in delitos_por_tipo:
            delitos_por_tipo[tipo] = 1
        else:
            delitos_por_tipo[tipo] += 1
    update_json_delitos("delitos_por_tipo", delitos_por_tipo)
    return delitos_por_tipo

def update_json_delitos(key_name, value):
    datos_procesados = {}
    with open('datos_procesados/delitos.json', 'r') as json_file:
        datos_procesados = json.load(json_file)
    datos_procesados[key_name] = value
    with open('datos_procesados/delitos.json', "w") as json_file:
        json.dump(datos_procesados,json_file, indent=4)