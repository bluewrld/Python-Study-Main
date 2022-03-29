#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quize', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    numero = int(input('\033[1;34mDigite um número entre 0 e 20:\033[m '))
    if 0 <= numero <= 20:
        break
    print('\033[1;31mTente novamente.\033[m', end=' ')
print(f'\033[0;35mVocê digitou o número:\033[m \033[0;32m{cont[numero]}\033[m')