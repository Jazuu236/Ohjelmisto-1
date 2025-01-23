import random
n = int(input("Anna arvauksien määrä: "))
sisällä = 0
for _ in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <=1:
        sisällä +=1
pi = 4 * sisällä / n
print(f"Arvioitu piin arvo: {pi}")
