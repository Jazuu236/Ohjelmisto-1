import random

def noppa(luku):
    return random.randint(1, luku)

def tulos():
    luku = int(input("Syötä nopan lukujen määrä: "))
    while (heitto := noppa(luku)) != luku:
          print(f"Heitto: {heitto}")
    print(f"Heitto: {luku}")

tulos()
