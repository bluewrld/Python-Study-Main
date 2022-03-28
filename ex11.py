#Faça um programa que leia a largura e altura de uma parede em metros. calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m².

larg = float(input('\u001b[32mLargura da parede:\u001b[m '))
alt = float(input('\u001b[32mAltura da parede:\u001b[m '))
área = larg*alt
print(f'\u001b[35mSua parede tem a dimensão de {larg*alt} em {área}m²\u001b[m')
tinta = área / 2
print(f'\u001b[35mPara pintar essa, parede você precisará de {tinta} litros de tinta\u001b[m ')