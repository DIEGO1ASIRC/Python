nombre = input("Porfavor introduzca su nombre: ")
edad = input("Porfavor introduzca su edad: ")
direccion = input("Porfavor introduzca su direccion: ")
telefono = input("Porfavor introduzca su telefono: ")

persona = {"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}

print(persona["nombre"] ,"tiene", persona["edad"], "años, vive en direccion", persona["direccion"], "y su numero de telefono es ", persona["telefono"])


