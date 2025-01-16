import random

kolminumeroinen_koodi = ''.join(str(random.randint(0, 9)) for _ in range(3))
nelinumeroinen_koodi = ''.join(str(random.randint(1, 6)) for _ in range(4))

print(f"Kolminumeroinen koodi: {kolminumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumeroinen_koodi}")

