#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando o laço FOR.
numero = int(input('\033[1;33mDigite um número para ver sua tabuada:\033[m '))
print('\u001b[37m-=-\u001b[m' * 20)
for c in range(1, 11):
    print(f'\033[1;35m{numero} x {c} = {numero*c}\033[m')
print('\033[1;32mPrograma Finalizado!\033[m')    
print('\u001b[37m-=-\u001b[m' * 20)