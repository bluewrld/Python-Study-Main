#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint
valor = 0
while True:
    jogador = int(input('\u001b[33mDiga um valor:\u001b[m '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[0;35mPar ou ímpar: [P/I]\033[m ')).strip().upper()[0]
    print(f'\033[0;32mVocê jogou {jogador} e o computador {computador}. total de {total}\033[m ', end=' ')
    print('\033[0;31mDEU PAR\033[m' if total % 2 == 0 else '\033[0;31mDEU ÍMPAR\033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;32mVocê VENCEU!\033[m')
            valor += 1
        else:
            print('\033[1;31mVocê PERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;32mVocê VENCEU!\033[m')
            valor += 1
        else:
            print('\033[1;31mVocê PERDEU!\033[m')
            break
    print('\033[1;33mVamos jogar novamente...\033[m')