# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1/ b) de 10 até 0, de 2 em 2 e c) uma contagem personalizada.
from time import sleep
def contador(i, f, p):
    print('~' * 30)
    print(f'\033[4mCONTAGEM DE {i} A {f} DE {p} EM {p}\033[m:')
    if p == 0:
        p = 1
    if i > f:
        for c in range(i, f - p, -p):
            if c < f:
                break
            print(c, end=' ')
            sleep(0.3)
    else:
        for c in range(i, f + p, p):
            if c > f:
                break
            print(c, end=' ')
            sleep(0.3)
    print('FIM!')
# programa principal
contador(10, 0, 2)
contador(0, 10, 1)
print('-' * 30)
print('agora é sua vez. personalize sua contagem!')
início = int(input('início: '))
fim = int(input('fim: '))
pulo = int(input('pulo: '))
contador(início, fim, pulo)