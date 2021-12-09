import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.sqrt((co*co)+(ca*ca))
print('A hipotenusa dos catetos {} e {} é {:.2f}.'.format(co, ca, h))