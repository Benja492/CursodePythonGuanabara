import math
n = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('Ângulo : {}°\nSeno: {:.2f}°\nCosseno: {:.2f}°\nTangente: {:.2f}°'.format(n, s, c, t))