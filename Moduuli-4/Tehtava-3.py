luvut = []
while True:
    numero = input("Anna luku tai paina ENTER: ")
    if numero == "":
        break
    try:
        luku = float(numero)
        luvut.append(luku)
    except ValueError:
        print("Et syöttänyt numeroa!")
if luvut:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt numeroa!")