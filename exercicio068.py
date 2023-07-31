from random import randint
v = 0
while True:

    print('=' * 30)
    print('Jogo do impar ou par.')
    print('=' * 30)
    pessoa = str(input('Digite i para IMPAR ou p para PAR: ')).lower()
    n = int(input('Digite um número: '))
    pc = randint(0, 10)
    soma = n + pc
    print(f'O computador escolheu {pc}.')
    if pessoa=="i" and (soma%2)==1:
        v += 1
        print(f'{n}+{pc}={soma} -> impar')
        print("Você ganhu!\n")
    elif pessoa=="p" and (soma%2)==0:
        v+=1
        print(f'{n}+{pc}={soma} -> par')
        print("Você ganhou!\n")
    else:
        break
print('Você perdeu.\n')
print(f'Voce ganhou {v} vezes!')

