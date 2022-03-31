#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = []
while True:
    n = str(input('qual o nome do aluno? ')).strip().title()
    note = float(input('qual a nota do aluno? '))
    note2 = float(input('qual a segunda nota do aluno? '))
    media = (note + note2) / 2
    boletim.append([n, [note, note2], media])
    perg = str(input('deseja resgistrar outro aluno? [S/N] ')).strip().upper()[0]
    if perg not in 'SN':
        print('\033[33mnão entendi...', end=' ')
        perg = str(input('\033[mresponda com [S/N]: ')).strip().upper()[0]
        if perg == 'N':
            break
    if perg == 'N':
        break
print('-=' * 5, 'BOLETIM', '=-' * 5)
print(f'{"Nº":<4}{"NOME ":<10}{"NOTA":>8}')
print('-' * 25)
for i, aluno in enumerate(boletim):
   print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8}')
while True:
    continuar = int(input('digite o número do aluno para ver a nota (999 para parar): '))
    if continuar == 999:
        break
    if continuar <= len(boletim):
        print(f'as notas do aluno {boletim[continuar][0]} são {boletim[continuar][1]}')