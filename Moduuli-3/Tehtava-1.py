kuha = float(input("Syötä kuhan pituus senttimetreinä: "))
if kuha<37:
    alinraja = (37-kuha)
    print(f"Kuhan pituus alittaa 37 cm {alinraja:.2f} senttimetrillä, joten vapauta kuha!")
if kuha>=37:
    print("Voit pyydystää kuhan.")