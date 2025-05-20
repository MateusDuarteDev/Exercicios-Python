lista = []

while True:
    numero = int(input('Digite um número : '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar!')
    continua = str(input('Deseja continuar ? [S/N]  ')).upper()
    if continua == 'N':
        break
print('-~'*20)
lista.sort()
print(f'Você digitou os valores {lista}')