def cuadrado(lista):

    listaCuadrada = []

    for numero in lista:
          
          numeroCuadrado = numero * numero
          listaCuadrada = listaCuadrada + [numeroCuadrado]

    return print(listaCuadrada)

cuadrado([1,2,3,4,5])