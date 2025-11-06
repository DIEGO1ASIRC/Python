frase_pedida = input("Porfavor introduzca una frase: ")
letra_pedida = input("Porfavor introduzca una letra: ")
posicion = int(0)
contador = int(0)
while posicion < len(frase_pedida):

    if frase_pedida[posicion] == letra_pedida:
        
        contador = contador + 1

    posicion = posicion +1

print ("Hemos encontrado un total de", contador, "contenidas en la frase que has puesto")