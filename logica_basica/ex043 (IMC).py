peso = float(input('Digite o seu peso, em kg : '))
altura = float(input('Digite a sua altura, em metros : '))
imc = peso/(altura*altura)
print('Seu IMC é de {:.2f}!'.format(imc))
if imc < 18.5:
    print('Logo, você está \033[0;31mAbaixo do Peso!')
elif imc < 25:
    print('Logo, você está no \033[0;31mPeso Ideal!')
elif imc < 30:
    print('Logo, você está em \033[0;31mSobrepeso!')
elif imc <= 40:
    print('Logo, você está em \033[0;31mObesidade!')
elif imc > 40:
    print('Logo, você está em \033[0;31mObesidade Mórbida')