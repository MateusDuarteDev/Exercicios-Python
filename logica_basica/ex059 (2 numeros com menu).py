num1 = int(input('Digite o Primeiro número : '))
num2 = int(input('Digite o Segundo número : '))
menu = 0
while menu != 5:
    menu = int(input('''-==-==-==-==- MENU -==-==-==-==-
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Opção : '''))
    if menu == 1:
        print('{} + {} = {}\n'.format(num1,num2,num1+num2))
    elif menu == 2:
        print('{} * {} = {}\n'.format(num1,num2,num1*num2))
    elif menu == 3:
        if num1 > num2:
            print('{} maior que {}\n'.format(num1,num2))
        else:
            print('{} maior que {}\n'.format(num2, num1))
    elif menu == 4:
        num1 = int(input('Digite o Primeiro número : '))
        num2 = int(input('Digite o Segundo número : '))
    elif menu == 5:
        print('Fim do programa!')
    else:
        print('Opção Inválida !')
print('Obrigado por usar a Calculadora !')
