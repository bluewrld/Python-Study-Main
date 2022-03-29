#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('\033[0;36mOs valores sorteados foram:\033[m ', end='')
for n in numeros:
    print(f'\033[0;32m{n}\033[m', end=' ')
print(f'\n\033[1;31mO maior valor sorteado foi\033[m \033[0;32m{max(numeros)}\033[m')
print(f'\033[1;34mO menor valor sorteado foi\033[m \033[0;32m{min(numeros)}\033[m')