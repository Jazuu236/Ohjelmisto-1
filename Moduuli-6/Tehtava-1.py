import random

def noppa():
    return random.randint(1,6)
def tulos():
    while (heitto := noppa()) != 6:
          print(f"Heitto: {heitto}")
    print("Heitto: 6")
tulos()
