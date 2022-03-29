#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos, B) quantos homens foram cadastrados e C) quantas mulheres tem menos de 20 anos.

tot18 = totH = totM20 = 0
while True:
    idade = int(input('\033[0;31mIdade:\033[m '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[0;35mSexo:\033[m \033[1;37m[\033[m\033[0;34mM\033[m\033[1;37m/\033[m\033[0;35mF\033[m\033[1;37m]\033[m ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[1;37mQuer continuar?\033[m \033[0;32m[S/N]\033[m ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\033[0;34mTotal de pessoas com mais de 18 anos:\033[m {tot18}')
print(f'\033[0;34mAo todo temos {totH} homens cadastrados.\033[m')
print(f'\033[1;35mE temos {totM20} mulheres com menos de 20 anos.\033[m')