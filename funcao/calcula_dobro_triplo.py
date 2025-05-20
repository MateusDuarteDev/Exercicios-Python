def calcula_dobro(valor):
    valor = valor*2
    return valor
def calcula_triplo(valor):
    valor = valor*3
    return valor
if __name__ == '__main__':
    valor = int(input("valor : "))
    dobro = calcula_dobro(valor)
    print("Valor dobrado : ", dobro) # print("Valor dobrado : ", calcula_dobro(valor))
    triplo = calcula_triplo(valor)
    print("Valor triplicado : ", triplo) # print("Valor triplicado : ", calcula_triplo(valor))