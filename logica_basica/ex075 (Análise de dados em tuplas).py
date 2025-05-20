lista = (int(input('Digite um número : ')),int(input('Digite um número : ')),int(input('Digite um número : ')),int(input('Digite um número : ')))
print(f'Você digitou os números :{lista}')
print('a) Quantas vezes aparece o número 9?')
print(f'O número 9 aparece {lista.count(9)} vezes')
print('b) Em que posição foi digitado o primeiro valor 3 ?')
if 3 in lista:
    posicao = lista.index(3)+1
    print(f'O número 3 foi digitado na {posicao}ª posicao')
else:
    print('Não foi digitado nenhum número 3')
print('c) Quais foram os números pares? ')
for i in lista:
    if i % 2 == 0:
        print(i)


