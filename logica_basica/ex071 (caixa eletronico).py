print('='*20)
print('CAIXA ELETRONICO')
print('='*20)
valor = int(input('Qual o valor do saque ? R$'))
nota50 = nota20 = nota10 = nota1 = 0
while True:
    if valor == 0:
        break
    while valor >= 50:
        valor = valor - 50
        nota50 = nota50 + 1
    if valor >=20:
        while valor>=20:
            valor = valor-20
            nota20 = nota20+1
    if valor >=10:
        while valor>=10:
            valor = valor-10
            nota10 = nota10+1
    if valor >=1:
        while valor>=1:
            valor = valor-1
            nota1 = nota1+1
print(f'''Você sacou : 
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota1} notas de 1''')

