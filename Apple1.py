quantNums = int(input("Digite a quantidade de números que deseja digitar: "))

nums = []
tempNums = []   # Sequência atual
tempNums2 = []  # Maior sequência guardada

for i in range(quantNums):
    num = int(input("Digite um número: "))
    nums.append(num)

for digit in nums:
    # Se a sequência estiver vazia OU se o número for > ao ÚLTIMO inserido
    if not tempNums or digit > tempNums[-1]:
        tempNums.append(digit)
    else:
        # Quebrou a sequência: recomeça a sequência atual com o novo número
        tempNums = [digit]

    # Se a sequência atual superou o tamanho da maior guardada, atualiza a maior
    if len(tempNums) > len(tempNums2):
        tempNums2 = list(tempNums)

print(len(tempNums2))