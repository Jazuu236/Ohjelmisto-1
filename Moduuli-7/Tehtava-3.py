lentoasemat = {}
while True:
    print("Syötä mitä haluat tehä.")
    print("Haluatko syöttää lentokentän? Kirjoita: lisää")
    print("Haluatko etsiä lentokentän? Kirjoita: etsi")
    print("Haluatko lopettaa? Kirjoita: lopeta")
    valinta = input("Valinta: ")

    if valinta == "lisää":
        icao = input("Syötä lentokentän ICAO-koodi: ")
        nimi = input("Syötä lentokentän nimi: ")
        lentoasemat[icao] = nimi
        print(f"{icao}, {nimi} lisätty!")

    elif valinta == "etsi":
        icao = input("Syötä lentokentän ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("Lentokentää ei löytyny!")

    elif valinta == "lopeta":
        print("Lopetetaan")
        break

    else:
        print("Virheellinen syöte!")