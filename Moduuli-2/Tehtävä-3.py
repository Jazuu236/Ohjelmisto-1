print("Syötä suorakulmion kanta ja korkeus saadaksesi sen pinta-alan ja piirin.")
kanta = float(input("Kanta:"))
korkeus = float(input("Korkeus:"))
pinta_ala = kanta*korkeus
piiri = 2*kanta+2*korkeus
print(f"{"Pinta-ala"}: {pinta_ala:10.2f}")
print(f"{"Piiri"}:     {piiri:10.2f}")
