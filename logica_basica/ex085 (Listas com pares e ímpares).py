lista = [[],[]]
for num in range(1,8):
    valor = int(input(f'{num}º valor: '))
    if valor % 2== 0 :
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Números pares : {lista[0]}')
print(f'Números impares : {lista[1]}')