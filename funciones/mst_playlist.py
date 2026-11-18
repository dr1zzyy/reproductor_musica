import json
import os 

RUTA = "canciones.json"

def mst_playlist(show=True):
    if os.path.exists(RUTA) and os.path.getsize(RUTA) > 0:
        try:
            with open(RUTA, "r") as archivo:
                datos = json.load(archivo)
        except json.JSONDecodeError:
            datos = []
    else:
        datos = []

    if show == True:
        print("========== PLAYLIST ==========================")
        
        for lista in datos:
            print(f'{lista["nombre"]} — {lista["autor"]}')
    
        print("========== PLAYLIST ==========================")

    return datos