# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista #

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'\033[1;33mDigite um valor para a posição {c}:\033[m ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('\033[1;37m=-\033[m' * 30)
print(f'\033[0;35mVocê digitou os valores\033[m \033[0;32m{listanum}\033[m')
print(f'\033[0;35mO maior valor digitado foi\033[m \033[0;32m{mai}\033[m \033[0;35mnas posições\033[m ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'\033[0;35m{i}...\033[m ', end='')
print()
print(f'\033[0;35mO menor valor digitado foi \033[0;32m{men}\033[m \033[0;35mnas posições\033[m ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'\033[0;35m{i}...\033[m ', end='')
print()