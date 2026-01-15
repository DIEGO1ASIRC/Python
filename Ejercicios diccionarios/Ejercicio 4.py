mes = {"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
fecha_pedida = input("Porfavor introduzca una fecha con el formato dd/mm/aaaa: ")
dia = str(fecha_pedida[0:2])
mes_numero = str(fecha_pedida[3:5]) 
año = str(fecha_pedida[6:10])

for mes_guardado in mes:

    if mes_numero == mes_guardado:

        mes_texto = mes[mes_numero]

print(dia+" de "+mes_texto+" de "+año)