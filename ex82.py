#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numero = list()
pares = list()
ímpares = list()
while True:
    numero.append(int(input('\033[0;33mDigite um número:\033[m ')))
    resp = str(input('\033[1;33mQuer continuar: [S/N]\033[m '))
    if resp in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('\033[1;37m-=\033[m' * 30)
print(f'\033[0;34mA lista completa é\033[m \033[0;35m{numero}\033[m')
print(f'\033[0;34mA lista de pares é\033[m \033[0;35m{pares}\033[m')
print(f'\033[0;34mA lista de ímpares é\033[m \033[0;35m{ímpares}\033[m')