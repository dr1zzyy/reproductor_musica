def mst_playlist():
    with open("canciones.txt", "r") as playlist:
        print("\n------ PLAYLIST ------")
        count=1
        for linea in playlist:
            cancion,autor = linea.strip().split(";")
            print(f"{count}. {cancion} - {autor}")
            count+=1
        print("----------------------\n")