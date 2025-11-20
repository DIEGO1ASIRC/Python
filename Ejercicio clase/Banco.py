opcion = int(0)
saldo = float(1000)
while opcion != 4:

    print("1. Reintegro")
    print("2. Ingreso")
    print("3. Saldo")
    print("4. Salir")
    opcion = float(input("Porfavor introduzca una opcion: "))

    if opcion == 1:
        
        reintegro=float(input("Cuanta cantidad quieres sacar de tu cuenta: "))
        saldo = saldo - reintegro
        print ("Te has quedado con un total de: ", saldo)

    elif opcion == 2:

        ingreso=float(input("Cuanta cantidad quieres meter en tu cuenta: "))
        saldo = saldo + ingreso
        print ("Te has quedado con un total de: ", saldo)
    
    elif opcion == 3:

        print("Este es tu saldo actual: ",saldo)
    
    elif opcion == 4:

        print("Saliendo del menú")

    else:

        print("Introduzca una opción válida")

