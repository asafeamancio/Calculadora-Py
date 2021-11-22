import random

def jogar():
    numero_secreto = (random.randrange(1, 101))
    print('************************************')
    print('*         Adivinha Número          *')
    print('*              ', numero_secreto, '                *')
    print('************************************')

    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print('Escolha uma dificuldade:')
    print('(1) Normal (2) Difícil (3) Muito Difícil')
    nivel = int(input('Digite o nível: '))

    if (nivel == 1):
        pontos = 500
        total_de_tentativas = 10
    if (nivel == 2):
        pontos = 800
        total_de_tentativas = 5
    if (nivel == 3):
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        numero_digitado = input('Digite um número de 1 e 100: ')
        chute = int(numero_digitado)
        print('Você digitou ', chute, '!')

        if (chute < 1 or chute > 100):
            print('Digite um número entre 1 e 100!')
            continue

        if (numero_secreto == chute):
            print('Você Acertou e fez {} pontos!'.format(pontos))
            break
        elif (rodada == total_de_tentativas and chute != numero_secreto):
            print('Você perdeu! O numero secreto era {} e você fez {} pontos.'.format(numero_secreto, pontos))
            break

        else:
            if (chute == numero_secreto + 1 or chute == numero_secreto + 2):
                print('Você Errou, mas esta bem perto!')
            elif (chute == numero_secreto - 1 or chute == numero_secreto - 2):
                print('Você Errou, mas esta bem perto!')
            elif (chute >= numero_secreto):
                print('Você Errou! Tente um valor menor.')
            elif (chute <= numero_secreto):
                print('Você Errou! Tente um valor maior.')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

print('Fim do Jogo!')
