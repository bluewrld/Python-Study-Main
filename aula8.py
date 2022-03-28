s = 0
for c in range(0, 4):
    n = int(input('\033[0;32mDigite um valor:\033[m '))
    s += n
print(f'\033[0;31mA somatória de todos os números foi {s}\033[m')  