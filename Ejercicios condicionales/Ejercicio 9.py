usuario = int(input("Porfavor introduzca su edad para poder calcular la tarifa para la sala de juegos: "))

if usuario < 4:

    print("Enhorabuena puedes entrar gratis")

elif usuario > 4 and usuario < 18:
    print("Debes pagar 5€")

elif usuario > 18:
    print("Debes pagar 10€")