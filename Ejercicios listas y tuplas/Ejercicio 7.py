abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
multiplo = 3
contador = 1
abecedario_multiplo = []
while multiplo < len(abecedario):

    multiplo = multiplo * contador
    abecedario_multiplo.push(abecedario(multiplo))

print (abecedario_multiplo)