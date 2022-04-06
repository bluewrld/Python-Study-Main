#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(numero, show = False):
    fat = 1
    for cont in range(numero, 0, -1):
        if show:
            print(f'{cont}', end = ' ')
            if cont > 1:
                print('X', end = ' ')
            else:
                print('=', end = ' ')
        fat *= cont
    return fat
# Programa principal...
numero = int(input('digite um número: '))
mostra = str(input('digite S para mostrar o fatorial ou N para mostra apenas o resultado: ')).strip().upper()
if mostra == 'S':
    show = True
else:
    show = False
print(fatorial(numero, show = show))