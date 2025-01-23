tunnus = "python"
salasana = "rules"
y = 0
ymax = 5
while y < ymax:
    t = input("Syötä käyttäjätunnus: ")
    s = input("Syötä salasana: ")
    if t == tunnus and s == salasana:
        print("Tervetuloa")
        break
    else:
        print("Väärä käyttäjätunnus ja salasana")
        y += 1
if y == ymax:
    print("Pääsy evätty")