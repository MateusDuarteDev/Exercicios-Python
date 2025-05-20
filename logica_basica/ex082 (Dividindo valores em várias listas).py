lista = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número : '))
    lista.append(numero)
    continua = str(input('Deseja continuar ? [S/N]  ')).upper()
    if continua == 'N':
        break
for pos,numero in enumerate(lista):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'A lista completa : {lista}')
print(f'A lista dos pares : {pares}')
print(f'A lista dos impares : {impares}')