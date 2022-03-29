#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = cont = 0
while True:
    numero = int(input('\u001b[37mDigite um valor\u001b[m \u001b[34m(999 para parar):\u001b[m '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'\033[0;35mA soma dos\033[m \033[0;32m{cont}\033[m \033[0;35mvalores foi\033[m \033[0;32m{soma}.\033[m')