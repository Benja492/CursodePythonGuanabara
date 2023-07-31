menor = maior = n = 0
soma = 0
aux = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n > maior:
        maior = n
        if menor == 0:
            menor = maior
    elif n < menor:
        menor = n
    soma += n
    aux += 1
    op = str(input("Você quer continuar[S/N]: ")).upper().strip()
    if op == "N":
        break
    else:
        continue
media = soma/aux
print("Você digitou {} números, o maior foi {} e o menor foi {}. A média entre todos é {}.".format(aux,maior,menor,media))

