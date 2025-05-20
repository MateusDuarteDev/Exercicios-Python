soma = 0
ct = 0
numero = 0
numero = int(input('Digite um número [999 para parar] : '))
while numero != 999:
    ct = ct+1
    soma = soma + numero
    numero = int(input('Digite um número [999 para parar] : '))
print('Foram digitados {} números e a soma deles é {}'.format(ct,soma))

