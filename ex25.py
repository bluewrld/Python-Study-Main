#Crie um programa que leia o nome de uma pessoa e diga se ela tem tem REIS  no nome.

nome = str(input('\033[0;32mQual o seu nome completo?\033[m ')).strip()
print(f'\033[0;34mSeu nome tem Reis?\033[m \033[0;31m{"REIS" in nome.upper()}\033[m')