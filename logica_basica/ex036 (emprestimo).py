casa = float(input('Digite o valor da casa : R$'))
salario = float(input('Digite o seu salário : R$'))
anos = float(input('Digite em quantos anos deseja pagar : '))
valormensal = (casa/anos)/12
maximo = salario*30/100
print('O valor mensal a ser pago é de R${:.2f}'.format(valormensal))
print('O valor máximo da parcela é : R${}'.format(maximo))
if valormensal >= maximo:
    print('Empréstimo NEGADO!!')
else :
    print('Empréstimo APROVADO!!')