numero_pedido = int(input("Porfavor introduzca un numero para mostrar todos los numeros impares anteriores a el: "))
numero = int(1)
numero_division = int(2)


while numero <= numero_pedido:

    division = numero % numero_division

    if division != 0 :

        print(numero)

    numero = numero + 1
    
    









