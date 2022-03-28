#Escreva um  programa que leia dois números inteiros e  compare-os mostrando na tela: O PRIMEIRO VALOR É MAIOR, O SEGUNDO VALOR É MAIOR e NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.

numero1 = int(input('\033[1;33mPrimeiro número:\033[m '))
numero2 = int(input('\033[1;33mSegundo número:\033[m '))
if numero1 > numero2:
    print('\033[1;32mO PRIMEIRO valor é maior.\033[m')
elif numero2 < numero1:
    print('\033[1;32mO SEGUNDO valor é maior.\033[m')
elif numero1 == numero2:
    print('\033[1;31mOs dois valores são IGUAIS.\033[m')