def calcular(lista):

    media = sum(lista)/len(lista) 

    lista_definitiva = []
    lista_varianza=[]
    
    for numero in lista:

        varianza = media - numero
        
        lista_varianza.append(varianza)

    for numero in lista_varianza:

        cuadrado = numero * numero
        
        lista_definitiva.append(cuadrado)

    return print(media), print(sum(lista_definitiva))




calcular([1,2,3,4,5])