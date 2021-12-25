l1 = float(input('Digite o valor do segmento 1: '))
l2 = float(input('Digite o valor do segmento 2: '))
l3 = float(input('Digite o valor do segmento 3: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    if l1 == l2 == l3:
        print('O triângulo que pode se formado é equilátero.')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('O triângulo que pode ser formado é isósceles')
    elif l1 != l2 != l3:
        print('O triângulo que pode ser formado é escaleno.')
else:
    print('Não existe triângulo que pode ser formado.')