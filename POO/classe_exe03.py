class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    def adicionar_nota(self,nota):
        self.notas.append(nota)
    def media_notas(self):
        return sum(self.notas)/len(self.notas)
    def __str__(self):
        return f'O aluno {self.nome} teve média {self.media_notas()}'

aluno1 = Aluno('João', '000000')
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(9)

print(aluno1)
