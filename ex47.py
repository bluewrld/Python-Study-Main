#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for n in range(2, 51, 2):
    print(' ', end='')
    print(f'\u001b[32m{n}\u001b[m', end=' ')
print('\n\033[0;31mPrograma Finalizado!\033[m')