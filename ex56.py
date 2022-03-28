#Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa mostre: A média de idade do grupo, qual é o nome do homem mais velho, quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p} PESSOA ------')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'a média de idade do grupo é de {mediaidade} anos.')
print(f' o homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'ao todo são {totmulher20} com menos de 20 anos.')