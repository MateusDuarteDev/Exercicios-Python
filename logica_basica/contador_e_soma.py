l_numeros = []
print("Digite [-1] para sair")
while True:
    numero = int(input("Digite um número: "))
    if numero == -1:
        break
    l_numeros.append(numero)
print("lista : ",l_numeros)
print("Tamanho da lista: ",len(l_numeros))
print("Soma : ",sum(l_numeros))