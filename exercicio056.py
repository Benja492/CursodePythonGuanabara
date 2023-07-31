somaidade = 0
homemaisvelho = 0
nomemaisvelho = 0
totalmulher20 = 0
for i in range (1, 5):
    print('----- {}° Pessoa -----'.format(i))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo [ M / F ]: ').strip().upper())
    somaidade += idade
    if i == 1 and sexo == 'M':
        homemaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > homemaisvelho:
        homemaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
mediadade = somaidade / 4
print('A média de idades é de {} anos.'.format(mediadade))
print('O homem mais se chama e {} e tem {} anos de idade.'.format(nomemaisvelho, homemaisvelho))
print('O número de mulheres menores de 20 anos é de {}.'.format(totalmulher20))