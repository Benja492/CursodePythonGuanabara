numpa=int(input('Digite um número: '))
razpa=int(input('Digite a razão da P.A: '))
cont=1
prog = numpa
total = 0
mais = 10
while mais!=0:
    total=total+mais
    while cont <= total:
        cont +=1
        print('{} ->'.format(prog),end=' ')
        prog+=razpa

    print('PAUSA')
    mais = int(input("Quer mostra quantos termos as mais? "))
    if mais==0:
        break
print("Fim")

