a = int(input('Digite a altura da parede em metros: '))
c = int(input('Digite o comprimento da parede em metros: '))
ap = a*c
tn = ap/2
print('Precisa-se de {} latas de tinta para pintar a parede de {} m².'.format(tn,ap))