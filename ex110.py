#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31musuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31musuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('digite um inteiro: ')
n2 = leiafloat('digite um real: ')
print(f'o valor inteiro digitado foi {n1} e o real foi {n2}.')