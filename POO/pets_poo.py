class Pet(object):
    def __init__(self,nome,especie,raça,preço):
        self.nome = nome
        self.especie = especie
        self.raça = raça
        self.preço = preço
    def get_nome(self):
        return self.nome
    def get_especie(self):
        return self.especie
    def get_raça(self):
        return self.raça
    def get_preço(self):
        return self.preço
    def set_nome(self,nome):
        self.nome = nome
    def set_especie(self,especie):
        self.especie = especie
    def set_raça(self, raça):
        self.raça = raça
    def set_preço(self,preço):
        self.preço = preço
    def mostra_dados(self):
        print('\nMostra dados completos : ')
        print('Nome: ',self.nome)
        print('Espécie: ',self.especie)
        print('Raça: ',self.raça)
        print ('Preço: ',self.preço,'\n')

    def atualiza_preço(self,atualiza):
        self.preço += atualiza

if __name__ == '__main__' :
    pet1 = Pet("Belinha", "Cachorro", "Poodle",1500.00)
    pet2 = Pet("Logan", "Gato","SRD", 100.00)

    print("Objeto criado : ",pet1)
    print("Objeto criado : ",pet2)

    pet1.mostra_dados()
    pet2.mostra_dados()

    pet1.set_raça("Yorkshire")
    print("Raça alterada Pet 1 : ", pet1.get_raça())
    pet2.set_nome("Pascoal")
    print("Nome alterado Pet 2 : ", pet2.get_nome())

    pet1.mostra_dados()
    pet2.mostra_dados()

    atualiza = int(input("Digite o aumento do valor do animal : "))
    pet1.atualiza_preço(atualiza)
    pet2.atualiza_preço(atualiza)

    print("Novo valor do pet : ", pet1.get_preço())
    print("Novo valor do pet : ", pet2.get_preço())




