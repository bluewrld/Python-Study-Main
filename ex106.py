#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaint(txt):
     while True:
          print('-' *45)
          n = str(input(txt))
          if n.isnumeric():
               print(f'ovcê acabou de digitar o número {n}')
               break
          else:
               print('ERRO! digite um número inteiro válido.')
#programa principal
n = leiaint('digite um número:')