#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    numero = int(input('\033[0;32mDigite um número:\033[m '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('\033[1;35mQuer continuar:\033[m \033[1;34m[S/N]\033[m ')).upper().strip()[0]
media = soma / quant
print(f'\033[1;31mVocê digitou {quant} números e a média foi {media}.\033[m')
print(f'\033[1;31mO maior valor foi {maior} e o menor foi {menor}\033[m')