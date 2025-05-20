'''
num = int(input('Digite o número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Milhar : {}".format(m))
print("Centena : {}".format(c))
print("Dezena : {}".format(d))
print("Unidade : {}".format(u))
'''
numero = str(input("Digite o número de 4 digitos entre 0 a 9999 : "))
print("Milhar : {}".format(numero[0]))
print("Centena : {}".format(numero[1]))
print("Dezena : {}".format(numero[2]))
print("Unidade : {}".format(numero[3]))
