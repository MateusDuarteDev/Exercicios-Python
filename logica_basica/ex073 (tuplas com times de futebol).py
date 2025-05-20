brasileirao = ['Botafogo','Fortaleza','Palmeiras','Mengão','Cruzeiro','Bambis','Bahia','Vasco','Galo','Inter','Bragantino','Athletico','Juventude','Criciúma','Grêmio','Flu','Curintia','Vitória','Cuiabá','Atlético-GO']

print('G-5 DO BRASILEIRÃO: ')
for a in brasileirao[0:5]:
    print(a)

print('\nZ-4 DO BRASILEIRÃO: ')
for b in brasileirao[-4:]:
    print(b)

print('\nEM ORDEM ALFABÉTICA : ')
alfabetico = sorted(brasileirao)
for c in alfabetico:
    print(c)

print('\nEM QUE POSIÇÃO ESTÁ O MENGÃO ???')
print(brasileirao.index('Mengão')+1)