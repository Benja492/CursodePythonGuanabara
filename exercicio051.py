p = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
d = p + (10-1) * r
for i in range(p, d+ r, r):
    print('{} '.format(i), end='➝ ')
print('fim')