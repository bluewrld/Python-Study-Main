#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0 com uma pausa de 1 segundo entre elas.

import time
c = 10
for c in range(10 , -1, -1):
    time.sleep(1)
    print(f'\033[0;34m{c}\033[m')
time.sleep(0.5)
print('\033[0;31mBUM!!!\033[m')