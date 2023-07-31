frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso+= junto[letra]
if inverso == junto:
    print('Temos um polindromo.')
else:
    print('Não temos um polindromo.')