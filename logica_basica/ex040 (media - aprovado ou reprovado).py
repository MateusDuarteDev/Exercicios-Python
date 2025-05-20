nota1 = float(input('Primeira nota : '))
nota2 = float(input('Segunda nota : '))
media = (nota1+nota2)/2
print('Sua média é {:.1f}!'.format(media))
if media < 5:
    print('Infelizmente você está REPROVADO!')
elif media >= 7:
    print('Parabéns, você está APROVADO!')
else:
    print('Você está de RECUPERAÇÃO e tem uma segunda chance!')
