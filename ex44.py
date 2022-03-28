#Elabore um programa ue calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento. À vista: 10% de desconto; em ate 2x no cartão: preço normal; à vista no cartão: 5% de desconto e 3x ou mais vezes no cartão: 20% de juros.

print('\u001b[37m{:=^40}\u001b[37m'.format(' \033[0;35mSUPERMERCADO REIS\033[m '))
preco = float(input('\u001b[32mPreço das compras: R$\u001b[m '))
print('''\u001b[33m
FORMAS DE PAGAMENTO
[1] à vista
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão\u001b[m
''')
opcao = int(input('\u001b[36mQual é a opção?\u001b[m '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print (f'\033[1;34mSua compra será parcelada de 2x de R${parcela:.2f}\033[m')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('\033[1;33mQuantas parcelas?\033[m '))
    parcela = total / totparc
    print (f'\033[1;35mSua compra será parcelada de {totparc}x de R${parcela:.2f} COM JUROS.\033[m')
print(f'\033[1;35mSua compra de R${preco:.2f} vai custar R${total:.2f} no final.\033[m')