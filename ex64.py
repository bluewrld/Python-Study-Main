#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = cont = soma = 0
numero = int(input('\033[0;32mDigite um número\033[m \033[0;31m[999 para parar]:\033[m '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('\033[0;32mDigite um número\033[m \033[0;31m[999 para parar]:\033[m '))
print(f'\033[0;35mVocê digitou\033[m \033[0;34m{cont}\033[m \033[0;35mnúmeros e a soma entre eles foi\033[m \033[0;34m{soma}.\033[m')