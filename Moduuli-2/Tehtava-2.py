import math

print("Syötä ympyrän-säde saadaksesi pinta-ala")
käyttäjä = input("Ympyrän säde: ")
säde = float(käyttäjä)
pinta_ala = pow(säde, 2) * math.pi
print(f"{"Ympyrän pinta-ala on"}: {pinta_ala:10.2f}")