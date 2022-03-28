#Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO.

from datetime import date
ano = int(input('\033[1;33mQue ano quer analisar? Coloue o para analisar o ano atual:\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\u001b[36mO ano {ano} é BISSEXTO!\u001b[m')
else:
    print(f'\u001b[36mO ano {ano} NÃO É BISSEXTO!\u001b[m')    