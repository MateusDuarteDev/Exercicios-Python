velocidade = float(input('Qual a velocidade do veículo ? '))
multa = (velocidade -80)*7
if velocidade >80:
    print('Carro acima da velocidade, foi multado!')
    print('O valor da multa é : R${}'.format(multa))
else :
    print('Carro abaixo da velocidade, não foi multado')