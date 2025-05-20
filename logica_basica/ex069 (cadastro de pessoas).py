print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
cti = 0
cth = 0
ctm = 0
while True:
    idade = int(input('IDADE : '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO : [M/F] ')).strip().upper()
    if idade >= 18:
        cti = cti + 1
    if sexo in 'M':
        cth = cth + 1
    if sexo in 'F' and idade < 20:
        ctm = ctm + 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja Continuar ? [S/N]')).strip().upper()
    if continua in 'N':
        break
print(f'A) São {cti} pessoas acima de 18 anos!')
print(f'B) São {cth} homens cadastrados!')
print(f'C) São {ctm} mulheres abaixo de 20 anos!')
