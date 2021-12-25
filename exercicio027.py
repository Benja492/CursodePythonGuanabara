n = str(input('Digite seu nome: ')).strip()
nd = n.split()
print('Seu primeiro nome é {}.\nSeu último nome é {}.'.format(nd[0], nd[len(nd)-1]))
