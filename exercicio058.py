from random import randint
n = randint(0,10)
e = int(input('Adivinhe um número entre 0 e 10: '))
t = 0
while e != n:
    e = int(input('Adivinhe um número entre 1 e 10: '))
    t += 1
print('Você acertou!')
print('Voce tentou {} vezes.'.format(t+1))