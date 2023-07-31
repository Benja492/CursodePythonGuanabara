total = 0
aux = 0
produtobarato =" "
while True:
    produto = str(input("Digite o nome do produto: "))
    preço = int(input("Digite o preço do produto: "))
    total += preço
    aux += 1

    if aux == 1:
        valorbarato =  preço
        valorcaro = preço
        produtobarato = produto
        produtocaro = produto
    else:
        if preço < valorbarato:
            valorbarato = preço
            produtobarato = produto
        if preço > valorcaro:
            valorcaro = preço
            produtocaro = produto


    op = str(input('Quer continuar [s / n]:')).lower()
    while op not in "sn":
        op = str(input('Quer continuar [s / n]:')).lower()
    if op =="n":
        break

print(f'O valor total da compra foi R$ {total}.')
print(f'O produto mais caro foi o {produtocaro}, com preço R$ {valorcaro}.')
print(f'O produto mais barato foi o {produtobarato}, com preço R$ {valorbarato}.')
