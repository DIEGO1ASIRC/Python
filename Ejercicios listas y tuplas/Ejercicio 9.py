palabra = input("Porfavor introduzca una palabra: ")
vocales = ["a","e","i","o","u"]
contador = 0
contador_vocales = 0
longitud = len(palabra)
print (len(palabra))

for letra in palabra:

    if letra in vocales:

        contador_vocales = contador_vocales + 1

print("La palabra que has introducido tiene un total de "+str(contador_vocales)+" vocales")