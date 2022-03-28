#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('\u001b[33mPrimeiro valor:\u001b[m '))
b = int(input('\u001b[33mSegundo valor:\u001b[m '))
c = int(input('\u001b[33mTerceiro valor:\u001b[m '))
#V  erificando que é menor
menor = a 
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
#Verificando que é maior
maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print (f'\033[0;35mO menor valor digitdo foi\033[m \033[0;31m{menor}\033[m')
print(f'\033[0;35mO maior valor digitado foi\033[m \033[0;31m{maior}\033[m')