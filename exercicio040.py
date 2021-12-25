n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2
if m >= 7:
    print('aluno aprovado com média {:.1f}.'.format(m))
elif 5 <= m < 7:
    print('Aluno de recuperação com média {:.1f}.'.format(m))
else:
    print('Aluno reprovado com média {:.1f}.'.format(m))