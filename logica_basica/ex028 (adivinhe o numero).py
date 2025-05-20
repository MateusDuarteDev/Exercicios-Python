import random
from time import sleep

num1 = random.randint(0,5)
print('-=-'*15)
num2 = int(input('Digite o número de 0 a 5 : '))
print('-=-'*15)
print('Processando ...... ')
sleep(2)
if num1 == num2:
    print('PARABÉNS VOCÊ ACERTOU !!')
else:
    print('Você não acertou... :(')
print('O número era : {}'.format(num1))
print('O número digitado foi :{}'.format(num2))