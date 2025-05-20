
ct = 0
soma = 0
num = int(input("Digite a quantidade de alunos : "))
for i in range(num):
    nota = float(input(f"Nota do aluno {i+1} : "))
    soma = soma + nota
    ct = ct + 1
media = soma / ct
print("A média de todos os alunos é:", media)
