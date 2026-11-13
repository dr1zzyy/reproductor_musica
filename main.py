from funciones.agg_cancion import agg_cancion
from funciones.mst_playlist import mst_playlist
from funciones.buscar_cancion import buscar_cancion
from funciones.del_cancion import del_cancion

#agg_cancion("Cancion2", "Roman")
#mst_playlist()
#buscar_cancion("Cancion1")

menu = True

while menu == True:
    print("=========== REPRODUCTOR DE MUSICA ============")
    print("1. Agregar cancion")
    print("2. Mostrar playlist")
    print("3. Buscar cancion")
    print("4  Eliminar cancion")
    print("5. Salir")
    print("==============================================")

    seleccion = input("Ingresa una opcion >> ")

    if seleccion == "1":
        nombre = input("Ingresa el nombre de la cancion >> ")
        autor = input("Ingresa el autor de la cancion >> ")

        agg_cancion(nombre,autor)

    if seleccion == "2":
        mst_playlist()

    if seleccion == "3":
        nombre = input("Ingresa el nombre de la cancion >> ")
        buscar_cancion(nombre)

    if seleccion == "4":
        nombre = input("Ingresa el nombre de la cancion >> ")
        del_cancion(nombre)

    if seleccion == "5":
        print("Gracias por usar el sistema")
        menu= False
        break   