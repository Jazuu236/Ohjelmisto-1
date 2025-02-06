import mariadb
from geopy.distance import geodesic

def koodi(icao):
    yhteys = mariadb.connect(
        user="root",
        password="Wedwed04!",
        host="127.0.0.1",
        port=3306,
        database="flight_game"
    )
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    kursori.close()
    yhteys.close()
    if tulos:
        return (tulos[0], tulos[1])
    else:
        return None

def laske_etaisyys(icao1, icao2):
    koord1 = koodi(icao1)
    koord2 = koodi(icao2)
    if koord1 and koord2:
        etaisyys = geodesic(koord1, koord2).kilometers
        print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys:.2f} kilometriä.")
    else:
        print("ICAO-koodien koordinaatteja ei löytynyt.")

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")
laske_etaisyys(icao1, icao2)
