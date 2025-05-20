print('\033[7;31;40mVamos fazer uma PA com 10 termos ?\033[m \n')
termo = int(input('Digite o primeiro termo da PA : '))
razao = int(input('Digite a razão da PA : '))
decimo = termo + (10-1)*razao
print('Esta é a PA que solicitou : ')
for c in range (termo,decimo + razao,razao):
    print(c,end=' ⭢ ')
print('FIM')