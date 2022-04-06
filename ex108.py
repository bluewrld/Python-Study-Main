#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
from time import sleep
#função que carrega o menu
def sistema():
    tit ='SISTEMA DE AJUDA PYHELP'
    sleep(0.5)
    print('\33[42m-' * (len(tit) + 4))
    print(f'  {tit}')
    print('-'*(len(tit) + 4),end='  '*62)
    print('\33[m')
    sleep(0.5)
    hlp=str(input('função ou Biblioteca>')).lower()
    if hlp in 'fimendexitquitbye':
        tit = 'ATÉ LOGO'
        print('\33[41m-' * (len(tit) + 4))
        print(f'  {tit}')
        print('-' * (len(tit) + 4), end='  ' * 69)
        print('\33[m')
    else:
        ajuda(hlp)
        flush=True
        sleep(0.5)
#funcao que acessa o intective help
def ajuda(sos):
    tit = str('ACESSANDO MANUAL DO COMANDO '+ sos)
    print('\33[46m-' * (len(tit) + 4))
    print(f'  {tit}')
    print('-' * (len(tit) + 4), end='  ' * 62)
    print('\33[m')
    sleep(0.8)
    print('\33[0;47m','     ')
    help(sos)
    print('     ')
    sistema()
#programa principal
sistema()