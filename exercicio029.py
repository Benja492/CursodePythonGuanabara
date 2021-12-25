v = float(input('Digite a velocidade do carro: '))
m = (v-80.0)*7
if v > 80.0:
    print('Você será multado!! O valor da multa é R$ {}.'.format(m))
else:
    print('Você não será multado.')