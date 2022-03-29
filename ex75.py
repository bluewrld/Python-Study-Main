#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9, B) Em que posição foi digitado o primeiro valor 3 e C) Quais foram os números pares.

numero = (int(input('\033[1;36mDigite um número:\033[m ')),
          int(input('\033[1;36mDigite outro número:\033[m ')),
          int(input('\033[1;36mDigite mais um número:\033[m ')),
          int(input('\033[1;36mDigite o último número:\033[m ')))
print(f'\033[0;35mVocê digitou os valores\033[m {numero}')
print(f'\033[0;35mO valor 9 apareceu\033[m \033[1;34m{numero.count(9)}\033[m vezes.\033[m')
if 3 in numero:
    print(f'\033[0;35mO valor 3 apareceu na\033[m \033[1;34m{numero.index(3)+1}ª posição.\033[m')
else:
    print('\033[0;35mO valor 3 não foi digitado em nenhuma posição.\033[m')
print('\033[0;35mOs valores digitados foram\033[m ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')