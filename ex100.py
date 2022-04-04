#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*valores):
  print(f'foram informados {len(valores)} valores.')
  print(f'dentre os valores {valores}, {max(valores)} é o maior valor.')
  print('-' * 50)
maior(5,4,6,9,8)
maior(4,5,1)
maior(8,17,26,51)
maior(0)