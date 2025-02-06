import mariadb

def hae_lentokentta(icao):
    yhteys = mariadb.connect(
        user="root",
        password="Wedwed04!",
        host="127.0.0.1",
        port=3306,
        database="flight_game"
    )
    sql = "SELECT name, municipality FROM airport WHERE ident=%s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    if tulos:
        print(f"Lentokentän nimi: {tulos[0]}. Sijainti: {tulos[1]}.")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")
    kursori.close()
    yhteys.close()


icao = input("Anna lentoaseman ICAO-koodi: ")
hae_lentokentta(icao)
