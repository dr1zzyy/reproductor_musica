import json
import os

RUTA = "canciones.json"

def buscar_cancion(busqueda):
        busqueda = busqueda.lower()
        if os.path.exists(RUTA) and os.path.getsize(RUTA) > 0:
            try:
                with open(RUTA, "r") as archivo:
                    datos = json.load(archivo)
            except json.JSONDecodeError:
                datos = []
        else:
            datos = []

        encontrados = 0

        resultados = []

        for lista in datos:
            if busqueda in [lista["nombre"], lista["autor"], lista["genero"]] :
                resultados.append({"nombre": lista["nombre"], "autor": lista["autor"], "genero" : lista["genero"]})
                encontrados += 1

        if encontrados == 0:
            return print("\nNo se encontro ninguna coincidencia\n")
        else:
            print(f"\nCoincidencias encontradas -> {encontrados}\n")
            for cancion in resultados:
                print(f"🎵 {cancion['nombre']} - {cancion['autor']} - {cancion["genero"]}")
