valor=int(input("Digite o valor a ser sacado: R$"))
cedula50=0
cedula20=0
cedula10=0
cedula01= 0
while valor != 0:
    while valor > 50:
        valor-=50
        cedula50+=1
    while valor > 20:
        valor-=20
        cedula20+=1
    while valor > 10:
        valor -= 10
        cedula10 +=1
    while valor >= 1:
        valor-=1
        cedula01+=1
print(f"""Você irá receber {cedula50} cédulas de 50, {cedula20} cédulas de 20, {cedula10} cédulas de 10 e {cedula01} cédulas de 1.""")