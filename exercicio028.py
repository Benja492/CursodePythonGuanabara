import random
n = random.randrange(0, 5)
print("O computador escolheu um número entre 0 e 5.Tente adivinha-ló!!")
ne = int(input("Digite um número: "))
if ne == n:
    print('Você acertou!!')
else:
    print('Você error.')