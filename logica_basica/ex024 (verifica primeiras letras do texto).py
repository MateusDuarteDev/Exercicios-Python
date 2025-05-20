cidade = input('Digite o nome da cidade : ').strip()
cid = cidade.lower().find('santo')
if cid == 0:
    print('A cidade começa com a palavra Santo')
else:
    print('A cidade NÃO começa com a palavra Santo')