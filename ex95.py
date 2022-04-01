#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas, B) A média de idade, C) Uma lista com as mulheres e D) Uma lista de pessoas com idade acima da média.
dicio = {}
pessoas = []
media = 0
while True:
    dicio['nome'] = str(input('\nnome: ')).strip().title()
    dicio['idade'] = int(input('idade:'))
    dicio['sexo'] = str(input('sexo: [M/F] ')).strip().upper()[0]
    while dicio['sexo'] != 'M' and dicio['sexo'] != 'F':
        dicio['sexo'] = str(input('decisão inválida! sexo: [M/F]')).upper()[0]
    pessoas.append(dicio.copy())
    decisao = str(input('deseja continunar o cadastro? [S/N] ')).upper()[0]
    while decisao != 'S' and decisao != 'N':
        decisao = str(input('decisão inválida! deseja continuar o cadastro? [S/N] ')).upper()[0]
    if decisao in 'Nn':
        break
print(f'\nA) o total de pessoas cadastradas foram {len(pessoas)}.')
print(f'B) a média das idades são {media/len(pessoas):.2f}.')
print('C) as mulheres cadastradas foram ', end='')
for v in range(0, len(pessoas)):
    media += pessoas[v]['Idade']
    if pessoas[v]['Sexo'] == 'F':
        print(f'{pessoas[v]["Nome"]}', end=' ')
print()
print('D) a lista de pessoas com idade acima da média:')
for v in range(0, len(pessoas)):
    if pessoas[v]['idade'] >= media/len(pessoas):
        print(f'   nome: {pessoas[v]["nome"]}, idade: {pessoas[v]["idade"]}, sexo: {pessoas[v]["sexo"]}')
print()