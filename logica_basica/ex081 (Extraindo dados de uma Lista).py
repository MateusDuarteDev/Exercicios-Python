lista = []
while True:
    numero = int(input('Digite um número : '))
    lista.append(numero)
    continua = str(input('Deseja continuar ? [S/N]  ')).upper()
    if continua == 'N':
        break
print(f'a) Quantos números foram digitados ? : {len(lista)}')
lista.sort(reverse = True)
print(f'b) A lista de valores ordenada de forma decrescente : {lista}')
if 5 in lista :
    print('O valor 5 está presente na lista')
else:
    print('O valor 5 não está na lista')
