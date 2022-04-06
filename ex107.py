#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de notas, A maior nota, A menor nota, A média da turma e A situação (opcional).
inf = {}
def dados(*notas, s=False):
    '''
    -> funcao para analisar a situacao de varios alunos.
    :arg1: notas = quantas notas voce quiser.
    :arg2: s = situacao dos alunos.
    :return: as informacoes e situacao de varios alunos.
'''
    m = 0
    inf['total'] = len(notas)
    inf['maior'] = max(notas)
    inf['menor'] = min(notas)
    inf['média'] = sum(notas)/len(notas)
    if s:
        if inf['média'] >= 10:
            inf['situação'] = 'boa'
        elif inf['média'] >= 5:
            inf['situação'] = 'razoável'
        else:
            inf['situação'] = 'ruim'
    else:
        inf['média'] = sum(notas)/len(notas)
from random import randint
dados(randint(1, 15),randint(1, 15),randint(1, 15), s=True)
print(inf)