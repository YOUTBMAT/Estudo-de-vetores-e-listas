numeros = [5, 7, 12, 2, 9, 21]

numeros[1] = 17
numeros[3] = 22
numeros[2] = 1
numeros[4] = 29

soma = numeros[4] + numeros[5]
sub = numeros[3] - numeros[1]
mult = numeros[0] * numeros[5]
div = numeros[3] / numeros[2]

print(f"Soma = {soma}, Subtração = {sub}, Multiplicação = {mult}, Divisão = {div}")

indice = 0
while indice < 6:
     print(f"{numeros[indice]*2}")
     indice += 1

     
#  numeros = [10, 7, 2, 15]
#  indice = 0
#  while indice < 4:
#      print(numeros[indice])
#      indice += 1
     
#  numeros = [10, 7, 2, 15]
#  indice = 0
#  while indice < 4:
#      print(f"{numeros[indice]*2}")
#      indice += 1