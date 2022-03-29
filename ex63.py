#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

print('\u001b[37m-\u001b[m'*30)
print('\033[1;30mSequência de Fibonacci\033[m')
print('\u001b[37m-\u001b[m'*30)
numero = int(input('\033[1;35mQuantos termos você quer mostrar?\033[m '))
t1 = 0
t2 = 1
print('\033[0;37m~\033[m'*30)
print(f'\033[0;32m{t1} → {t2}\033[m', end=' ')
cont = 3
while cont <= numero:
    t3 = t1 + t2
    print(f'\033[0;32m→ {t3}\033[m', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('\n\033[1;31mFIM!\033[m')
print('\033[0;37m~\033[m'*30)