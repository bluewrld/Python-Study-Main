n1 = float(input('\033[1;33mDigite a primeira nota:\033[m '))
n2 = float(input('\033[1;33mDigite a segunda neta:\033[m '))
m = (n1 + n2)/2
print('\033[0;35mA sua média foi\033[m \u001b[37m{:.1f}\u001b[m'.format(m))
print('\033[0;32mPARABÉNS\033[m' if m >=6 else '\033[1;31mESTUDE MATS!\033[m')