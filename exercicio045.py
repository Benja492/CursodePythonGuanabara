import random
print('{:=^40}'.format('Jokenpo'))
jogada = ('pedra','papel','tesoura')
print('''Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
player = int(input('Escolha um número correspondente as opções: ')) - 1
maquina = random.randint(1, 3) - 1
if player == 0 and maquina == 1:
    print('Você perdeu! Você escoheu pedra e a máquina escolheu papel.')
elif player == 1 and maquina == 2:
    print('Você perdeu! Você escoheu papel  e a máquina escolheu tesoura.')
elif player == 2 and maquina == 0:
    print('Você perdeu! Você escoheu tesoura e a máquina escolheu pedra.')
elif player == 0 and maquina == 2:
    print('Você ganhou! Você escolheu pedra e a máquina tesoura.')
elif player == 1 and maquina == 0:
    print('Você ganhou! Você escolheu papel e a máquina pedra.')
elif player == 2 and maquina == 1:
    print('Você ganhou! Você escolheu tesoura e a máquina papel.')
elif player == maquina:
    print('Empatou! Você e a máquina escolheram {}.'.format(jogada[player]))

else:
    print('ERROR 404')