sexo = str(input('Digite o sexo [M/F] : ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dado inválido ... \nUse M para masculino ou F para feminino!')
    sexo = str(input('Digite o sexo [M/F] : ')).strip().upper()[0] #STRIP tira os espaços anteriores. UPPER deixa maiusculo. [0] usa apenas o primeiro caractere.
print('Sexo {} registrado com sucesso!'.format(sexo))

