numero = int(input('Digite o número que dejeja converter : '))
opcao = int(input('Digite [1] para binário,[2] para octal ou [3] para hexadecimal : '))
if opcao == 1:
    print('{} convertido para BINÁRIO é : {}'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é : {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é : {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente !')