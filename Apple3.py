while True:
    quantNums = int(input("Digite a quantidade de números que deseja digitar: "))

    if quantNums % 2 != 0:
            print("A quantidade de números digitados deve ser par, e metade deve ser positiva, a outra negativa")
            continue
    
    nums = []
    negativos = 0
    positivos = 0
    erro = False
    
    for i in range(quantNums):
        num = int(input("Digite um número: "))
        nums.append(num)

    for digit in nums:
        if digit == 0:
            print("ERRO: 0 não é positivo nem negativo")
            erro = True
            break

    if erro:
        continue

    for i in nums:  
        if i >= 1:
            positivos += 1
        elif i <= -1:
            negativos += 1


    if negativos != positivos:
        print("ERRO: A quantidade de números positivos e negativos deve ser igual")
        continue

    tamanho = len(nums)

    print(f"Tamanho: {tamanho}, Primeiro: {nums[0]}, Ultimo: {nums[-1]}")
    break   