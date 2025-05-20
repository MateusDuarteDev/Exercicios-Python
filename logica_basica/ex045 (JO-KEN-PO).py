import random
from time import sleep
jokenpo = ['pedra', 'papel', 'tesoura']
print('VAMOS JOGAR JOKENPO ???')
pessoa = input('Qual a sua escolha ? : Pedra, Papel ou Tesoura ? ').lower()
pc = random.choice(jokenpo)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*30)
print('Você escolheu \033[31m{}\033[m e o PC escolheu \033[31m{}\033[m, logo...'.format(pessoa,pc))
print('-='*30)
if pessoa == 'pedra':
    if pc == 'pedra':
        print('EMPATE !!')
    elif pc == 'papel':
        print('PC GANHOU !!')
    elif pc == 'tesoura':
        print('VOCÊ GANHOU !!')
elif pessoa == 'papel':
    if pc == 'papel':
        print('EMPATE !!')
    elif pc == 'pedra':
        print('VOCÊ GANHOU !!')
    elif pc == 'tesoura':
        print('PC GANHOU !!')
elif pessoa == 'tesoura':
    if pc == 'tesoura':
        print('EMPATE !!')
    elif pc == 'pedra':
        print('PC GANHOU !!')
    elif pc == 'papel':
        print('VOCÊ GANHOU !!')
else:
    print('VOCÊ NÃO SABE JOGAR ???')
