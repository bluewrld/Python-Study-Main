#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input('\033[0;32mUma distância em metros:\033[m '))
cm = medida*100
mm = medida*1000
print(f'\033[1;33mA medida de\033[m \033[1;35m{medida}\033[m \033[1;33mCorresponde a\033[m \033[1;35m{cm}cm\033[m \033[1;33me\033[m \033[1;35m{mm}mm\033[m')