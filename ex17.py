#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('\u001b[32mComprimento do cateto oposto:\u001b[m '))
ca = float(input('\u001b[32mComprimento do cateto adjacente:\u001b[m '))
## hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co,ca)
print(f'\u001b[34mA hipotenusa vai medir\u001b[m \033[1;31m{hi:.2f}\033[m')