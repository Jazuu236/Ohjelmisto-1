def summa(lista):
    return sum(lista)
if __name__ == "__main__":
    lista = []
    numerot = (input("Syötä kokonaisluku tai paina ENTER: "))
    while numerot != "":
        lista.append(int(numerot))
        numerot = (input("Syötä seuraava kokonaisluku tai paina ENTER: "))

print("Syötettyjen lukujen summa on:", summa(lista))