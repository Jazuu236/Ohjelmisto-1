import mariadb

def lukumaara(koodi):
    yhteys = mariadb.connect(
        user="root",
        password="Wedwed04!",
        host="127.0.0.1",
        port=3306,
        database="flight_game"
    )
    sql = """
    SELECT type, COUNT(*) as lukumaara
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    """
    kursori = yhteys.cursor()
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]} kappaletta")
    else:
        print("Ei löytynyt lentokenttiä!.")
    kursori.close()
    yhteys.close()

koodi = input("Anna maakoodi: ")
lukumaara(koodi)