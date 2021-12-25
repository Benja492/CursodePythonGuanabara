numero = int(input('Digite um número inteiro: '))

print('Digite o número da opção correspondente a sua necessidade: ')
print('''( 1 ) BINÁRIO\n( 2 ) OCTAL\n( 3 ) HEXADECIMAL''')
opçao = int(input('Opção: '))

if opçao == 1:
    print('A conversão binaria de {}    é : {}.'.format(numero,bin(numero)))
elif opçao == 2:
    print('A conversão octal de {} é : {}.'.format(numero,oct(numero)))
elif opçao == 3:
    print('A conversão hexadecimal de {} é : {}.'.format(numero,hex(numero)))
else:
    print('ERRO 404')