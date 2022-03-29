#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('\033[1;33mGERADOR DE PA\033[m')
print('\u001b[37m-=\u001b[m' * 10)
primeiro = int(input('\u001b[35mPrimeiro termo:\u001b[m '))
razao = int(input('\u001b[35mRazão da PA:\u001b[m '))
termo = primeiro
cont = 1 
while cont <= 10:
    print(f'\033[0;32m{termo}\033[m', end=' \033[0;35m->\033[m ')
    termo += razao
    cont += 1
print('\n\u001b[31mFIM!\u001b[m')