articulo = ""
precio = 0
lista_de_compra = {articulo:precio}
while articulo != "salir":
    
    articulo = input("Porfavor inroduzca el nombre del articulo ")
    precio = input("Porfavor inroduzca el precio del articulo ")

    lista_de_compra[articulo] = precio

del lista_de_compra[""]
del lista_de_compra["salir"]
print (lista_de_compra)