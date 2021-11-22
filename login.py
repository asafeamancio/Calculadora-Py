import adivinhacao
import forca

def login():
    print('*************')
    print('*** Login ***')
    print('*************')

    print('\nOpções (1) Advinhação (2) Forca')
    jogo = int(input('Escolha um jogo: '))

    if(jogo == 1):
        print('Iniciando Adivinhação')
        adivinhacao.jogar()
    elif(jogo == 2):
        print('Iniciando Forca')
        forca.jogar()
    elif(jogo != 1 or jogo != 2):
        print('Você digitou um número inválido.')
        print('Desligando...')

if(__name__ == '__main__'):
    login()