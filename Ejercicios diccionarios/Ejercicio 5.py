asignaturas = {"Matematicas":6,"Lengua":7,"Fisica":4,"Quimica":9}
creditosTotales = 0
for asignatura in asignaturas:

    print(asignatura+" tiene "+str(asignaturas[asignatura])+" creditos ")
    creditosTotales = creditosTotales + asignaturas[asignatura]

print ("El total de creditos es: "+ str(creditosTotales))
