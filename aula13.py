'''lanche = ['Picolé', 'Hambúrguer', 'Pringles']
lanche.append('Batata Frita')
lanche.insert(0, 'Calabresa')
lanche.pop(3)
del lanche[1]
lanche.remove('Calabresa')
print(lanche)
'''
# 1
'''lista = [10,9,7,6,8,5,2,3,4,1]
lista.sort()
print(lista)
lista = [10,9,7,6,8,5,2,3,4,1]
lista.sort(reverse=True)
print(lista)'''

# 2

'''import enum
valores = []
valores.append(1)
valores.append(2)
valores.append(3)

for c, v in enumerate(valores):
    print(f'Na lista {c} encontrei o valor {v}')'''

'''valores = list()


for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na lista {c} encontrei o valor {v}')'''


# Criando cópias

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[:]
b[2] = 10
b.append(11)
print(f'Lista A {a}')
print(f'Lista B {b}')