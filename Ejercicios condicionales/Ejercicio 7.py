renta_anual = int(input("Porfavor introduzca su renta anual: "))

if renta_anual < 10000:
    print ("El tipo de impositivo es del 5%")
elif renta_anual > 10000 and renta_anual < 20000:
    print ("El tipo de impositivo es del 15%")
elif renta_anual > 20000 and renta_anual < 35000:
    print ("El tipo de impositivo es del 20%")
elif renta_anual > 35000 and renta_anual < 60000:
    print ("El tipo de impositivo es del 30%")
elif renta_anual > 60000:
    print ("El tipo de impositivo es del 45%")
