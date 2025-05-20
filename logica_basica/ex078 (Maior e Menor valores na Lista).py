lista = []
maior = menor = 0
for cont in range(0,5):
    lista.append(int(input(f'Digite o número da posição {cont}: ')))
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'A lista que digitou foi : {lista}')
print(f'O maior número digitado foi {maior} nas posições ', end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor número digitado foi {menor} nas posições ', end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
