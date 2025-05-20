"""Exercício 3 : 

3. Implemente uma função (def) que recebe três valores reais, calcula a média aritmética e retorna o valor calculado. A função principal (main) lê os três valores, chama a função (def) e mostra o valor retornado pela função (def).
Obs.: no programa (main), chame a função (def) média aritmética pelo menos duas vezes."""

def valor_media(v1,v2,v3):
    media=(v1+v2+v3)/3
    return media
if __name__ == '__main__' :
    v1 = int(input("Digite o primeiro valor : "))
    v2 = int(input("Digite o segundo valor : "))
    v3 = int(input("Digite o terceiro valor : "))
    media = valor_media(v1,v2,v3)
    print("A média dos 3 números é : ", media)

    v4 = int(input("Digite outro primeiro valor : "))
    v5 = int(input("Digite outro segundo valor : "))
    v6 = int(input("Digite outro terceiro valor : "))
    media = valor_media(v4, v5, v6)
    print("A média dos 3 números é : ", media)