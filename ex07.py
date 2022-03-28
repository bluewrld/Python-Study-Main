n1 = float(input('\033[0;32mPrinmira nota do aluno:\033[m '))
n2 = float(input('\033[0;32mSegunda nota do aluno:\033[m '))
média = (n1 + n2) / 2
print('\033[1;33mA média entre\033[m \033[1;34m{:.1f}\033[m \033[1;33me\033[m \033[1;35m{:.1f}\033[m \033[1;33mé igual a\033[m \033[0;31m{:.1f}\033[m'.format(n1, n2, média))