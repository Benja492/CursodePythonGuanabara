peso = float(input('Digite seu peso: '))
altura = float(input('Digite seu altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso. Imc = {:.2f}.'.format(imc))
elif 18.5 < imc < 25:
    print('Você está no peso ideal. Imc = {:.2f}.'.format(imc))
elif 25 <= imc < 30:
    print('Você está com sobrepeso. Imc = {:.2f}.'.format(imc))
elif 30 <= imc < 40:
    print('Você está com obesidade. Imc = {:.2f}.'.format(imc))
elif imc >= 40:
    print('Você está com obesidade mórbida. Imc = {:.2f}.'.format(imc))