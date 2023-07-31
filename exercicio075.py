a=int(input("Digite um número: "))
b=int(input("Digite um número: "))
c=int(input("Digite um número: "))
d=int(input("Digite um número: "))
tupla=(a, b, c, d)
x9=0
p3=0
aux=0
par=0
for i in tupla:
#    aux+=1
#    if i==9:
#        x9+=1
#    if p3==0:
#        if i==3:
#            p3=aux
    if (i%2)==0:
        par+=1
print(f"Você digitou os valores: {tupla}")
print(f"O número 9 foi digitado {tupla.count(9)} vezes.")
print(f"O número 3 aparece pela primeira vez na posição {tupla.index(3)+1}.")
print(f"Existem {par} números pares.")





