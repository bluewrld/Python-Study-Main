#Desenvolva um programa que leia seis números inteiros e mostre a soma somente daqueles que forem pares. Se o valor digitado for ímpar. desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c} valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')