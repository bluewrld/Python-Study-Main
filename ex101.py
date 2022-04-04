#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import sample
def sorteia(x):
    x += sample(range(1, 100), 5)[:] 
    return x
def somapar(s):
    s = sum([q for q in s if q % 2 == 0])
    return s
numeros = []
print(f'números sorteados: {sorteia(numeros)}'
      f'\nsoma dos pares na lista: {somapar(numeros)}')