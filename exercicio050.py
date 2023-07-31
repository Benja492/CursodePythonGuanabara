s = 0
c = 0
for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        c += 1
print('Você digitou {} números pares e a soma deles é {}.'.format(c, s))
