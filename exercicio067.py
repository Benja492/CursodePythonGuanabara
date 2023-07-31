n = int(input('Digite um número: '))
while n >= 0:
    print('----------------')
    for i in range(10):
        print('{} x {} = {}'.format(n,i+1,n*(i+1)))
        i+=1
    print('-----------------')
    n = int(input('Digite um número: '))
print('Tabuada encerrada. Volte sempre!')