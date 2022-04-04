#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(a):
    from datetime import date
    hoje = date.today().year
    if hoje-a >= 18 and hoje-a <= 65:
        print('VOTO OBRIGATÓRIO')
    elif hoje-a < 16:
        print('VOTO NEGADO')
    else:
        print('VOTO OPCIONAL')
ano = int(input('digite o ano (aaaa): '))
voto(ano)