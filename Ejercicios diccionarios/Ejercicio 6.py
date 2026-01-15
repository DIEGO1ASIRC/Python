nombre = ""
edad = ""
sexo = ""
telefono = ""
correo = ""

datos_personales = {"nombre": nombre, "edad": edad, "sexo": sexo, "telefono": telefono, "correo": correo}
opcion = ""
while opcion != "salir":

    opcion = input("Cuando desee salir simplemente presione salir, para seguir escriba siguiente ")

    if  opcion == "siguiente":

        nombre = input("Porfavor introduzca su nombre: ")
        datos_personales["nombre"] = nombre
        print (datos_personales)

        edad = input("Porfavor introduzca su edad: ")
        datos_personales["edad"] = edad
        print (datos_personales)

        sexo = input("Porfavor introduzca su sexo: ")
        datos_personales["sexo"] = sexo
        print (datos_personales)

        telefono = input("Porfavor introduzca su telefono: ")
        datos_personales["telefono"] = telefono
        print (datos_personales)

        correo = input("Porfavor introduzca su correo: ")
        datos_personales["correo"] = correo
        print (datos_personales)



