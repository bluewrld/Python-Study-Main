#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('\033[0;32mEm que cidade você nasceu?\033[m ')).strip()
print(cidade[:5].upper() == 'SANTO')