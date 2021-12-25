l1 = float(input('Digite a reta 1:'))
l2 = float(input('Digite a reta 2:'))
l3 = float(input('Digite a reta 3:'))
if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    print('É possível criar um triângulo com as retas inseridas.')
else:
    print('Não é possível criar um triângulo com as retas inseridas.')
