n = 0
soma = 0
contador = -1
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um valor: '))
print('O total de números digitados foi {} e a soma é {}'.format(contador, soma))
