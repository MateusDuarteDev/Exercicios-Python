class ContaCorrente:
    def __init__(self,numero_conta,correntista,saldo=0):
        self.numero_conta = numero_conta
        self.correntista = correntista
        self.saldo = saldo

    def alterarCorrentista(self,novo_nome):
        self.correntista = novo_nome

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor

    def __str__(self):
        return f'''\nNúmero da Conta: {self.numero_conta}, 
Correntista: {self.correntista}, 
Saldo: R$ {self.saldo}'''

conta1 = ContaCorrente (1234,'João')
print(conta1)

conta1.deposito(1000)
print(f"\nApós depósito de R$ 1000,00: {conta1}\n")

conta1.saque(200)


print(f"Após saque de R$ 200,00: {conta1}\n")

conta1.alterarCorrentista("Pedro")
print(f"Após alterar nome: {conta1}\n")