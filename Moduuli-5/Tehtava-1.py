import random

noppa = int(input("Syötä arpakuutioiden lukumäärä: "))
for _ in range(noppa):
    print(random.randint(1,6))