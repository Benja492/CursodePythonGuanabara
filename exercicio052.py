n = int(input('Digite um número: '))
t = 0
for i in range(1, n+1):
    if n % i == 0:
        t += 1
print('O número {} foi dívisivel {} vezes.'.format(n, t))
if t > 2:
    print('Logo, ele não é um número primo.')
else:
    print('Logo, ele é um número primo.')