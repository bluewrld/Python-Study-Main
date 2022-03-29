#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" entre um número entre 0 e 10, só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('\033[0;33mSou seu computador... acabei de pensar em um número entre 0 e 10.\033[m')
print('\033[0;33mSerá que você consegue advinhar qual foi?\033[m ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[1;37mQual é seu palpite?\033[m '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[1;34mMais... tente mais uma vez!\033[m')
        elif jogador > computador:
            print('\033[1;31mMenos... tente mais uma vez!\033[m')
print(f'\033[0;35mAcertou com\033[m \033[1;32m{palpites} Palpites\033[m \033[0;35mPARABÉNS!\033[m')