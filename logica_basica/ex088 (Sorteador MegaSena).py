from random import randint
from time import sleep
lista = []
rep = 0
jogos = int(input('Digite quantos jogos deseja sortear : '))
print('~='*20)
for j in range(1,jogos+1):
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            rep = rep + 1
        if rep >= 6:
            break
    lista.sort()
    print(f'Jogo {j} : {lista}')
    sleep(1)
    lista.clear()
    rep = 0
print('~='*5,'BOA SORTE !!!','~='*5)
