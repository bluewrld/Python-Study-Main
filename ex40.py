#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida. Abaixo de 5.0: REPROVADO, entre 5.0 e 6.9: RECUPERAÇÃO e média 7.0 ou superior: APROVADO.

nota1 = float(input('\033[0;33mPrimeira nota:\033[m '))
nota2 = float(input('\033[0;33mSegunda nota:\033[m '))
media = (nota1 + nota2) / 2
print(f'\u001b[37mTirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}\u001b[m')
if 7 > media >= 5:
    print('\033[1;33mO aluno está em RECUPERAÇÃO.\033[m')
elif media < 5:
    print('\033[1;31mO aluno está REPROVADO.\033[m')
else:
    print('\033[1;32mO aluno está APROVADO.\033[m')