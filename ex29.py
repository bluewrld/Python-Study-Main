#Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80km/h, escreva uma mensagem dizendo que ele foi MULTADO. A multa vai custar R$7,00 por km acima do limite. 

velocidade = float(input('\033[1;33mQual é a velocidade atual do carro?\033[m '))
if velocidade > 80:
    print('\u001b[31mMULTADO! você atingiu o limite permitido, que é de 80km/h.\u001b[m')
    multa = (velocidade-80) * 7
    print(f'\u001b[32mVocê deve pagar uma multa no valor de R${multa:.2f}\u001b[m')
print('\u001b[34mTenha um bom dia! dirija com segurança.\u001b[m')