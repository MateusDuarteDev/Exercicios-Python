soma = 0
idadeMaior = 0
mulheres = 0
homemVelho = ''
for c in range(1,4+1):
    print('----- {}ª PESSOA -----'.format(c))
    nome = input('\nNome : ')
    idade = int(input('Idade : '))
    sexo = input('sexo [M/F]').upper()
    soma = soma + idade
    if idade < 20 and sexo == 'F':
        mulheres = mulheres +1
    if sexo == 'M' and idade > idadeMaior:
        idadeMaior = idade
        homemVelho = nome
print('A média de idade é : {}'.format(soma/4))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeMaior,homemVelho))
print('Tem {} mulher(es) menores de 20 anos'.format(mulheres))