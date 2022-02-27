n1 = int(input("Digite um numero: "))
print("O dobro de {} vale {}.".format(n1, (n1 * 2)))
print(
    "O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(
        n1, (n1 * 3), n1, (n1 ** (1 / 2))
    )
)
