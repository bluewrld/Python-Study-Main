# Exemplo 1
'''pessoas = list()
pessoas.append('Leandro')
pessoas.append(40)
dados = list()
print(pessoas)
dados.append(pessoas[:])
pessoas[0] = 'BlueWRLD'
pessoas[1] = 20
print(pessoas)'''

# Exemplo 2
'''pessoas = [['BlueWRLD', 20], ['Junqueira', 22], ['Mama', 40], ['Papa', 61]]
print(pessoas[0][1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idades')'''

# Exemplo 3
pessoas = list()
dados = list()
totmen = totmaior = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)    

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmen} menores de idade e {totmaior} maior de idade')      