pessoas = []
somaidade = 0
media = 0

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome : '))
    while True:
        pessoa['sexo'] = str(input('Sexo : [M/F] ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade : '))
    somaidade = somaidade + pessoa['idade']
    pessoas.append(pessoa)
    while True:
        continuar = str(input('Deseja continuar ? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
            break
print('-='*20)
print(f'O grupo tem {len(pessoas)} pessoas')
media = somaidade/len(pessoas)
print(f'A média de idade é de : {media:.2f} anos.')
print('~~'*20)
print(f'As mulheres cadastradas foram :')
for i in pessoas:
    if i['sexo'] == 'F':
        print(f'{i["nome"]};', end=' ')
print()
print('~~'*20)
print('A lista de pessoas acima da média :')
for i in pessoas:
    if i['idade'] > media :
        for k,v in i.items():
            print(f'{k} = {v} ;', end=' ')
        print()
print('~~'*20)
print('<<ENCERRADO>>')





