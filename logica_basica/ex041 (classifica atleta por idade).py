from datetime import date
ano = int(input('Digite o ano de seu nascimento : '))
hoje = date.today().year
categoria = hoje - ano
print('O atleta tem {} anos e está na categoria...'.format(categoria))
if categoria <= 9:
    print("MIRIM")
elif categoria <= 14:
    print('INFANTIL')
elif categoria <= 19:
    print('JUNIOR')
elif categoria <= 25:
    print('SENIOR')
else:
    print('MASTER')