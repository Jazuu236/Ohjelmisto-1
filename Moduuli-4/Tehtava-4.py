import random
vastaus = random.randint(1, 10)
while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1-10: "))
        if arvaus < vastaus:
            print("Liian pieni arvaus")
        elif arvaus > vastaus:
            print("Liian suuri arvaus")
        else:
            print("Oikein!")
            break
    except ValueError:
        print("Anna vain kokonaisluku")