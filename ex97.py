#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

print('=' * 40)
print(f'{"área do Terreno":^40}')
print('=' * 40)
def area(l, c):
    a = l * c
    print(f'o seu terreno de {l}x{c} tem uma área de {a:.1f}m².')
l = float(input('digite a largura do terreno: '))
c = float(input('digite o comprimento do terreno: '))
area(l, c) 