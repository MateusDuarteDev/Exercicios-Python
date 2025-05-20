from datetime import date
ano = int(input('Digite o ano de seu nascimento : '))
hoje = date.today().year
alistamento = hoje - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,alistamento,hoje))
if alistamento == 18:
    print('Você deve se alistar AGORA!')
elif alistamento < 18:
    falta = 18 - alistamento
    print('Ainda não deve se alistar, faltam {} anos'.format(falta))
else :
    passou = alistamento - 18
    print('Você se alistou em {}, já se passaram {} anos.'.format(ano+18,passou))
