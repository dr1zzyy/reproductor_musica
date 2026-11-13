def agg_cancion(nombre, autor):

    with open("canciones.txt", "a") as lista:
        lista.write(f"{nombre};{autor}" + "\n")

    return print(f"\n🎵 Nueva cancion agregada // {nombre}-{autor} //\n")
