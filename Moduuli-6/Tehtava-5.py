def karsittu(lista):
    for i in lista:
        if i % 2 != 0:
            lista.remove(i)
    return lista

if __name__ == "__main__":
    lista = []
    numerot = (input("Syötä kokonaislukuja tai paina ENTER: "))
    while numerot != "":
        lista.append(int(numerot))
        numerot = (input("Syötä seuraava kokonaisluku tai paina ENTER: "))

print(f"Alkuperäinen lista: {lista}")
print("Karsittu lista: ", karsittu(lista))