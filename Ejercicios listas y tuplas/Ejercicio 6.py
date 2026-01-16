asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
suspensas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

for asignatura in asignaturas:

    nota_final = int(input("Porfavor introduzca la nota que has sacado en "+ asignatura +":"))

    if nota_final >= 5:

        suspensas.remove(asignatura)

print(*suspensas)