#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
nome1 = str(input('\u001b[32mPrimeiro aluno:\u001b[m '))
nome2 = str(input('\u001b[32mSegundo aluno:\u001b[m '))
nome3 = str(input('\u001b[32mTerceiro aluno:\u001b[m '))
nome4 = str(input('\u001b[32mQuarto aluno:\u001b[m '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('\u001b[34mA ordem de apresentação será\u001b[m ')
print(f'\033[1;31m{lista}\033[m')