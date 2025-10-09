cantidad_pan = float(input("Porfavor introduzca el número de barras de pan que no son del día "))
descuento_numero = "60%"
descuento = 60 / 100
precio_total_pan = cantidad_pan * 3.49
pan_descuento = precio_total_pan * descuento

print("Se han vendido", cantidad_pan, "panes que no son del día a los que se les aplicará un descuento del", descuento_numero, "dándonoso un total de", pan_descuento)