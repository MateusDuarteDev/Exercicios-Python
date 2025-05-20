class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def mudar_lado(self,novo_lado):
        self.lado = novo_lado

    def mostra_lado(self):
        return self.lado

    def area(self):
        area = self.lado * self.lado
        return area

quadrado1 = Quadrado(5)

print(f"Tamanho do lado: {quadrado1.mostra_lado()}")
print(f"Área do quadrado: {quadrado1.area()}")

quadrado1.mudar_lado(6)

print(f"Novo tamanho do lado: {quadrado1.mostra_lado()}")
print(f"Área do quadrado: {quadrado1.area()}")
