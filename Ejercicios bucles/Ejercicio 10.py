numero_pedido = int(input("Porfavor introduzca un número para comprobar is es primo o no: "))

primo_o_no = numero_pedido % 2

if primo_o_no == 0:

    print("El número", numero_pedido, "es primo")

else:

    print("El número", numero_pedido, "no es primo")