funcao = str(input('Digite a função : '))
pilha = []
for c in funcao:
    if c == '(':
        pilha.append('(')
    elif c ==')':
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua função é válida')
else:
    print('Sua função é inválida')
