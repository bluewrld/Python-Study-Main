#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar. (considere US$1,0 = R$5,33)

real = float(input('\u001b[32mQuanto dinheiro você tem na carteira:\u001b[m '))
dolar = real / 5.33
print(f'\u001b[36mcom R${real} você pode comprar US${dolar}\u001b[m')