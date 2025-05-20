dados = {}
total = 0
dados['nome'] = str(input('Nome do jogador : '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou ? '))
dados['gols'] = []
for i in range(0,partidas):
    gols = int(input(f'Quantos gols na partida {i+1}? '))
    dados['gols'].append(gols)
    total = total + gols
dados['total'] = total
print('-='*30)
print(dados)
print('-='*30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas')
for i,j in enumerate(dados['gols']):
    print(f'=> Na partida {i+1}, fez {j} gols')
print(f'Foi um total de {total} gols')
