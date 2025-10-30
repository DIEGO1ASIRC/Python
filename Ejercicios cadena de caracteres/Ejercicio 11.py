producto_completo = input("Porfavor introduzca el nombre del producto, el precio y el número de unidades: ")

producto_completo = producto_completo.split(" ")

nombre = producto_completo[0]
precio = producto_completo[1]
unidades = producto_completo[2]

print(nombre, precio.zfill(6), unidades.zfill(3))