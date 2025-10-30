cesta_compra = input("Porfavor introduzca todo lo que haya comprado separado mediante comas: ")

cesta_compra_separada = cesta_compra.split(",")



print (*cesta_compra_separada, sep="\n")