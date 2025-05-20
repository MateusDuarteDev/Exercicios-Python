soma = 0
print('Digite os 6 números para somar os pares : ')
for c in range (1,7):
    num = int(input('Digite o {}º número : '.format(c)))
    if num%2==0:
        soma = soma + num

print('A soma é : {}'.format(soma))