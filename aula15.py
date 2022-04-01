'''nomes = {'nome': 'Leandro', 'idade': '19'}
# print(f'O {nomes["nome"]} tem {nomes["idade"]} anos')
# print(nomes.values())
for k, v in nomes.items():
    print(f'{k} = {v}')'''

# Example 2
'''brasil = []
rj = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
ba = {'UF': 'Bahia', 'Sigla': 'BA'}
brasil.append(rj)
brasil.append(ba)
print(brasil[1])'''

# Example 3
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')