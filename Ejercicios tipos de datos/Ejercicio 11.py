ahorros = float(input("Porfavor introduzca la cantidad de dinero que tienes ahorrado ")) 

interes_año = 4 / 100

ahorros_finales = ahorros * (1 + interes_año)

ahorros_finales2 = ahorros_finales * 2
ahorros_finales3 = ahorros_finales * 3

print("El primer año tus ahorros serán", round(ahorros_finales), "tu segundo año serán de", round(ahorros_finales2), "tu tercer año serán de", round(ahorros_finales3))
