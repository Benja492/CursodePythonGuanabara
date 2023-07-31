from math import factorial
n = int(input('Digite um número para ser calculado seu fatorial: '))
f = factorial(n)
c = n
print('{}! ='.format(n), end=' ')
while c > 1:
    print('{} x'.format(c), end=' ')
    c -=1
print('1', end=' ')
print('= {}'.format(f))
