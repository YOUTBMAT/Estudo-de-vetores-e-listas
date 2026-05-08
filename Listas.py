lista = [3,2,1]
# 0 é posição, 5 é a adição
lista.insert(0,5)
# adiciona na ultima posição uma única coisa
lista.append(6)
# adiciona várias coisas no fim
lista.extend([8, 8, 7])
# remove o valor, não o que esta no índice
lista.remove(2)
# remove o que está no índice
lista.pop(0)
# obtem a informação de qual o índice do valor
index = lista.index(6)
# conta o número de registros de um número pedido
count = lista.count(8)
print (f"Lista completa {lista}, Index pedido: {index}, Count pedido: {count}")

# organiza a lista em ordem crescente
lista.sort()
print (f"Lista completa {lista}, Index pedido: {index}, Count pedido: {count}")

# inverte a ordem da lista
lista.reverse()
print (f"Lista completa {lista}, Index pedido: {index}, Count pedido: {count}")

# Retorna o tamanho da lista
tamanho = len(lista)
# Retorna o menor valor da lista
menor = min(lista)
# Retorna o maior valor da lista
maior = max(lista)
# Retorna a soma dos valores da lista
soma = sum(lista)
# Retorna a lista ordenada (gera uma nova lista)
ordenada = sorted(lista)
# Retorna a lista ordenada decrescente (gera uma nova lista)
decrescente = sorted(lista, reverse=True)
# Retorna a lista na ordem inversa (gera uma nova lista)
invertida = list(reversed(lista))

print(f"Tamanho: {tamanho}, Menor: {menor}, Maior: {maior}, Soma: {soma}")
print(f"Ordenada: {ordenada}, Decrescente: {decrescente}, Invertida: {invertida}")
