preço = float(input("O Valor do produto: R$"))
novo = preço - (preço * 5 / 100)
print(
    "O valor do produto que custava R${}, na promoção com desconto de 5% vai custar R${}".format(
        preço, novo
    )
)
