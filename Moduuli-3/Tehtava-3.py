while True:
    sp = input("Syötä sukupuoli (mies/nainen): ").lower()
    if sp == "mies" or sp == "nainen":
        break
    print("Virheellinen syöte. Syötä 'mies' tai 'nainen'.")

hg = int(input("Anna hemoglobiiniarvosi (g/l): "))

if 117 <= hg <= 175 and sp == "nainen":
    print("Arvo on normaali")
elif hg<117:
    print("Arvo on alhainen")
elif hg>175:
    print("Arvo on korkea")
else:
    if 134 <= hg <= 195 and sp == "mies":
        print("Arvo on normaali")
    elif hg < 134:
        print("Arvo on alhainen")
    elif hg > 195:
        print("Arvo on korkea")