class Tarefa:
    def __init__(self,descricao):
        self.descricao = descricao
        self.completa = False
    def marcar_completa(self):
        if self.completa is False:
            self.completa = True
        else:
            print('Tarefa já foi completa')
    def marcar_incompleta(self):
        if self.completa is True:
            self.completa = False
        else:
            print('Tarefa está incompleta')
    def __str__(self):
        return f'A tarefa é : {self.descricao} \nA tarefa está completa : {str(self.completa)}'
tarefa1 = Tarefa('Dever de matemática')
tarefa2 = Tarefa('Dever de Portugues')
print(tarefa1)
tarefa1.marcar_completa()
print(tarefa1)
tarefa1.marcar_incompleta()
print(tarefa1)
