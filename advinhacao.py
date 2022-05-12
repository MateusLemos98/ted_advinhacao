import random


print('*******************************************')
print('Jogo de Advinhação')
print('*******************************************')



numero_secreto = (random.randrange(1, 101))
total_de_tentativas = 0
print('Qual o nível de dificuldade que você deseja?')
print('Fácil (1), Médio (2), Difícil (3)')

nivel = int(input('Defina o nível:'))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5
else:
    print('Nível inválido. Digite Novamente!')



for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute = int(input("Digite um número entre 1 e 100:"))
    print("Você digitou: ", chute)


    if (chute < 1 or chute > 100):
        print('Você precisa digitar um número entre 1 e 100. Tente novamente.')
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")



print("Fim do jogo")

