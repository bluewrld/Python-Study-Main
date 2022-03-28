#Faça um programa que leia um frase pelo teclado e mostre: quantas vezes a aparece a letra A, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('\033[1;33mDigite uma frase:\033[m ')).upper().strip()
print(f'\033[0;35mA letra A aparece {frase.count("A")} vezes na frase\033[m')
print(f'\033[0;35mA primeira letra A apareceu na posição {frase.find("A")+1}\033[m')
print(f'\033[0;35mA última letra A apareceu na posição {frase.rfind("A")+1}\033[m')