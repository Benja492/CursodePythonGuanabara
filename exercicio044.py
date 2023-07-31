print('{:=^40}'.format('Comercial Reis'))
total = float(input('Digite o valor total das compras: '))
print('''Formas de pagamento:
[ 1 ] Á vista em dinheiro.
[ 2 ] Á vista no cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')
op = int(input('Digite o número da forma de pagamento: '))
if op == 1:
    desconto = total-(total*(90/100))
    print('O valor da compra terá um desconto de 10% (R$ {}) e sairá por {}.'.format(desconto ,total-desconto))
elif op == 2:
    desconto = total - (total * (95 / 100))
    print('O valor da compra tera um desconto de 5% (R$ {}) e sairá por {}.'.format(desconto, total-desconto))
elif op == 3:
    print('O valor da compra será parcelado em 2x e cada parcela sairá por R$ {}.'.format(total/2))
elif op == 4:
    juros = total * (20/100)
    parcelas = int(input('Digite o número de parcelas: '))
    print('O valor da compra terá um juros de 20% (R$ {}) e  será parcelado em {}x, cada parcela sairá por R$ {}.'.format(juros, parcelas, (total+juros)/parcelas))
else:
    print("ERROR 404")
