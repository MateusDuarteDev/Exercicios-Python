class Funcionario:
    def __init__(self,nome,departamento,salario):
        self.nome = nome
        self.departamento = departamento
        self.salario = salario
    def aumentar_salario(self):
        self.salario = self.salario*1.1
        return self.salario
    def __str__(self):
        return f'O funcionário {self.nome} do departamento {self.departamento} terá um salário de : {str(self.salario)}'

funcionario1 = Funcionario('Mateus','TI',5000)

print(funcionario1)
funcionario1.aumentar_salario()
print(funcionario1)
