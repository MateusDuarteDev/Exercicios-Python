import random
from time import sleep
ct = 0
pc = random.randint(0,100)
print('-=-'*15)
print('Pensei em um número ... tente adivinhar ...')
pessoa = int(input('Digite um número de 0 a 100 : '))
print('-=-'*15)
while pc != pessoa:
    print('Você não acertou... :(',end=' ')
    ct = ct+1
    if pc > pessoa :
        print('Tente um número \033[7;31;40m⬆⬆ MAIOR ⬆⬆\033[m ...')
    else :
        print('Tente um número \033[7;30;41m⬇⬇ MENOR ⬇⬇\033[m ...')
    pessoa = int(input('\nTente Novamente outro numero entre 0 e 100: '))
print('\nPARABÉNS VOCÊ ACERTOU !!')
ct = ct+1
print('Você precisou de {} tentativas'.format(ct))
