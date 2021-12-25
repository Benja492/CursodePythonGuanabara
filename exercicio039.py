from datetime import date
atual = date.today().year
ano = int(input('Digite o ano em que você nasceu: '))
if atual - ano >= 19:
    print('Seu tempo de se alistar já se passou há 1 ano.')
elif atual - ano == 18:
    print('Já está na hora de se alistar.')
else:
    print('Ainda não é hora de se alista. Espere mais {} anos.'.format(18-(atual)))