i = 1
j = 1
print('Sequencia de FIBONACCI')
termo = int(input('Quantos termos da sequencia de Fibonacci deseja saber? '))
print('Esta é a sequencia de Fibonacci com {} termos que solicitou : '.format(termo))
print('0 - 1 - 1', end = ' - ')
while termo > 3:
    k = i + j
    print(k,end= ' - ')
    i = j
    j = k
    termo = termo-1
print(' FIM')