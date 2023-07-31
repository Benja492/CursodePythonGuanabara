n = int(input("Digite um números [999 para sair]: "))
soma = 0
numeros = 0
while True:
    if n == 999:
        break
    else:
        soma+=n
        numeros+=1
    n = int(input("Digite um números [999 para sair]: "))
print("Numeros digitados: {}. \n Soma dos numeros : {}.".format(numeros,soma))