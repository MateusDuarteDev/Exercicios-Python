lista = []
for c in range(0,5):
    i = int(input(f'Digite o número : '))
    if c == 0 or i > lista[-1]:
        lista.append(i)
    else:
        pos = 0
        while pos < len(lista):
            if i <= lista[pos]:
                lista.insert(pos,i)
                break
            pos = pos + 1
print(f'Os valores digitados : {lista}')
