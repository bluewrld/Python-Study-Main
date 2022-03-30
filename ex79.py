#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

numeros = list()
while True:
    n = int(input('\u001b[34mDigite um valor:\u001b[m '))
    if n not in numeros:
        numeros.append(n)
        print('\033[0;32mValor adicionado com sucesso...\033[m')
    else:
        print('\033[0;31mValor duplicado! não vou adicionar...\033[m')
    r = str(input('\033[1;33mQuer continuar? [S/N]\033[m '))
    if r in 'Nn':
        break
print('\033[1;37m-=\033[m' * 30)
numeros.sort()
print(f'\033[0;35mVocê digitou os valores\033[m \033[0;34m{numeros}\033[m')