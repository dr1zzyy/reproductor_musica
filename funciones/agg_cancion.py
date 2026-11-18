import json
import os

RUTA = "canciones.json"

def guardar(cancion, ruta):
    if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
            if not isinstance(datos, list):
                datos = []
        except json.JSONDecodeError:
            datos = []
    else:
        datos = []

    datos.append(cancion)

    print(f"\n🎵 Nueva cancion agregada // {cancion["nombre"]} <-> {cancion["genero"]}\n")

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    return True


def agg_cancion(nombre, autor, genero):
    INPUT = {"nombre": nombre.lower(), "autor": autor.lower(), "genero": genero.lower()}
    return guardar(INPUT, RUTA)