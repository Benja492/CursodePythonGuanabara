import datetime
maioridade = 0
menoridade = 0
ano = datetime.date.today().year
for i in range(7):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(1+i)))
    idade = ano - nasc
    if idade >= 18:
        maioridade +=1
    else:
        menoridade +=1
print('Neste grupo tem {} pessoas maiores de idade e {} pessoas menores de idade.'.format(maioridade,menoridade))