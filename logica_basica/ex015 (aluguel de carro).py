dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos KM rodados ? '))
pago = (dias*60) + (km*0.15)
print('O valor total do aluguel é de R${:.2f}'.format(pago))
