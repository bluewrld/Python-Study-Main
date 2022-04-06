from datetime import date

def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa Principal
nasc = int(input('Em que ano você nasceu? '))        
print(voto(nasc))