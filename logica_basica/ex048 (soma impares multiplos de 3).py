soma = 0
ct = 0
for c in range (0,500+1):
    if c%2==1:
        if c%3==0:
            soma = soma + c
            ct = ct + 1
print('A soma dos {} valores solicitados é : {}'.format(ct,soma))
