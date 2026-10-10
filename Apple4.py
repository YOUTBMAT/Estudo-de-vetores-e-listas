local = 0
while True:
    move = input("Digite 1 para andar para frente, -1 para andar para trás, 0 para sair: ")

    moves = [-1,1,0]

    if move == '1':
        local += 1
        print(f"Andou e está na posição {local}")

    elif move == '-1':
        if local == 0:
            print("Você não pode andar para -1")
        else:
            local -= 1
            print(f"Andou e está na posição {local}")

    elif move == '0':
        print(f"Você andou até {local}")
        break

    elif move not in moves:
        print("ERRO: Digite uma opção viável")
        continue