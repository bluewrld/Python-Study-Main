n = int(input('\033[0;32mDigite um valor:\033[m '))
print('\033[0;35mO dobro de {} vale {}.\033[m'.format(n, (n*2)))
print('\033[0;31mO triplo de {} vale {}.\033[m \033[0;34m\nA raiz quadrada de {} é igual a {:.2f}.\033[m'.format(n, (n*3), n, pow(n, (1/2))))