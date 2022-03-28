#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('\033[1;33mQual é a distância da sua viagem?\033[m '))
print(f'\u001b[34mVocê está prestes a fazer uma viagem de\u001b[m \u001b[32m{distancia}km.\u001b[m ')
if distancia <= 200:
    preço = distancia * 0.50 
else:
    preço = distancia * 0.45
print(f'\u001b[32mO preço de sua passagem será de\u001b[m \u001b[31mR${preço:.2f}\u001b[m')