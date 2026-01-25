def areaCirculo(radio, altura = 0):

    total = 1

    if altura == 0:

        total = 3.14 * (radio * radio)
    
    else:

        total = 3.14 * (radio * radio) * altura

    return print(total)



areaCirculo(3)