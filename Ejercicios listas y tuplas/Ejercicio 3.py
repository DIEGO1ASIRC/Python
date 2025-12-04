asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

contador = 0
notas_totales = []

while contador < len(asignaturas):

    nota = input("Porfavor introduzca la nota que has sacado en " + asignaturas[contador] + ": ")

    notas_totales.append("En " + asignaturas[contador] + " has sacado " + nota)

    contador = contador + 1

for notas_actuales in notas_totales:
    
    print(notas_actuales)