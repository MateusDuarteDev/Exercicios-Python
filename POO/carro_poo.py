"""
- Resolva o exercício usando os conceitos de Programação Orientada a Objetos (POO) e a linguagem de programação Python.



1. Crie uma classe com o método construtor (__init__) e pelo menos quatro atributos.

2. Crie os métodos gets e sets de todos os atributos.

3. Crie o método mostra dados usando os atributos da classe.

4. Crie o método retorna dados para retornar todos os atributos da classe.

5. No método main, teste (use) a classe criada, crie (instancie) pelo menos três objetos dessa classe e use (chame) todos os métodos desenvolvidos na classe.

"""

class Carro:
    def __init__(self, modelo, marca, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
    def get_modelo(self):
        return self.modelo
    def get_marca(self):
        return self.marca
    def get_ano(self):
        return self.ano
    def get_cor(self):
        return self.cor
    def set_modelo(self,novo_modelo):
        self.modelo = novo_modelo
    def set_marca(self,nova_marca):
        self.marca = nova_marca
    def set_ano(self,nova_ano):
        self.ano = nova_ano
    def set_cor(self,nova_cor):
        self.cor = nova_cor
    def mostra_dados(self):
        print("- Mostra Dados : ")
        print("Modelo :",self.modelo)
        print("Marca :",self.marca)
        print("Ano :",self.ano)
        print("Cor :", self.cor,"\n")
    def aumento_mensalidade_valor(self,aumento):
        self.mensalidade += aumento

if __name__ == '__main__':
     carro1 = Carro('HB20', 'Hyundai', 2020, 'Branco')
     print(carro1)
     carro2 = Carro('Ka', 'Ford', 2017,'Prata')
     print(carro2)
     carro3 = Carro('Gol', 'Volkswagen', 2010,'Vermelho')
     print(carro3)

     print("- Carro 1 : ")
     print("Modelo :", carro1.get_modelo())
     print("Marca :", carro1.get_marca())
     print("Ano :", carro1.get_ano())
     print("Cor :", carro1.get_cor())
     print("- Carro 2 : ")
     print("Modelo :", carro2.get_modelo())
     print("Marca :", carro2.get_marca())
     print("Ano :", carro2.get_ano())
     print("Cor :", carro2.get_cor())
     print("- Carro 3 : ")
     print("Modelo :", carro3.get_modelo())
     print("Marca :", carro3.get_marca())
     print("Ano :", carro3.get_ano())
     print("Cor :", carro3.get_cor())

     carro1.set_modelo('Veloster')
     print("Modelo alterado :", carro1.get_modelo())
     carro2.set_cor('Chumbo')
     print("Cor alterada :", carro2.get_cor())
     carro3.set_ano(2014)
     print("Ano alterado :", carro1.get_ano(),"\n")

     carro1.mostra_dados()
     carro2.mostra_dados()
     carro3.mostra_dados()
