class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def trocaCor(self,novaCor):
        self.cor = novaCor

    def mostraCor(self):
        return self.cor

bola1 = Bola('Azul','10','Metal')

print(f'Cor da bola : {bola1.mostraCor()}')
bola1.trocaCor('Vermelha')
print(f'Cor da bola : {bola1.mostraCor()}')
