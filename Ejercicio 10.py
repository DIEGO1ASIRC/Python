payasos_pedidos = int(input("Porfavor introduzca cuantos payasos has pedido hoy: "))
muñecas_pedidas = int(input("Porfavor introduzca cuantas muñecas has pedido hoy: ")) 
peso_payasos = int(payasos_pedidos * 112)
peso_muñecas = int(muñecas_pedidas * 75)

peso_total = peso_muñecas + peso_payasos

cantidad_total = payasos_pedidos + muñecas_pedidas

print("Has vendido un total de", cantidad_total, "y pesa un total de", peso_total, "gramos")