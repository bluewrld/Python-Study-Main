import time
nome = str(input('\033[0;32mDigite seu nome completo:\033[m ')).strip()
print('\033[0;33mAnalisande seu nome...\033[m')
time.sleep(2)
print('\033[1;34mSeu nome em maiúsculas é\033[m \033[1;31m{}\033[m'.format(nome.upper()))
time.sleep(2)
print('\033[1;34mSeu nome em minúsculas é\033[m \033[1;31m{}\033[m'.format(nome.lower()))
time.sleep(2)
print('\033[1;34mSeu nome tem ao todo\033[m \033[1;31m{}\033[m \033[1;31mletras\033[m'.format(len(nome) , - nome.count(' ')))
time.sleep(2)
#print('Seu primeiro nome tem {} letras'.tormat (nome, find(" '))
separa = nome.split()
print('\033[1;33mSeu primeiro nome é\033[1m \033[1;31m{}\033[m \033[1;33me ele tem\033[m \033[1;31m{}\033[m \033[1;33mletras\033[m'. format(separa[0], len(separa[0])))