pizza_pedir = input("Porfavor escriba vegetariana si prefiere pizza vegetariana o elige pizza si prefieres no vegetariana: ")

if pizza_pedir == "vegetariana":
    print("Ingredientes vegetarianos: Pimiento y tofu")
    ingrediente = input("Porfavor introduzca que ingrediente quieres que añadamos a su pizza: ")
    pizza_pedida = "pizza vegetariana"

elif pizza_pedir == "pizza":
    print("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón")
    ingrediente = input("Porfavor introduzca el ingrediente que quiere añadir a la pizza: ")
    pizza_pedida = "pizza no vegetariana"

print ("La pizza elegida es la",pizza_pedida, "siendo el ingrediente añadido:",ingrediente)