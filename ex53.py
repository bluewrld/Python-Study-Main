#Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.

frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'o inverso de {junto} é {inverso}.')
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('a frase digitada não é um palíndromo!')