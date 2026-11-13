def del_cancion(nombre):

    archivo_formateado= []

    with open("canciones.txt", "r") as playlist:
        canciones = playlist.readlines()
        for cancion in canciones:
            if nombre not in cancion: 
                archivo_formateado.append(cancion)

    with open("canciones.txt", "w") as playlist_nueva:
        playlist_nueva.writelines(archivo_formateado)
        print(f"\nCancion {nombre} eliminada de la playlist\n")