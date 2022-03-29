# Estrutura de repetição while #

n = 1
par = impar = 0
while n != 0:
    n = int(input('\033[0;34mDigite um valor:\033[m ' '\033[0;31m0 PARA PARAR\033[m '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else: 
            impar += 1
print(f'\033[0;35mVocê digitou\033[m \033[0;32m{par}\033[m \033[0;35mnúmeros pares e\033[m \033[0;32m{impar}\033[m \033[0;35mnúmeros ímpares\033[m')                