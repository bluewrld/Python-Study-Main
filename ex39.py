#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: se ele ainda vai se alistar ao serviço militar, se é a hora ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date 
atual = date.today().year
nasc = int(input('\033[0;34mAno de nascimento:\033[m '))
idade = atual - nasc
print(f'\033[0;33mQuem nasceu em {nasc} tem {idade} anos em {atual}\033[m')
if idade == 18:
    print('\033[0;31mVocê tem que se alistar IMEDIATAMENTE!\033[0;32m')
elif idade < 18:
    saldo = 18 - idade
    print(f'\033[0;36mAinda faltam {saldo} para você se alistar.\033[m')
elif idade > 18:
    saldo = idade - 18
    print(f'\033[1;31mVocê já deveria ter se alistado há {saldo} anos!\033[m')