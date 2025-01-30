def litroiksi(gallon):
    return gallon * 3.785

def luku():
    while True:
        gallon = float(input("Syötä gallona määrä: "))
        if gallon < 0:
            print("Lopetetaan!")
            break
        litra = litroiksi(gallon)
        print(f"{gallon} gallonaa on {litra} litraa.")
luku()