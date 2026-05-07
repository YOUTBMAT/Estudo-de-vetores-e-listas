# Definindo o vetor com os números sorteados (6 posições)
mega_sena = [2, 3, 4, 14, 29, 47]

# Criando um vetor vazio de 6 posições para os números jogados
jogados = [0] * 6

print("--- Validador da Mega Sena ---")

# Lendo os números do teclado e preenchendo o vetor manualmente
for i in range(6):
    jogados[i] = int(input(f"Digite o {i+1}º número da sua aposta: "))

# Variável para contar os acertos
quantidade_acertos = 0

# Comparando cada número jogado com cada número sorteado (Busca manual)
for i in range(6): # Percorre o vetor jogados
    for j in range(6): # Percorre o vetor mega_sena
        if jogados[i] == mega_sena[j]:
            quantidade_acertos += 1

# Exibindo os resultados
print("\n" + "="*30)
print(f"Números Sorteados: {mega_sena}")
print(f"Números Jogados:   {jogados}")
print(f"Quantidade de acertos: {quantidade_acertos}")
print("="*30)

if quantidade_acertos == 6:
    print("Parabéns! Você é o novo milionário!")