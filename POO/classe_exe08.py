class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,anos):
        self.idade = self.idade + anos
        if self.idade < 21:
            self.altura = self.altura + (0.5 * anos)

    def engordar(self,quilos):
        self.peso = self.peso + quilos

    def emagrecer(self,quilos):
        self.peso = self.peso - quilos

    def crescer(self,centrimetros):
        self.altura = self.altura + centrimetros
    def __str__(self):
        return f'''Nome : {self.nome}
Idade : {self.idade}
Peso : {self.peso}
Altura : {self.altura}\n'''

pessoa = Pessoa("João", 10, 35.0, 120)
print(pessoa)


pessoa.envelhecer(3)
print(f"Após envelhecer 3 anos: {pessoa}")

pessoa.engordar(2)
print(f"Após engordar 2 kg: {pessoa}")

pessoa.emagrecer(1)
print(f"Após emagrecer 1 kg: {pessoa}")

pessoa.crescer(5)  # Crescimento em centímetros
print(f"Após crescer 5 cm: {pessoa}")