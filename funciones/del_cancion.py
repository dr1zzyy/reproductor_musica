import json
import os

RUTA = "canciones.json"

def del_cancion(nombre):
    nombre = nombre.lower()

    if os.path.exists(RUTA) and os.path.getsize(RUTA) > 0:
        try:
            with open(RUTA, "r") as archivo:
                datos = json.load(archivo)
        except json.JSONDecodeError:
            datos = []
    else:
        datos = []

    INPUT = [u for u in datos if u.get("nombre") != nombre]

    if INPUT == datos:
        return print("No se encontro la cancion")

    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(INPUT, f, indent=4, ensure_ascii=False)

    print(f"\n❌️ Has eliminado la cancion // {nombre}\n")