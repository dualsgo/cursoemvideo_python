# Exercício Python #104 - Validando entrada de dados em Python - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leia_int(mensagem):
	while True:
		valor = input(mensagem)
		try:
			float(valor)
			print(f'Você digitou o valor: {valor}')
			break
		except ValueError:
			print('Este valor não é um número.')


leia_int('Digite um valor inteiro: ')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que criar uma função chamada leiaInt() que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
def leia_int(mensagem):
	while True:
		valor = input(mensagem)
		if valor.isnumeric():
			print(f'Você digitou o valor: {valor}')
			break
		else:
			print('Este valor não é um número inteiro.')

# A função isnumeric() verifica se a string contém apenas números. Se o valor digitado pelo usuário for um número, o programa vai exibir a mensagem 'Você digitou o valor: {valor}' e vai encerrar o loop com o break. Se o valor digitado pelo usuário não for um número, o programa vai exibir a mensagem 'Este valor não é um número.' e o loop vai continuar.

# Por fim, vamos chamar a função leiaInt() passando a mensagem 'Digite um valor inteiro: '.
leia_int('Digite um valor inteiro: ')