#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = dict()
jogos = list()
jogador = str(input('digite o nome do jogador: '))
n = int(input(f'quantas partidas o {jogador} jogou??? '))
s = 0
for c in range(1, n+1):
  j = int(input(f'quantos gols ele marcou no {c}º jogo? '))
  s += j
  jogos.append(j)
dados['jogador:'] = jogador
dados['gols'] = jogos
dados['total:'] = s
print('-='*1500)
print(dados)
print('-='*1500)
for k,v in dados.items():
  print(f'o campo {k} tem o valor de {v} \n')
print('-='*1500)
print(f'o jogador {jogador} jogou {n} partidas.')
for p in range(1, n+1):
    print(f'=> na partida {p} marcou {jogos[p-1]} gols.\n')
print('-='*1500)