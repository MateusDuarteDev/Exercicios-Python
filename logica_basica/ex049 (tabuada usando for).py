numero = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,10+1):
    print("{} X {} = {}".format(numero,c,numero*c))