facturas = {}
opcion = "0"
while opcion != "3":

    print("1.-Añadir nueva factura")
    print("2.-Pagar una existente")
    print("3.-Terminar")
    opcion = str(input("Porfavor introduzca una opcion: "))


    if opcion == "1":

        numero_factura = (input("Porfavor introduzca el numero de factura: "))
        precio_factura = int(input("Porfavor introduzca el precio de la factura: "))

        facturas[numero_factura] = precio_factura

    elif opcion == "2":

        for factura in facturas:

            print ("Numero de factura = "+ str(factura)+ " dinero a pagar = "+ str(facturas[factura]))

        pagar = input("De las facturas existentes cuál desea pagar: ")

        if pagar == factura:

                del facturas[factura]

                print("Te quedan las siguientes facturas: ")
        
    for factura in facturas:

        print ("Numero de factura = "+ str(factura)+ " dinero a pagar = "+ str(facturas[factura]))
    
    

    