s = 0
c = 0
for i in range(1, 501):
    if (i%2 == 1) and (i % 3 == 0):
        c = c + 1
        s = s + i
print('A soma dos {} valores é igual a {}.'.format(c,s))