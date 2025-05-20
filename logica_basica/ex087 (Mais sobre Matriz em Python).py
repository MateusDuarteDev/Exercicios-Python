matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = soma = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
        if matriz[l][c] %2 == 0:
            pares = pares + matriz[l][c]
        if matriz[l][2]:
            soma = soma + matriz[l][2]
        if matriz[1][c] > maior:
            maior = matriz[1][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]',end ='')
    print()

print(f'a) A soma de todos os valores pares digitados : {pares}')
print(f'b) A soma dos valores da terceira coluna : {soma}')
print(f'c) O maior valor da segunda linha : {maior}')