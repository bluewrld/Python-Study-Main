#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
now = datetime.now()
dados = dict()
dados['nome'] = str(input('nome: ')).strip().title()
nasc = int(input('data de nascimento: '))
dados['idade'] = now.year - nasc
ctps = int(input('carteira de trabalho(0 não tem): '))
if ctps == 0:
    dados['nº carteira de trabalho'] = 'não tem!'
else:
    dados['nº carteira de trabalho'] = ctps
if dados['nº carteira de trabalho'] != 'não tem!':
    dados['ano de contratação'] = int(input('ano de contratação: '))
    dados['aposentadoria'] = (dados['ano de contratação'] + 35) - nasc
    dados['salário'] = float(input('salário: R$ '))
print('=' * 30)
print('      <DADOS PESSOAIS>')
for k, v in dados.items():
    print(f'   - {k}: {v}')