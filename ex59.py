#Crie um programa que leia dois valores e mostre o menu: [1]somar, [2]multiplicar, [3]maior, [4]novos números, [5]sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
import time
numero1 = int(input('\u001b[35mPrimeiro valor:\u001b[m '))
numero2 = int(input('\u001b[35mSegundo valor:\u001b[m '))
opcao = 0
while opcao != 5:
    print('\033[1;37m=-=\033[m' * 10)
    print('''    \u001b[37m[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\u001b[m''')
    print('\033[1;37m=-=\033[m' * 10)
    opcao = int(input('\033[1;31m>>>>> Qual é a sua opção?\033[m '))
    if opcao == 1:
        soma = numero1 + numero2
        print(f'\033[0;35mA soma entre\033[m \033[1;32m{numero1}\033[m \033[0;35me\033[m \033[1;32m{numero2}\033[m \033[0;35mé\033[m \033[1;32m{soma}.\033[m')
    elif opcao == 2:
        produto = numero1 * numero2
        print(f'\033[0;35mO resultado de\033[m \033[0;32m{numero1}\033[m \033[0;35mx\033[m \033[0;32m{numero2}\033[m \033[0;35mé\033[m \033[0;32m{produto}\033[m')
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f'\033[0;35mEntre\033[m \033[0;32m{numero1}\033[m \033[0;35me\033[m \033[0;32m{numero2}\033[m \033[0;35mo maior valor é\033[m \033[0;32m{maior}\033[m')
    elif opcao == 4:
        print('\033[1;33mInforme os números novamente:\033[m ')
        numero1 = int(input('\u001b[37mPrimeiro valor:\u001b[m '))
        numero2 = int(input('\u001b[37mSegundo valor:\u001b[m '))
    elif opcao == 5:
        print('\033[1;32mFinalizando...\033[m')
        time.sleep(1)
    else:
        print('\033[0;31mOpção inválida, tente novamente.\033[m')
print('\033[1;32mPogama Finalizado!\033[m')