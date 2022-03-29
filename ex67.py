#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    numero = int(input('\033[1;35mQuer ver a tabuada de qual valor?\033[m '))
    print('\u001b[37m-\u001b[m' * 30)
    if numero < 0:
        break
    for c in range (1, 11):
        print (f'\u001b[34m{numero} x {c} = {numero*c}\u001b[m')
    print('\u001b[37m-\u001b[m' * 30)
print('\u001b[31mPrograma Finalizado!\u001b[m')