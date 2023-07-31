from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
categoria = date.today().year - ano
if categoria <= 9:
    print('Sua categoria é mirim.')
elif 9 < categoria <= 14:
    print('Sua categoria é infantil.')
elif 14 < categoria <= 19:
    print('Sua categoria é júnior.')
elif 19 < categoria <= 25:
    print('Sua categoria é sênior.')
else:
    print('Sua categoria é master.')
