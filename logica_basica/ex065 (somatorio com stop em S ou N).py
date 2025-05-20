soma = 0
ct = 0
maior = 0
menor = 0
cond = 's'
while cond in 'Ss':
    numero = int(input('Digite um número : '))
    ct = ct+1
    soma = soma + numero
    if ct == 1:
        maior = menor = numero
    else :
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    cond = str(input('Deseja continuar ? [S/N]  ')).upper().strip()
    while cond not in 'SsNn':
        print('Opção inválida!')
        cond = str(input('Deseja continuar ? [S/N]  ')).upper().strip()
media = soma/ct
print('Foram digitados {} números e a média deles é {}'.format(ct,media))
print('O menor número foi {} e o maior foi {} !'.format(menor,maior))
