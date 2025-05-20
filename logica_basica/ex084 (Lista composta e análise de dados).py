princ = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome : ')))
    temp.append(float(input('Peso : ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    continua = str(input('Deseja continuar ? [S/N]  ')).upper()
    if continua == 'N':
        break


print(f'a) Quantas pessoas foram cadastradas ? {len(princ)}')
print(f'b) O maior peso foi de {maior}Kg, de : ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end = ' ')
print()
print(f'b) O menor peso foi de {menor}Kg, de : ',end ='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end = ' ')

