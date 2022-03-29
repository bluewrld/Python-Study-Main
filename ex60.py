#Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('\u001b[37mDigite um número para calcular seu fatorial:\u001b[m '))
c = n
f = 1
print(f'\u001b[32mCalculando {n}! =\u001b[m ', end='')
while c > 0:
    print(f'\u001b[32m{c}\u001b[m', end='')
    print(' \u001b[31mx\u001b[m ' if c > 1 else ' \u001b[31m=\u001b[m ', end='')
    f *= c
    c -= 1
print(f'\u001b[34m{f}\u001b[m')