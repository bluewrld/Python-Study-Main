#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
resutados = dict()
jogadores = list()
print('Valores sorteados:')
for c in range(0, 4):
    n = randint(1, 6)
    resutados['jogador'+str(c+1)] = n
    jogadores.append(n)
    sleep(0.5)
    print(f'o {"jogador"+str(c+1)} tirou {n}')
jogadores.sort(reverse= True)
jogar = 't'
print('ranking dos jogadores:')
for p in range(0,4):
    print(f'{p+1}º Lugar: ', end='')
    for k, v in resutados.items():
        if v == jogadores[p] and jogar != k:
            sleep(0.1)
            print(k,'com',v)
            jogar = k
            break