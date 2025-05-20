salario = int(input('Digite seu salário : R$'))
if salario <= 1250 :
    salario = salario*1.15
else :
    salario = salario*1.1
print('Seu novo salário com aumento é : {}'.format(salario))
