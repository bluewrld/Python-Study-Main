#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
nome1 = str(input('\u001b[32mPrimeiro aluno:\u001b[m '))
nome2 = str(input('\u001b[32mSegundo aluno:\u001b[m '))
nome3 = str(input('\u001b[32mTerceiro aluno:\u001b[m '))
nome4 = str(input('\u001b[32mQuarto aluno:\u001b[m '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'\u001b[34mO aluno escolhido foi\u001b[m \033[1;31m{escolhido}\033[m')