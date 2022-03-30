# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados, B) A lista de valores, ordenada de forma decrescente e C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    valores.append(int(input('\033[0;36mDigite um valor:\033[m ')))
    resp = str(input('\033[1;33mQuer continuar? [S/N]\033[m '))
    if resp in 'Nn':
        break
print('\033[1;37m-=\033[m' * 30)
print(f'\033[0;34mVocê digitou\033[m \033[0;35m{len(valores)}\033[m \033[0;34melementos.\033[m')
valores.sort(reverse=True)
print(f'\033[0;34mOs valores em ordem descrescente são\033[m \033[0;35m{valores}\033[m')
if 5 in valores:
    print('\033[0;32mO valor 5 faz parte da lista.\033[m')
else:
    print('\033[0;31mO valor 5 não foi encontrado na lista.\033[m')