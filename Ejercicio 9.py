cantidad_invertir = float(input("Porfavor introduzca una cantidad a invertir "))
años = int(input("Porfavor introduzca cuantos años vas a querer invertir "))
interes_anual = 3.25
meses = años*12
cantidad_invertir = cantidad_invertir * interes_anual
resultado = cantidad_invertir * meses
print("El capital obtenido en la inversión será de un total de:", resultado) 