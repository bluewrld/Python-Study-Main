#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para valores superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('\033[0;33mQual é o salário do funcionário?\033[m \033[0;32mR$\033[m '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'\u001b[34mQuem ganhava\u001b[m \033[0;32mR${salario:.2f}\033[m \u001b[34mpassa a ganhar\u001b[m \u001b[32mR${novo:.2f}\u001b[m \u001b[34magora.\u001b[m ')