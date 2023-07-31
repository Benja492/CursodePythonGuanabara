numpa=int(input('Digite um número: '))
razpa=int(input('Digite a razão da P.A: '))
cont=0
prog = numpa
while cont != 11:
    cont +=1
    if cont==1:
        print('{} ->'.format(numpa),end=' ')
    else:
        prog+=razpa
        if cont<11:
            print('{} ->'.format(prog),end=' ')
        else:
            print('Fim.')