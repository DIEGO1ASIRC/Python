pregunta_precio = input("Dime un precio de algun producto ")

euros = pregunta_precio.split(".")[0]

centimos = pregunta_precio.split(".")[1]


print ("El producto cuesta", euros, "con", centimos, "centimos")