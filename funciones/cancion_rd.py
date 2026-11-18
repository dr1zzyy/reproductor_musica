import random

from funciones.mst_playlist import mst_playlist

def cancion_random():
    playlist = mst_playlist(show=False)
    
    if len(playlist) > 0:
        cancion_elegida = random.choice(playlist)
        print(f"Eleccion random -> 🎵 {cancion_elegida["nombre"]} - {cancion_elegida["autor"]} 🎵")
    else:
        print("La playlist está vacía.")