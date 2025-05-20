import random
ct = 0
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('~~*'*20,'\n')
    numero = int(input('Digite o número : '))
    parimpar = ' '
    while parimpar not in 'PI':
        parimpar = str(input('Escolhe PAR ou IMPAR ?[P/I] ')).strip().upper()[0]
    pc = random.randint(0,10)
    soma = numero + pc
    if parimpar in 'P' and soma%2==1:
        print(f'Você jogou {numero} e o PC {pc}. A soma é {soma} e deu IMPAR!')
        print('VOCE PERDEU')
        break
    elif parimpar in 'I' and soma%2==0:
        print(f'Você jogou {numero} e o PC {pc}. A soma é {soma} e deu PAR!')
        print('VOCE PERDEU')
        break
    ct = ct + 1
    if parimpar in 'P' and soma%2==0:
        print(f'Você jogou {numero} e o PC {pc}. A soma é {soma} e deu PAR!')
        print('VOCE GANHOU')
        print('Vamos jogar novamente ...')
    elif parimpar in 'I' and soma%2==1:
        print(f'Você jogou {numero} e o PC {pc}. A soma é {soma} e deu IMPAR!')
        print('VOCE GANHOU')
        print('Vamos jogar novamente ...')
print(f'GAME OVER ! Você venceu {ct} vezes')
