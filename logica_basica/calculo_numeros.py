"""Exercicio 1

1. Projete o programa que leia vários valores reais digitados pelo usuário e no final mostre as seguintes informações:
- A quantidade de valores digitados;
- A soma dos valores digitados;
- A média aritmética dos valores digitados;
- E a quantidade de valores digitados maior que 20."""

ct = 0
ct20 = 0
soma = 0
media = 0
print("Digite [-1] para sair !!")
while True :
    numero = int(input("Digite um número real: "))
    if numero == -1:
        break
    if numero < 0:
        print("Número inválido!")
    if numero >= 0 :
        ct = ct+1
        soma = soma + numero
    if numero > 20:
        ct20 = ct20 +1
media = soma/ct

print("Quantidade de números digitados :",ct)
print("A soma dos números :",soma)
print("A média dos números :",media)
print("Quantidade de números maiores que 20 :",ct20)