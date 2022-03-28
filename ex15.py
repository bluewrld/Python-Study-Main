#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

dias = int(input('\u001b[32mQuantos dias alugados?\u001b[m '))
km = float(input('\u001b[32mQuantos km rodados?\u001b[m '))
pago = (dias * 60) + (km * 0.15)
print(f'\u001b[35mO total a pagar é de\u001b[m \u001b[31m{pago:.2f}\u001b[m')