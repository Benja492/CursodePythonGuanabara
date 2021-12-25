f = str(input('Digite uma frase: ')).upper().strip()
v = f.count('A')
pa = f.find('A')+1
ua = f.rfind('A')+1
print('O número de vezes que o "a" aparece é {}.\nO primeiro "a" aparece em {} e o último em {}.'.format(v, pa, ua))
