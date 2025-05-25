# Exercício Python #103 - Ficha do Jogador - Aula 00 até 21 - Mundo 3
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def nome_valido(mensagem):
	while True:
		entrada = input(mensagem).strip().title()
		if entrada.replace(' ', '').isalpha():
			return entrada
		else:
			print('Nome inválido. Nao são permitidos números nem caracteres especiais.')


def valor_valido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Apenas valores numéricos.')


def ficha(nome, gols):
	print(f'{'-'*33}')
	print(f'|{'JOGADOR':^15}|{'GOLS MARCADOS':^15}|')
	print(f'{'-'*33}')
	print(f'|{nome:^15}|{gols:^15}|')
	print(f'{'-'*33}')


ficha(nome_valido('Digite o nome do jogador: '), valor_valido('Digite a quantidade de gols marcados: '))

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que criar uma função chamada ficha() que vai receber dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# Primeiramente, vamos criar uma função chamada nome_valido() que vai receber uma mensagem como parâmetro e vai retornar um nome válido. O nome não pode conter números nem caracteres especiais.
def nome_valido(mensagem):
	while True:
		entrada = input(mensagem).strip().title()
		if entrada.replace(' ', '').isalpha():
			return entrada
		else:
			print('Nome inválido. Nao são permitidos números nem caracteres especiais.')

# Agora, vamos criar uma função chamada valor_valido() que vai receber uma mensagem como parâmetro e vai retornar um valor inteiro válido. Essa função é para garantir a digitação de um valor numérico.
def valor_valido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Apenas valores numéricos.')

# Por fim, vamos criar a função ficha() que vai receber o nome e a quantidade de gols marcados como parâmetros e vai exibir a ficha do jogador.

def ficha(nome, gols):
	print(f'{"-"*33}')
	print(f'|{"JOGADOR":^15}|{"GOLS MARCADOS":^15}|')
	print(f'{"-"*33}')
	print(f'|{nome:^15}|{gols:^15}|')
	print(f'{"-"*33}')

# Por fim, vamos chamar a função ficha() passando o nome do jogador e a quantidade de gols marcados que foram validados pelas funções nome_valido() e valor_valido().
# ficha(nome_valido('Digite o nome do jogador: '), valor_valido('Digite a quantidade de gols marcados: '))

# Agora vamos fazer uma versão que atenda ao enunciado do exercício. Se o usuário não informar o nome do jogador, o programa vai considerar o nome como desconhecido. Se o usuário não informar a quantidade de gols marcados, o programa vai considerar que o jogador não marcou gols.
def ficha(nome='Desconhecido', gols=0):
	print(f'{"-"*33}')
	print(f'|{"JOGADOR":^15}|{"GOLS MARCADOS":^15}|')
	print(f'{"-"*33}')
	print(f'|{nome:^15}|{gols:^15}|')
	print(f'{"-"*33}')


ficha(input('Digite o nome do jogador: ').strip().title(), int(input('Digite a quantidade de gols marcados: ')))