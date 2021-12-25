a = int(input('Digite o ano em questão: '))
d = int(input('Digite a quantidade de dias que ele tem: '))
if d > 365:
    print('O ano de {} é um ano bissexto.'.format(a))
else:
    print('O ano de {} não é um ano bissexto.'.format(a))
