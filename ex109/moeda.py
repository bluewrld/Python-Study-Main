# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), doobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco = 0, formato = False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')