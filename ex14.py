#Ecreva um programa que converta uma temperatura digitada em °C e converta para °F:

celsius = float(input('\u001b[32mInforme a temperatura em °C:\u001b[m '))
fahrenheit = (9*celsius/5) + 32
print(f'\u001b[36mA temperatura de\u001b[m \u001b[31m{celsius}°c\u001b[m \u001b[36mcorresponde a\u001b[m \u001b[31m{fahrenheit}°f\u001b[m ')