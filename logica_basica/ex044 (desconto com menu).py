print('{:=^40}'.format(' PURPLE HAZE TABACARIA '))
valor = float(input('Digite o Valor do produto : '))
print('''Qual será a forma de pagamento ?
[1] para à vista no dinheiro/cheque
[2] para à vista no cartão
[3] para pagar em até 2x no cartão
[4] para pagar em 3x ou mais no cartão''')
condicao = int(input(''))
if condicao == 1:
    valor = valor-(valor*10/100)
    print('Para pagamento à vista no dinheiro/cheque você tem 10% de desconto e o valor final é {}'.format(valor))
elif condicao == 2:
    valor = valor-(valor*5/100)
    print('Para pagamento à vista no cartão você tem 5% de desconto e o valor final é {}'.format(valor))
elif condicao == 3:
    print('Para pagamento em até 2x no cartão você não tem desconto e o valor final é {}'.format(valor))
elif condicao == 4:
    valor = valor+(valor*20/100)
    print('Para pagamento em até 3x no cartão você tem juros de 20% e o valor final é {}'.format(valor))
else:
    print('OPÇÃO INVÁLIDA')