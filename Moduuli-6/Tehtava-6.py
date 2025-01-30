import math

def ykhinta(halkaisija, hinta):
    sade = halkaisija / 2
    pintaala = math.pi * (sade ** 2)
    neliom = pintaala * 10000
    yhinta = hinta / neliom
    return yhinta

pizza1hal = float(input("Syötä 1. pizzan halkaisia sentteinä: "))
pizza1hin = float(input("Syötä 1. pizzan hinta euroina: "))
pizza2hal = float(input("Syötä 2. pizzan halkaisia sentteinä: "))
pizza2hin = float(input("Syötä 2. pizzan hinta euroina: "))

pizza1_yhinta = ykhinta(pizza1hal, pizza1hin)
pizza2_yhinta = ykhinta(pizza2hal, pizza2hin)

if pizza1_yhinta < pizza2_yhinta:
    print("Pizza 1 tarjoaa paremman vastineen rahalle.")
elif pizza2_yhinta < pizza1_yhinta:
    print("Pizza 2 tarjoaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat tarjoavat saman vastineen rahalle.")