edad = int(input("Porfavor introduzca su edad actual: "))
ingresos = int(input("Porfavor introduzca sus ingresos actuales: "))

if edad > 16 and ingresos > 1000:

    print("Tienes que tributar chavalin")

elif edad < 16 or ingresos < 1000:

    print("Anda no tienes que tributar")