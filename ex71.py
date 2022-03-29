#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('\u001b[37m=\u001b[m'*30)
print('{:^30}'.format('\033[0;34mBANCO REIS\033[m'))
print('\u001b[37m=\u001b[m'*30)
valor = int(input('\033[0;33mQue valor você quer sacar? R$\033[m '))
total = valor
cedulas = 50
totced = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totced += 1
    else:
        if totced > 0:
            print(f'\033[0;35mTotal de\033[0m \033[0;31m{totced}\033[m \033[0;35mcédulas de R$\033[m\033[0;31m{cedulas}\033[m ')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totced = 0
        if total == 0:
            break
print('\u001b[37m=\u001b[m'*30) 
print('\u001b[34mVolte sempre ao BANCO REIS! tenha um bom dia.\u001b[m')