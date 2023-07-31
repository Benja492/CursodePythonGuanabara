homens = 0
mulheres20 = 0
maioridade = 0
sexo=" "
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input("Digite m para MULHER ou h para HOMEM: ")).strip().lower()
    if idade >= 18:
        maioridade += 1
    if sexo == "h":
        homens += 1
    if sexo == "m" and idade < 20:
        mulheres20 += 1
    op = str(input('Quer continuar [s / n]:')).lower()
    if op == "n":
        break
print(f'Foram cadastradas {maioridade} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheres20} mulheres com menos de 20 anos de idade.')