import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hi))