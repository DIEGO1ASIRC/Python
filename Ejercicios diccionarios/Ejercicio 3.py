fruta = {"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}

fruta_pedir = input("Porfavor introduzca que fruta desea comprar: ")

while fruta_pedir not in fruta:

    fruta_pedir = input("Porfavor introduzca que fruta desea comprar: ")

kilos = int(input("Porfavor introduzca cuantos kilos quiere de la fruta: "))

precio_fruta = fruta[fruta_pedir] 
precio_total = precio_fruta * kilos

print(precio_total)