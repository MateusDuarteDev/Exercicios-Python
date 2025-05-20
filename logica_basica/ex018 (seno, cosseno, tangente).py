import math
angulo = float(input('Digite o angulo : '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("O angulo {} tem o seno {:.2f}".format(angulo,sen))
print("O angulo {} tem o cosseno {:.2f}".format(angulo,cos))
print("O angulo {} tem a tangente {:.2f}".format(angulo,tan))
