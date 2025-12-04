
numeros_ganadores = input("Porfavor introduzca los números ganadores de la lotería: ")

lista_ganadores = []

while numeros_ganadores != "salir":

    lista_ganadores.append(numeros_ganadores)

    numeros_ganadores = input("Porfavor introduzca los números ganadores de la lotería: ")

    numeros = ",".join(sorted(lista_ganadores))

if numeros_ganadores == "salir":

    print ("Los números ganadores son: " + numeros )
