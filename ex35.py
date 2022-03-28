#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('\u001b[37m-=-\u001b[m'* 20)
print('\033[1;35mAnalisador de Triângulos\033[m')
print('\u001b[37m-=-\u001b[m' * 20)
r1 = float(input('\033[1;33mPrimeiro segmento:\033[m '))
r2 = float(input('\033[1;33mSegundo segmento:\033[m '))
r3 = float(input('\033[1;33mTerceiro segmento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;34mOs segmentos acima PODEM formar um triângulo.\033[m')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM formar um triângulo.\033[m ')