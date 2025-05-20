class Retangulo:
    def __init__(self, ladoA , ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_lados(self, novo_ladoA , novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retorna_lados(self):
        return self.ladoA,self.ladoB

    def calcular_area(self):
        area = self.ladoA * self.ladoB
        return area

    def calcular_perimetro(self):
        perimetro = (self.ladoA + self.ladoB) * 2
        return perimetro

def calcular():
        comprimento = float(input("Comprimento (m): "))
        largura = float(input("Largura (m): "))

        retangulo = Retangulo(comprimento, largura)

        area_local = retangulo.calcular_area()
        perimetro_local = retangulo.calcular_perimetro()

        print(f"Área do local: {area_local:.2f} m²")
        print(f"Perímetro do local: {perimetro_local:.2f} m")

calcular()

