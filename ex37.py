#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO: 1 para BINÁRIO, 2 para OCTAL e 3 para HEXADECIMAL.

numero = int(input('\033[1;33mDigite um número inteiro:\033[m '))
print('''\033[1;34mEscolha uma das bases para conversão:
[ 1 ] Conveter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL\033[m''')
opcao = int(input('\033[1;33mDigite a sua opção:\033[m '))
if opcao == 1:
    print(f'\033[0;34m{numero}\033[m \033[0;35mConvertido para BINÁRIO é igual a\033[m {bin(numero)}')
elif opcao == 2:
    print(f'\033[0;34m{numero}\033[m \033[0;35mConvertdido para OCTAL é igual a\033[m {oct(numero)}')
elif opcao == 3:
    print(f'\033[0;34m{numero}\033[m \033[0;35mConvertido para HEXADECIMAL é igual a\033[m {hex(numero)}')  
else:
    print('\033[1;31mOpção inválida, tente novamente.\033[m')