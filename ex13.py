#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salário = float(input('\u001b[32mQual é o salário do funcionário? R$\u001b[m '))
novo = salário + (salário * 15 / 100)
print(f'\u001b[33mUm funcionário que recebia R${salário:.2f}, com 15% de aumento, passa a receber R${novo:.2f}\u001b[m')