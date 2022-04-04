#   Exemplo 1
'''def mostralinha():
    print('-' * 30)
mostralinha()
print('Sistema de Aluno')
mostralinha()
print('Sistema do caralho')
mostralinha()'''

#   Exemplo 2
'''def titulo(txt):
    print(txt)
    print('-'*30)
titulo('OLÁ')
titulo('TESTANDO')
titulo('KKKK')'''

#   Exemplo 3

'''def soma(a,b):
    s = a + b
    print(s)

soma(8,2)
soma(3,3)
soma(9,20)'''

#   Exemplo 4

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam}')
contador(2,1,7)
contador(11,12,9,11)
contador(1)    