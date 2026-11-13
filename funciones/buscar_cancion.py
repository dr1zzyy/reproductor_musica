def buscar_cancion(nombre):
    with open("canciones.txt", "r") as playlist:
        encontrados = 0
        for linea in playlist:
            cancion,autor1 = linea.strip().split(";")
            if cancion == nombre:
                encontrados += 1
                return print("\n"+cancion + "->" + autor1+"\n")

        if encontrados == 0 :
            print("\n🔎❌️ Cancion no encontrada\n")
            
            