class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
        else :
            print('Livro já foi emprestado')
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
        else:
            print('O livro já foi devolvido')
    def __str__(self):
        return f'''O livro é : {self.titulo} \nO livro está disponível: {str(self.disponivel)}'''


livro1 = Livro('Senhor dos Anéis','J.R.Tolkien','1890')

print('Antes : \n', livro1)
livro1.emprestar()
print('Depois : \n', livro1)
livro1.devolver()
print('Depois 2: \n', livro1)
