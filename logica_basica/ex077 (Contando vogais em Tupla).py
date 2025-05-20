tupla = ('Arroz','Feijao','Batata','Carne','Salada','Beterraba','Frango','Peixe','Chuchu','Couve-Flor')

for i in tupla:
    print(f'\nNa palavra {i.upper()} temos ',end='')

    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')