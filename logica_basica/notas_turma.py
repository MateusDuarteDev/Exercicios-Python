ct = 1
l_notas = []
print("Digite [-1] para sair")
while True:
    nota = float(input(f"Nota do aluno {ct}: "))
    ct+=1
    if nota == -1:
        break
    l_notas.append(nota)

print("\nQuantidade de alunos: ",len(l_notas))
print("Média da turma: ",sum(l_notas)/len(l_notas))