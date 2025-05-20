'''from math import factorial
num = int(input('Qual fatorial quer saber ? '))
f = factorial(num)
print('Fatorial : {}! = {}'.format(num,f))
'''
fatorial = 1
n = int(input('Qual fatorial quer saber ? '))
num = n
while num > 0:
    fatorial = fatorial * num
    num = num - 1
print('Fatorial : {}! = {}'.format(n,fatorial))

