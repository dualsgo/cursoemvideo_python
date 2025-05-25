# Exercício Python #101 - Funções para votação - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def valor_valido(mensagem):
	while True:
		try:
			entrada = int(input(mensagem))
			if 1924 < entrada < 2024:
				return entrada
			else:
				print('Ano fora do intervalo permitido...')
		except ValueError:
			print('Apenas valores numéricos!')


def voto(ano_de_nascimento):
	idade = 2024 - ano_de_nascimento
	if idade < 16:
		print(f'Idade: {idade} anos - Não tem idade suficiente para votar!')
	elif idade == 16 or idade == 17 or idade > 70:
		print(f'Idade: {idade} anos - Voto facultativo!')
	else:
		print(f'Idade: {idade} anos - Voto obrigatório!')


voto(valor_valido('Digite o seu ano de nascimento: '))

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que criar uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# Primeiramente, vamos receber o ano de nascimento do usuário. Para isso, vamos criar uma função chamada valor_valido() que vai receber uma mensagem como parâmetro e vai retornar um valor inteiro válido.
def valor_valido(mensagem):
	while True:
		try:
			entrada = int(input(mensagem))
			if 1924 < entrada < 2024:
				return entrada
			else:
				print('Ano fora do intervalo permitido...')
		except ValueError:
			print('Apenas valores numéricos!')

# Essa estrutura garante que o usuário só vai digitar um valor numérico válido. O ano de nascimento deve estar entre 1924 e 2024. Você pode alterar esses valores se quiser ou remover essa verificação.

# Agora, vamos criar a função voto() que vai receber o ano de nascimento como parâmetro e vai retornar se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO.
def voto(ano_de_nascimento):
	idade = 2024 - ano_de_nascimento
	if idade < 16:
		print(f'Idade: {idade} anos - Não tem idade suficiente para votar!')
	elif idade == 16 or idade == 17 or idade > 70:
		print(f'Idade: {idade} anos - Voto facultativo!')
	else:
		print(f'Idade: {idade} anos - Voto obrigatório!')


# Por fim, vamos chamar a função voto() passando o ano de nascimento que foi validado pela função valor_valido().
voto(valor_valido('Digite o seu ano de nascimento: '))