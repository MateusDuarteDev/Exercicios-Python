import math
ca = float(input('Digite o cateto adjacente : '))
co = float(input('Digite o cateto oposto : '))
h = math.hypot(ca,co)

print("A hipotenusa desse triangulo é {:.2f}".format(h))