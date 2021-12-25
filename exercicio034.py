s = float(input('Digite o valor do salário: '))
if s <= 1250.0:
    print('Seu salário terá um acréscimo de 15% e será de R$ {}.'.format(s+(s*(15/100))))
else:
    print('Seu salário terá um acréscimo de 10% e será de R$ {}.'.format(s + (s * (10 / 100))))