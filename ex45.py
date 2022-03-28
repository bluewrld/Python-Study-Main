#Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import randint 
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''\033[1;35m
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m
''')
jogador = int(input('\033[0;37mQual é a sua jogada?\033[m '))
print('\033[1;34mJO\033[m')
sleep(1)
print('\033[1;34mKEN\033[m')
sleep(1)
print('\033[1;34mPO!!!\033[m')
sleep(1)
print('\u001b[37m-=\u001b[m' * 11)
print('\033[1;33mComputador jogou {}\033[m'.format(itens[computador]))
print('\033[1;33mJogador jogou {}\033[m'.format(itens[jogador]))
print('\u001b[37m-=\u001b[m' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[0;32mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[0;32mCOMPUTADOR VENCE!\033[m')
    else: 
        print('\033[0;31mJOGADA INVÁLIDA!\033[m')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[0;32mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;33mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[0;32mJOGADOR VENCE!\033[m')
    else: 
        print('\033[0;31mJOGADA INVÁLIDA!\033[m')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[0;32mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[0;32mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATE!\033[m')
    else: 
        print('\033[0;31mJOGADA INVÁLIDA!\033[m')