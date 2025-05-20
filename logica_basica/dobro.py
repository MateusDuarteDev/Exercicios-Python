"""Exercício 2 :

2. Elabore o programa que gere a sequência do dobro dos números naturais até 10 na
ordem crescente. Mostre também a soma da sequência gerada.   """

soma = 0
for i in range (0,10+1,1):
    dobro = i*2
    print (dobro)
    soma = soma + dobro
print("Soma : ",soma)