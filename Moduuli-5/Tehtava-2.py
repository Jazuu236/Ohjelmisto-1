luvut = []

luku = input("Anna ensimmäinen luku tai lopeta painamalla ENTER: ")
while luku != "":
    luvut.append(luku)
    luku = input("Anna seuraava luku tai lopeta painamalla ENTER: ")

luvut.sort(reverse=True)
suurin = luvut[:5]

print("Viisi suurinta lukua:", suurin)