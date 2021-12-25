print('='*10,'Aprovando Empréstimos','='*10)

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite a quantidade de anos para pagar: '))
mes = anos*12
prestaçao = casa/mes
limite = salario-(salario*(70/100))

if prestaçao > limite:
    print('O empréstimo não foi aprovado.')
    print('O valor das parcelas serão de R$ {:.2f} e isso ultrapassa o limite de 30% do seu salário.'.format(prestaçao))
else:
    print('O empréstimo foi aprovado.')
    print('O valor das parcelas serão de R$ {:.2f}.'.format(prestaçao))