#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('\033[0;34mInforme seu sexo:\033[m \033[0;31m[M/F]\033[m ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'\033[0;35mSexo\033[m \033[0;32m{sexo}\033[m \033[0;35mfoi registrado com sucesso.\033[m')