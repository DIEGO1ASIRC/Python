primer_numero = int(1)

segundo_numero = int(1)

while primer_numero <= 10:

    print ("Tabla de multiplicar del", primer_numero)

    while segundo_numero <= 10:
        numero_total = primer_numero * segundo_numero
        print(primer_numero, "*", segundo_numero, "=", numero_total)
        segundo_numero = segundo_numero + 1

    primer_numero = primer_numero + 1
    segundo_numero = int(1)