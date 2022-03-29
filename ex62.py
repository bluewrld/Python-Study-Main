#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('\u001b[36mGERADOR DE PA\u001b[m')
print('\u001b[37m-=\u001b[m' * 10)
primeiro = int(input('\u001b[35mPrimeiro termo:\u001b[m '))
razao = int(input('\u001b[35mRazão da PA:\u001b[m '))
termo = primeiro
cont = 1 
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'\033[1;35m{termo}\033[m', end=' \033[0;32m->\033[m ')
        termo += razao
        cont += 1
    print('\n\033[0;37mPAUSA!\033[m')
    mais = int(input('\u001b[35mQuantos termos você quer mostrar a mais?\u001b[m '))
print(f'\033[1;31mProgressão finalizada com\033[m \033[0;32m{total}\033[m \033[1;31mtermos mostrados.\033[m')