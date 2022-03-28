#Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

preço = float(input('\u001b[32mQual é o preço do produto? R$\u001b[m '))
novo = preço - (preço * 5 /100)
print(f'\u001b[31mO produto que custava R${preço}, com o desconto de 5% vai custar R${novo}\u001b[m')