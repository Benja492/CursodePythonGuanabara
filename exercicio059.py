n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
op = 0
while op != 5:
    print('-----------------------------')
    print('''    [ 1 ] Somar.
    [ 2 ] Multiplicar.
    [ 3 ] Maior.
    [ 4 ] Novos números.
    [ 5 ] Sair do programa.''')
    op = int(input('Digite o número da opção: '))
    if op == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    if op == 2:
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, n1 * n2))
    if op == 3:
        if n1 > n2:
            print('O valor {} é maior do que o valor {}.'.format(n1, n2))
        elif n2 > n1:
            print('O valor {} é maior do que o valor {}.'.format(n2, n1))
        else:
            print('Os valores são iguais.')
    if op == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))

    if op == 5:
        print('Encerrando o programa.')
    if 0<op>5:
        print('Comando inválido.')