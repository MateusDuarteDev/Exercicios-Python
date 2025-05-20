soma = 0
ct = 0
while True:
    n = int(input('Digite um numero [0 para parar]: '))
    if n == 0:
        break
    soma = soma + n
    ct = ct + 1
print(f'Digitou {ct} números e a soma é : {soma}')