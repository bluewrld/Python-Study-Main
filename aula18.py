# Tratamento de Erros e Exceções

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problem com os tigos de dados que você digitou. ')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('0 usuário pceferiu não infernar os dados !')
except Exception as erro:
    print(f'0 erro encontrado foi {erro._cause_} ')
else:
    print(f'0 resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
    