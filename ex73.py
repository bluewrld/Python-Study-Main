#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times, b) Os últimos 4 colocados, c) Times em ordem alfabética e d) Em que posição está o time da Chapecoense.

times = ('corinthians', 'palmeiras', 'santos', 'grêmio',
        'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
        'atlético', 'botafogo', 'atlético-PR', 'bahia',
        'são paulo', 'fluminense', 'sport recife',
        'EC vitória', 'coritiba', 'avaí', 'ponte preta',
        'atlético-GO')
print('\u001b[37m-=\u001b[m' * 15)
print(f'\033[1;31mLista de times do brasileirão: {times}\033[m')
print('\u001b[37m-=\u001b[m' * 15)
print(f'\033[1;34mOs 5 primeiros são: {times[0:5]}\033[m')
print('\u001b[37m-=\u001b[m' * 15)
print(f'\033[1;32mOs 4 últimos são: {times[-4:]}\033[m')
print('\u001b[37m-=\u001b[m' * 15)
print(f'\033[0;36mTimes em ordem alfabética: {sorted(times)}\033[m')
print('\u001b[37m-=\u001b[m' * 15)
print(f'\033[0;31mO chapecoense está na {times.index("chapecoense")+1}ª posição.\033[m')