leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

leiviskamassa = leiviska * 20 * 32 * 13.3
naulamassa = naula * 32 * 13.3
luotimassa = luoti * 13.3

kokonaismassa = leiviskamassa + naulamassa + luotimassa

kilogrammat = kokonaismassa / 1000
grammat = kokonaismassa % 1000

print(str(int(kilogrammat)) + " kg " + str(int(grammat)) + " g")