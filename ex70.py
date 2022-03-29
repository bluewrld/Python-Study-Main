#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra, B) quantos produtos custam mais de R$1000 e C) qual é o nome do produto mais barato. 

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('\033[0;36mNome do produto:\033[m '))
    preco = float(input('\033[0;32mPreço : R$\033[m '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1 
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[1;33mQuer continuar? [S/N]\033[m ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[1;37m{:-^40}\033[m'.format('\033[0;31mFIM DO PROGRAMA\033[m' ))
print(f'\033[1;32mO total da compra foi R${total:.2f}.\033[m')
print(f'\033[1;32mTemos {totmil} produtos custando mais de R$1000.00\033[m')
print(f'\033[1;32mO produto mais barato foi {barato} que custa R${menor:.2f}\033[m')