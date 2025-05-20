primo = int(input('Número que deseja saber se é primo : '))
total = 0
for c in range(1,primo+1):
    if primo % c == 0:
        total = total + 1
if total == 2:
    print('O número {} é PRIMO !'.format(primo))
else :
    print('O número {} NÃO É PRIMO !'.format(primo))
