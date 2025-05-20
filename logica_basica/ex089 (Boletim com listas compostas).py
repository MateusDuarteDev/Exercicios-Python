lista = []
while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2 : '))
    media = (nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    continua = str(input('Deseja continuar ? [S/N]  ')).upper()
    if continua == 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<20}{"Média":>18}')
print('-'*43)
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<20}{a[2]:>17.1f}')
print('-'*43)
while True:
    consulta = int(input('\nDeseja ver as notas de qual aluno? [999 interrompe] '))
    if consulta == 999:
        print('FINALIZANDO...')
        break
    elif consulta <= len(lista)-1:
        print(f'Notas de {lista[consulta][0]} são {lista[consulta][1]}')
    elif consulta > len(lista)-1:
        print('Não encontrado, tente novamente !')
