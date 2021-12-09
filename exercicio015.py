d = int(input('Digite a quantidade de dias alugados: '))
km = float(input('Digite a quantidade de quilometros rodados: '))
v = d*60+km*0.15
print('O valor a ser pago é de R${}.'.format(v))