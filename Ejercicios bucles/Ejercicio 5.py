cantidad_invertir = int(input("Porfavor introduzca la cantidad a invertir: "))
interes_anual = float(input("Porfavor introduzca el interes anual actual: "))
numero_años = int(input("Introduzca el numero de años a invertir: "))

contar_años = int(1)

while contar_años <= numero_años:

    cantidad_invertir = cantidad_invertir * interes_anual

    print("El año número", contar_años, "tenías", cantidad_invertir)

    contar_años = contar_años + 1