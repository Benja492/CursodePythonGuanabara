n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 < n2 and n1 < n3:
    print('O menor valor digitado é {}.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor valor digitado é {}.'.format(n2))
elif n3 < n2 and n3 < n1:
    print('O menor valor digitado é {}.'.format(n3))
else:
    print("ERROR 404")
