#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. A prestação mensal não pode exceder 30% ou então o empréstimo será negado.

casa = float(input('\033[1;33mValor da casa: R$\033[m '))
salario = float(input('\033[1;33mSalário do comprador: R$\033[m '))
anos = int(input('\033[1;33mQuantos anos de financiamento?\033[m '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'\033[0;34mPara pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}\033[m')
if prestacao <= minimo:
    print('\033[1;32mEmpréstimo pode ser condedido.\033[m')
else:
    print('\033[1;31mEmpréstimo negado.\033[m')