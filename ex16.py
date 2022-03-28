#Crie um programa que leia um número REAL qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
número = float(input('\u001b[32mDigite um valor:\u001b[m '))
print(f'\u001b[34mO valor digitado foi\u001b[m \033[1;31m{número}\033[m \u001b[34me sua porção inteira é\u001b[m \033[1;31m{math.trunc(número)}\033[m')

número = int(input('\u001b[32mDigite um valor:\u001b[m '))
print(f'\u001b[34mO valor digitado foi\u001b[m \033[1;31m{número}\033[m \u001b[34me sua porção inteira é\u001b[m \033[1;31m{math.sqrt(número)}\033[m')