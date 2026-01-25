def calcularIVA(precio, porcentaje = 0):

    if porcentaje == 0:

        precio = precio * 1.21

    else:

        porcentaje = porcentaje / 100
        precio = precio + (precio * porcentaje)
    
    return print (precio)

        
    

calcularIVA(20, 10)
    