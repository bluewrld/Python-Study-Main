#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela. abaixo de 18.5: ABAIXO DO PESO; entre 18.5 e 25: PESO IDEAL; 25 até 30: SOBREPESO; 30 até 40: OBESIDADE e acima de 40: OBESIDADE MÓRBIDA.

peso = float(input('\033[0;32mQual é o seu peso? (kg)\033[m '))
altura = float(input('\033[0;32mQual é a sua altura? (m)\033[m '))
imc = peso / (altura ** 2)
print(f'\033[0;35mO IMC dessa pessoa é de\033[m \033[1;37m{imc:.1f}\033[m')
if imc < 18.5:
        print('\033[0;35mVocê está ABAIXO DO PESO normal.\033[m')
elif 18.5 <= imc < 25:
    print('\033[1;34mVocê está na faixa de peso NORMAL.\033[m') 
elif 25 <= imc < 30:
    print('\033[1;31mVocê está em SOBREPESO.\033[m')
elif 30 >= imc < 40:
    print('\033[1;31mVocê está em OBESIDADE.\033[m')
elif imc >= 40:
   print('\033[1;31mVocê está em OBESIDADE MÓRBIDA.\033[m')   