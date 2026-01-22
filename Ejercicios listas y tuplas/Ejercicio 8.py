palabra = input("Introduzca una palabra y te diré si es palíndroma: ")

inversa = palabra[::-1]


if palabra == inversa:

    print ("La palabra introducida es palíndroma")

else:

    print("La palabra no es palíndroma")
