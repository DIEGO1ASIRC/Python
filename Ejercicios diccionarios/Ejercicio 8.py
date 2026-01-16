palabra_añadir = "hola"
pregunta = "si"
palabras = {}
contador = 0
frase_definitiva = ""
while pregunta != "no":
    
    palabra_añadir = input("Porfavor introduzca la palabra y su traducción en este formato <palabra>:<traduccion>: ")
    palabra = palabra_añadir.split(":")[0]
    traduccion = palabra_añadir.split(":")[1]
    palabras[palabra] = traduccion
    print (palabras)
    pregunta = input("¿Desea continuar? ")

frase = input("Porfavor introduzca una frase para traducir con las palabras dadas: ")

frase_separada = frase.split(" ")

while len(frase_separada) > contador:

    if frase_separada[contador] in palabras:

        frase_definitiva = frase_definitiva + " " + str(palabras[frase_separada[contador]])

    else:

        frase_definitiva = frase_definitiva + " " + frase_separada[contador]

    contador = contador + 1

print (frase_definitiva)