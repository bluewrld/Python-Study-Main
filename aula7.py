nome = str(input('\033[1;33mQual é seu nome?\033[m ')).strip().upper()
if nome == 'LEANDRO':
    print('\u001b[31mQue nome bonito!\u001b[m')
elif nome == 'ARTHUR' or nome == 'LUCAS' or nome == 'JOSE':
    print('\u001b[34mQue nome comum!!\u001b[m')  
elif nome in 'LUIZA ESTER SABRINNA CAMILY':
    print('\u001b[35mBelo nome feminino!\u001b[m')    
print('\u001b[32mTenha um BOM DIA!\u001b[m')