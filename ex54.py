#Crie um programa que leia o ano de nascimento de seta pessoas. No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nascimento = int(input('em que ano a pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'e também tivemos {totmenor} pessoas menores de idade.')