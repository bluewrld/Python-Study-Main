#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade; até 9 anos de idade: MIRIM; até 14 anos: INFANTIL; até 19: JUNIOR; até 25: SENIOR; acima: MASTER.

from datetime import date
atual = date.today().year
nascimento = int(input('\033[0;33mAno de nascimento:\033[m '))
idade = atual - nascimento
print(f'\u001b[34mO atleta tem\u001b[m \u001b[32m{idade}\u001b[m \u001b[34manos\u001b[m')
if idade <= 9:
    print('\u001b[34mClassificação: MIRIM\u001b[m')
elif idade <= 14:
    print('\u001b[35mClassificação: INFANTIL\u001b[m')
elif idade <= 19:
    print('\u001b[33mClassificação: JUNIOR\u001b[m')
elif idade <= 25:
    print('\u001b[36mClassificação: SENIOR\u001b[m')
else:
    print('\u001b[31mClassificação: MASTER\u001b[m')