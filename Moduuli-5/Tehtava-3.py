def alkuluku(luku):
    for i in range(2, luku//2+1):
        if (luku % i) == 0:
            return False
    return True
luku = int(input("Syötä kokonaisluku: "))
print(alkuluku(luku))