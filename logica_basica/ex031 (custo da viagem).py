distancia = float(input('Digite a distância em km da viagem : '))
if distancia <= 200:
    valor = distancia*0.5
else:
    valor = distancia*0.45
print('A viagem tem {} km e custará R${}'.format(distancia,valor))
