r1 = float(input('Digite o valor da RETA 1 : '))
r2 = float(input('Digite o valor da RETA 2 : '))
r3 = float(input('Digite o valor da RETA 3 : '))
if r1+r2 < r3 or r1+r3 < r2 or r2+r3 < r1:
    print('Essas retas não formam um triangulo')
else:
    print('Essas retas conseguem formar um triangulo ',end='')
    if r1==r2==r3:
        print('EQUILATERO')
    elif r1==r2 or r1==r3 or r2==r3:
        print('ISOSCELES')
    else :
        print('ESCALENO')
