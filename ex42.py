#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado. EQUILÁTERO: todos são iguais; ISÓCELES: dois lados iguais; ESCALENO: todos os lados diferentes.

print('\u001b[37m=-\u001b[m'* 20)
print('\u001b[34mAnalisador de Triângulos\u001b[m')
print('\u001b[37m-=\u001b[m' * 20)
r1 = float(input('\033[0;32mPrimeiro segmento:\033[m ' ))
r2 = float(input('\033[0;32mSegundo segmento:\033[m '))
r3 = float(input('\033[0;32mTerceiro segmento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;35mOs segmentos acima PODEM formar um triângulo\033[m ', end='')
    if r1 == r2 == r3:
        print('\033[1;37mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;37mESCALENO!\033[m')
    else:
        print('\033[1;37mISÓCELES!\033[m')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM formar um triângulo.\033[m ')