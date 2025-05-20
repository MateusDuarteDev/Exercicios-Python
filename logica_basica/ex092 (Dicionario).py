from datetime import date
dados = {}

dados['nome'] = str(input('Nome : '))
nascimento = int(input('Ano de nascimento : '))
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem) : '))
if dados['ctps'] > 0:
    dados['contratacao'] = int(input('Ano de contratação : '))
    dados['salario'] = int(input('Salário : '))
    ano = dados['contratacao'] +35
    dados['aposentadoria'] = ano - nascimento

for k,v in dados.items():
    print(f'{k} tem o valor {v} ...')