#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('\u001b[32mDigite o ângulo que você deseja:\u001b[m '))
seno = math.sin(math.radians(angulo))
print(f'\u001b[34mO ângulo de\u001b[m \033[1;31m{angulo}\033[m \u001b[34mtem o SENO de\u001b[m \033[1;31m{seno:.2f}\033[m')
cosseno = math.cos(math.radians(angulo))
print(f'\u001b[34mO ângulo de\u001b[m \033[1;31m{angulo}\033[m \u001b[34mtem o COSSENO de\u001b[m \033[1;31m{cosseno:.2f}\033[m')
tangente = math.tan(math.radians(angulo))
print(f'\u001b[34mO ângulo de\u001b[m \033[1;31m{angulo}\033[m \u001b[34mtem a TANGENTE de\u001b[m \033[1;31m{tangente:.2f}\033[m')