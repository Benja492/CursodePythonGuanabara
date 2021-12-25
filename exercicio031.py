d = float(input('Digite o valor da distância em km: '))
if d <= 200:
    p = d * 0.5
    print('O valor da passagem será de R$ {}.'.format(p))
else:
    p = d * 0.45
    print('O valor da passagem será de R$ {}.'.format(p))