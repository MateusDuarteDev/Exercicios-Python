from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1,7+1):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if atual - ano >= 21:
        maior = maior + 1
    else :
        menor = menor + 1
print('Das 7 pessoas, {} são maiores de idade e {} são menores'.format(maior,menor))
