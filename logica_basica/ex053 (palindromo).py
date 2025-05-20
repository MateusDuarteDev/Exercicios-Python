frase = str(input('Digite a frase : ')).lower().replace(' ','')
palindromo = frase[::-1]
if frase == palindromo:
    print('Esta frase é um palindromo')
else :
    print('Esta frase NÃO é um palindromo')