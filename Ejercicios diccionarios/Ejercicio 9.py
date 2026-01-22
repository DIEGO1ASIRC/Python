facturas = []
opcion = "0"
while opcion != "3":

    print("1.-Añadir nueva factura")
    print("2.-Pagar una existente")
    print("3.-Terminar")
    opcion = str(input("Porfavor introduzca una opcion: "))


    if opcion == "1":

        numero_factura = input("Porfavor introduzca el numero de factura: ")
        precio_factura = int(input("Porfavor introduzca el precio de la factura: "))

        facturas["numero_factura"] = precio_factura

    