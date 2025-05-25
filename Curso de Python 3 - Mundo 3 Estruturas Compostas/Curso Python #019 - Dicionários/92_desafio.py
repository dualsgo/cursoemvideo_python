# Exercício Python #092 - Cadastro de Trabalhador em Python - Aula 00 até 19 - Mundo 3
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
from random import randint

dados = []
ano_atual = datetime.now().year

while True:
	pessoa = {}  # Cria um novo dicionário para cada pessoa

	pessoa['nome'] = str(input('Nome: '))
	pessoa['nascimento'] = int(input('Ano de nascimento: '))
	pessoa['idade'] = ano_atual - pessoa['nascimento']

	carteira = str(input('Possui CTPS: S/N ')).strip().upper()

	while carteira not in 'SN':
		carteira = str(input('Resposta inválida: S/N ')).strip().upper()

	if carteira == 'S':
		pessoa['ctps'] = randint(1234567, 9999999)
		pessoa['contratacao'] = int(input('Ano de contratação: '))
		pessoa['salario'] = float(input('Salário: R$ '))

	dados.append(pessoa.copy())

	continuar = str(input('Continuar? S/N ')).strip().upper()

	while continuar not in 'SN':
		continuar = str(input('Continuar? S/N ')).strip().upper()

	if continuar == 'N':
		print('Encerrando...')
		break
	elif continuar == 'S':
		print('Prosseguindo...')

for pessoa in dados:
	if 'ctps' in pessoa:  # Verifica se a pessoa tem CTPS
		print(
			f"{pessoa['nome']}, nasceu em {pessoa['nascimento']} possui {pessoa['idade']} anos, porta a CTPS nº {pessoa['ctps']}. Trabalha desde {pessoa['contratacao']} com salário de R$ {pessoa['salario']:.2f} e terá que contribuir mais {35 - (ano_atual - pessoa['contratacao'])} anos para se aposentar.")
	else:
		print(
			f"{pessoa['nome']}, nascido em {pessoa['nascimento']} possui {pessoa['idade']} anos e ainda não é contribuinte.")

# V2

from datetime import datetime

atual = datetime.today().year
informacoes = dict()

informacoes['nome'] = input('Digite o nome: ').strip().title()
informacoes['nascimento'] = int(input('Digite o ano de nascimento: '))
informacoes['idade'] = atual - informacoes['nascimento']

print(f'Nome: {informacoes["nome"]}')
print(f'Ano de nascimento: {informacoes["nascimento"]}')
print(f'Idade: {informacoes["idade"]} anos')

if informacoes['idade'] >= 18:
	ctps = input('Possui CTPS? S/N: ').strip().upper()
	if ctps == 'S':
		informacoes['CTPS'] = int(input('Digite o número da CTPS: '))
		print(f'CTPS nº: {informacoes["CTPS"]}')
		if informacoes['CTPS']:
			informacoes['ano_contratacao'] = int(input('Digite o ano de contratação: '))
			informacoes['salario'] = float(input('Digite o salário: R$ '))
			informacoes['aposentadoria'] = (informacoes['ano_contratacao'] + 30) - atual

			print(f'Ano de contratação: {informacoes["ano_contratacao"]}')
			print(f'Salário: R$ {informacoes["salario"]:.2f}')
			print(f'Tempo para se aposentar: {informacoes["aposentadoria"]} anos')

# V3


from datetime import date

ano_atual = date.today().year


def print_divider():
	print('-' * 30)


def print_error(message):
	print(f'\033[1;31m{message}\033[m')


def obtem_nome():
	while True:
		print_divider()
		entrada_nome = input('Digite o nome: ').strip().title()
		print_divider()
		if entrada_nome.replace(' ', '').isalpha():
			return entrada_nome
		else:
			print_error('NOME INVÁLIDO! Apenas caracteres alfabéticos.')


def obtem_idade():
	while True:
		try:
			entrada_ano_nascimento = int(input('Digite o ano de nascimento: '))
			if not (1980 < entrada_ano_nascimento < 2006):
				print_error('Apenas maiores de 18 anos. Ano deve estar entre 1980 e 2006')
			else:
				return ano_atual - entrada_ano_nascimento
		except ValueError:
			print_error('ERRO! Apenas dados numéricos.')


def obtem_ctps():
	while True:
		try:
			primeira_parte = input('Digite os 7 dígitos iniciais: ')
			if len(primeira_parte) != 7 or not primeira_parte.isdigit():
				print_error('Deve conter 7 dígitos.')
				continue
			segunda_parte = input('Digite os 4 dígitos finais: ')
			if len(segunda_parte) != 4 or not segunda_parte.isdigit():
				print_error('Deve conter 4 dígitos.')
				continue
			return f'{primeira_parte}/{segunda_parte}'
		except ValueError:
			print_error('Dado inválido para essa operação.')


def obtem_ano_contratacao():
	while True:
		try:
			entrada_ano_contratacao = int(input('Digite o ano de contratação: '))
			if not (1980 < entrada_ano_contratacao < 2024):
				print_error('Ano deve estar entre 1980 e 2024')
			else:
				return entrada_ano_contratacao
		except ValueError:
			print_error('ERRO! Apenas dados numéricos.')


def obtem_salario():
	while True:
		try:
			entrada_salario = float(input('Digite o salário em R$: '))
			salario_formatado = f'R$ {entrada_salario:.2f}'
			return salario_formatado.replace('.', ',')
		except ValueError:
			print_error('ERRO! Apenas dados numéricos.')


def obtem_sexo():
	while True:
		print_divider()
		entrada_sexo = input('Digite o sexo:\n[M] Masculino\n[F] Feminino\nSua resposta: ').strip().upper()
		print_divider()
		if entrada_sexo == 'M':
			return 'Masculino'
		elif entrada_sexo == 'F':
			return 'Feminino'
		else:
			print_error('Opção inválida! Tente novamente.')


dados = dict()

while True:
	dados['nome'] = obtem_nome()
	dados['idade'] = obtem_idade()
	dados['sexo'] = obtem_sexo()
	carteira = input('Possui CTPS (Carteira de Trabalho e Previdência Social):\n[S] Sim\n[N] Não\nSua resposta: ').strip().upper()
	if carteira == 'S':
		dados['ctps'] = obtem_ctps()
		dados['ano_contratacao'] = obtem_ano_contratacao()
		dados['salario'] = obtem_salario()
		contribuicao = ano_atual - dados['ano_contratacao']
		idade_minima = 65 if dados['sexo'] == 'Masculino' else 62
		faltam = idade_minima - dados['idade']
		dados['contribuicao'] = contribuicao
		dados['anos_restantes'] = faltam
		print('\033[1;32mCadastro realizado com sucesso!\033[m')
	while True:
		print_divider()
		continuar = input('Deseja continuar?\n[S] Sim\n[N] Não\nSua resposta: ').strip().upper()
		print_divider()
		if continuar in ['S', 'N']:
			break
	if continuar == 'N':
		break

titulos = {
	'nome': 'Nome',
	'idade': 'Idade',
	'sexo': 'Sexo',
	'ctps': 'CTPS',
	'ano_contratacao': 'Ano de Contratação',
	'salario': 'Salário',
	'contribuicao': 'Anos de Contribuição',
	'anos_restantes': 'Anos para Aposentadoria'
}

for chave, valor in dados.items():
	titulo = titulos.get(chave, chave)
	print(f'{titulo:<30}{valor:>15}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o professor pede para criar um programa que leia o nome, o ano de nascimento e a carteira de trabalho de uma pessoa. Se a pessoa tiver carteira de trabalho, o programa deve ler o ano de contratação e o salário. No final, o programa deve mostrar o nome, a idade, o tempo de contribuição e quantos anos faltam para a pessoa se aposentar.

# Primeiramente, vamos importar a função datetime da biblioteca datetime para obter o ano atual.
from datetime import datetime

# Vamos criar uma lista vazia chamada dados para armazenar as informações das pessoas.
dados = []

# Vamos obter o ano atual com a função today().year da biblioteca datetime.
ano_atual = datetime.today().year

# Vamos criar um loop while True para solicitar as informações das pessoas.
while True:
    # Vamos criar um dicionário chamado pessoa para armazenar as informações de cada pessoa.
	pessoa = {}

	# Vamos solicitar o nome da pessoa e armazenar no dicionário pessoa.
	pessoa['nome'] = str(input('Nome: '))

	# Vamos solicitar o ano de nascimento da pessoa e armazenar no dicionário pessoa.
	pessoa['nascimento'] = int(input('Ano de nascimento: '))

	# Vamos calcular a idade da pessoa e armazenar no dicionário pessoa.
	pessoa['idade'] = ano_atual - pessoa['nascimento']

	# Vamos solicitar se a pessoa possui carteira de trabalho e armazenar na variável carteira.
	carteira = str(input('Possui CTPS: S/N ')).strip().upper()

	# Vamos criar um loop while para verificar se a resposta é válida.
	while carteira not in 'SN':
		carteira = str(input('Resposta inválida: S/N ')).strip().upper()

	# Se a pessoa possuir carteira de trabalho, vamos solicitar o número da CTPS, o ano de contratação e o salário.
	if carteira == 'S':
		# Para não ficar vamos colocar um número aleatório para a CTPS
		pessoa['ctps'] = randint(1234567, 9999999)
		# Os demais dados o usuário irá informar
		pessoa['contratacao'] = int(input('Ano de contratação: '))
		pessoa['salario'] = float(input('Salário: R$ '))

	# Vamos adicionar o dicionário pessoa à lista dados.
	dados.append(pessoa.copy())

	# Vamos perguntar se deseja continuar e armazenar na variável continuar.
	continuar = str(input('Continuar? S/N ')).strip().upper()

	# Vamos criar um loop while para verificar se a resposta é válida.
	while continuar not in 'SN':
		continuar = str(input('Continuar? S/N ')).strip().upper()

	# Se a resposta for N, vamos encerrar o programa.
	if continuar == 'N':
		print('Encerrando...')
		break

	# Se a resposta for S, vamos prosseguir com o programa.
	elif continuar == 'S':
		print('Prosseguindo...')

# Vamos percorrer a lista dados e mostrar as informações das pessoas.
for pessoa in dados:
	# Se a pessoa possuir CTPS, vamos mostrar o nome, o ano de nascimento, a idade, o número da CTPS, o ano de contratação, o salário e quantos anos faltam para se aposentar.
	if 'ctps' in pessoa:
		print(
			f"{pessoa['nome']}, nasceu em {pessoa['nascimento']} possui {pessoa['idade']} anos, porta a CTPS nº {pessoa['ctps']}. Trabalha desde {pessoa['contratacao']} com salário de R$ {pessoa['salario']:.2f} e terá que contribuir mais {35 - (ano_atual - pessoa['contratacao'])} anos para se aposentar.")
	# Se a pessoa não possuir CTPS, vamos mostrar o nome, o ano de nascimento e a idade.
	else:
		print(
			f"{pessoa['nome']}, nascido em {pessoa['nascimento']} possui {pessoa['idade']} anos e ainda não é contribuinte.")

