#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    n = int(input('\033[1;33mDigite um valor:\033[m '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('\033[0;31mAdicionado ao final da lista...\033[m')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'\033[0;34mAdicionado na posição\033[m \033[0;32m{pos}\033[m \033[0;34mda lista...\033[m ')
                break
            pos += 1
print('\033[1;37m-=\033[m' * 30)
print(f'\033[0;34mOs valores digitados em ordem foram\033[m \033[0;32m{lista}.\033[m')