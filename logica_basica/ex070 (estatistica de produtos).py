print('-'*20)
print('CADASTRE SUA COMPRA')
print('-'*20)
soma = 0
ctpreco = 0
menor = 0
ct = 0
while True:
    produto = str(input('PRODUTO : ')).title()
    preco = float(input('PREÇO : '))
    ct = ct + 1
    soma = soma + preco
    if ct == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        ctpreco = ctpreco + 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja Continuar ? [S/N]')).strip().upper()[0]
    if continua in 'N':
        break
print('{:~^50}'.format(' FIM DA COMPRA '))
print(f'A) O total da compra foi : {soma:.2f}')
print(f'B) Total de {ctpreco} produtos custam mais de R$1000.00')
print(f'C) O produto mais barato foi {barato} que custa R${menor:.2f}')
