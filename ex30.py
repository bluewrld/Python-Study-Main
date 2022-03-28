#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

numero = int(input('\033[1;33mDigite um número qualquer:\033[m '))
resultado = numero % 2
if resultado == 0:
    print(f'\u001b[34mO número\u001b[m \u001b[32m{numero}\u001b[m \u001b[34mé PAR.\u001b[m')
else:
    print(f'\u001b[34mO número\u001b[m \u001b[32m{numero}\u001b[m \u001b[34mé ÍMPAR.\u001b[m')