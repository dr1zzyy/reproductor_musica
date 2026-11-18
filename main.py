import os
import time

from funciones.agg_cancion import agg_cancion
from funciones.mst_playlist import mst_playlist
from funciones.buscar_cancion import buscar_cancion
from funciones.del_cancion import del_cancion
from funciones.cancion_rd import cancion_random

#agg_cancion("Cancion2", "Roman")
#mst_playlist()
#buscar_cancion("Cancion1")


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

puntos = [
    ".",
    "..",
    "...",
    "....",
    ".....",
]

def animate(animation, speed, cicles):
    for cicle in range(0, cicles+1):
        for frame in animation:
                print(frame)
                time.sleep(speed)
                clean()

menu = True

while menu == True:

    clean()

    animate(puntos, 0.024, 1)

    print("=========== REPRODUCTOR DE MUSICA ============")
    print("1. Agregar cancion")
    print("2. Mostrar playlist")
    print("3. Buscar cancion")
    print("4  Eliminar cancion")
    print("5. Escuchar aleatoria")
    print("6. Salir")
    print("==============================================")

    seleccion = input("Ingresa una opcion >> ")

    if seleccion == "1":
        clean()
        animate(puntos, 0.024, 1)
        nombre = input("Ingresa el nombre de la cancion >> ")
        autor = input("Ingresa el autor de la cancion >> ")
        genero = input("Ingresa el genero de la cancion >> ")

        clean()
        animate(puntos, 0.024, 1)
        agg_cancion(nombre,autor, genero)
        input("\nPresiona ENTER para continuar...")

    if seleccion == "2":
        clean()
        animate(puntos, 0.024, 1)
        clean()
        animate(puntos, 0.024, 1)
        mst_playlist()
        input("\nPresiona ENTER para continuar...")        

    if seleccion == "3":
        clean()
        animate(puntos, 0.024, 1)
        print("*** Puedes buscar por cualquiera de los 3 ***\n")
        nombre = input("Busqueda por nombre, autor o genero >> ")
        clean()
        animate(puntos, 0.024, 1)
        
        buscar_cancion(nombre)

        input("\nPresiona ENTER para continuar...")
        

    if seleccion == "4":
        clean()
        animate(puntos, 0.024, 1)
        nombre = input("Ingresa el nombre de la cancion >> ")
        clean()
        animate(puntos, 0.024, 1)
        del_cancion(nombre)
        input("\nPresiona ENTER para continuar...")

    if seleccion == "5":
        clean()
        animate(puntos, 0.024, 1)
        cancion_random()
        input("\nPresion ENTER para continuar...")

    if seleccion == "6":
        clean()
        animate(puntos, 0.024, 1)
        print("Gracias por usar el sistema")
        menu= False
        break   