#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último separadamente.

n = str(input('\033[1;36mDigite seu nome completo:\033[m ')).strip()
nome = n.split()
print(f'\033[1;35mSeu primeiro nome é\033[m \033[1;31m{nome[0]}\033[m')
print(f'\033[1;35mSeu último nome é\033[m \033[1;31m{nome[len(nome)-1]}\033[m')