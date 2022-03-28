#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = int(input('\033[0;32mDigite um número:\033[m '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'\033[1;35mAnalizando o número\033[m \033[1;31m{numero}\033[m')
print(f'\033[1;35mUnidade\033[m \033[1;31m{unidade}\033[m')
print(f'\033[1;35mDezena\033[m \033[1;31m{dezena}\033[m')
print(f'\033[1;35mCentena\033[m \033[1;31m{centena}\033[m')
print(f'\033[1;35mMilhar\033[m \033[1;31m{milhar}\033[m')