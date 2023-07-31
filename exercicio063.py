n = int(input("Digite o número de termos a serem exibidos: "))
i=0
f0 = 0
f1 = 0
f2 = 1
print('{} -> {} ->'.format(f1,f2),end=' ')
while i<n:
    i+=1
    f0 = f1 + f2
    print('{} ->'.format(f0), end=' ')
    f1=f2
    f2=f0
print('fim.')

