numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_invertidos = numeros[::-1]

for numero in numeros_invertidos:

    if numero == 1:
      
      print(numero)  
      
      break

    print(numero, end=",")
