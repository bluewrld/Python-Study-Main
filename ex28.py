#Escreva na tela um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time
computador = randint(0, 5) #Faz o computador pensar
print('\u001b[37m-=-\u001b[m' * 20)
print('\033[0;33mVou pensar em um número entre 0 e 5. Tente advinhar...\033[0m')
print('\u001b[37m-=-\u001b[m' * 20)
time.sleep(3)
jogador = int(input('\033[0;33mEm que número eu pensei?\033[m ')) #Jogador tenta advinhar
if jogador == computador:
    print('\u001b[35mPARABÉNS, você conseguiu vencer!\u001b[m')
else:
    print(f'\033[0;31mGANHEI! eu pensei no número\033[m \033[0;35m{computador}\033[m \033[0;31m, não no número\033[m \033[0;35m{jogador}\033[m\033[0;31m!\033[m')