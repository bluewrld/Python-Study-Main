#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from time import sleep
resp = None
gols = []
dado = []
while resp != 'N':
    nome = str(input('nome do jogador: '))
    quantidade = int(input(f'quantidade de partidas de {nome}: '))
    for c in range(quantidade):
        gol = int(input(f'quantidade de gols na {c + 1}º partida: '))
        gols.append(gol)
    info = {'nome': nome, 'quantidade': quantidade, 'gols': gols[:], 'soma': sum(gols)}
    dado.append(info.copy())
    info.clear()
    gols.clear()
    resp = str(input('quer continuar [S/N]:')).upper()[0]
print('-=' * 30)
print(f'{"cod":<4}{"nome":<11}{"gols":<15} total')
print('-' * 38)
for n, i in enumerate(dado):
    print(f'{n:<4}{i["nome"]:<11} {str(i["gols"]):<18}{i["soma"]}')
print('-' * 38)
c = 1
while True:
    detalhes = int(input('de qual jogador quer ver o levantamento?(999 para parar)\n'))
    if detalhes == 999:
        print('finalizando...')
        sleep(1)
        break
    elif detalhes <= len(dado) - 1:
        c = 0
        print(f'-- levantamento do jogador {dado[detalhes]["nome"]}:')
        for cp in dado[detalhes]["gols"]:
            print(f' {"no":>5} jogo {c} fez {cp} gols')
            c += 1
        print(f'no total {dado[detalhes]["soma"]} gols')
    else:
        print(f'não existe jogador com o número {detalhes}! por favor digite novamente:')
print('<<< VOLTE SEMPRE >>>')