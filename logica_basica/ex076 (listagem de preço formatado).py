listagem = ('Lápis',1.50,
            'Borracha',2,
            'Caderno',15,
            'Estojo',20,
            'Compasso',9.99,
            'Mochila',229.99,
            'Canetas',18.70,
            'Livro de Ciências',60,
            'Garrafinha',30.10)
print('~'*39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('~'*39)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('~'*39)
