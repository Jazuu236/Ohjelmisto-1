def nimilist():
    nimet = set()
    while True:
        nimi = input("Syötä nimi tai paina ENTER: ")
        if nimi == "":
            break
        if nimi in nimet:
            input("Aiemmin syötetty nimi. Paina ENTER jatkaaksesi!")
        else:
            nimet.add(nimi)
    print("Syötetyt nimet: ")
    print(nimet)
nimilist()
