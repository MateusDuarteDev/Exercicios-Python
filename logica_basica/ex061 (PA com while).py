print('\033[7;31;40mVamos fazer uma PA com 10 termos ?\033[m \n')
termo = int(input('Digite o primeiro termo da PA : '))
razao = int(input('Digite a razão da PA : '))
ct = 1
print('Esta é a PA que solicitou : ')
while ct <= 10:
    print(termo,end=' ⭢ ')
    termo = termo + razao
    ct = ct + 1
print('FIM')