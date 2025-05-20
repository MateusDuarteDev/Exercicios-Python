while True:
    tabuada = int(input('Quer ver a tabuada de qual valor ? '))
    if tabuada <= 0:
        break
    print('-' * 20)
    for n in range(1,11):
        print(f'{tabuada} x {n} = {tabuada*n}')
    print('-'*20)
print('FIM')