# Exercício Python #102 - Função para Fatorial - Aula 00 até 21 - Mundo 3
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def valor_valido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Apenas valores numéricos.')


def mostrar():
	while True:
		print('Exibir o cálculo?')
		continuar = input('[S] SIM [N] NÃO').strip().upper()
		if continuar not in ['S', 'N']:
			print('Digite S ou N')
		else:
			if continuar == 'S':
				return True
			else:
				return False


def fatorial(valor, mostrar_calculo):
	"""
	Calcula o fatorial de um número
	:param valor: número a ser calculado
	:param mostrar_calculo: exibe ou não o cálculo
	"""
	resultado = 1
	if mostrar_calculo:
		print(f'{valor}! = ', end='')
		for i in range(valor, 0, -1):
			print(i, end=' x ' if i > 1 else f' = ')
			resultado *= i
		print(resultado)
	else:
		for i in range(valor, 0, -1):
			resultado *= i
		print(f'{valor}! = {resultado}')


fatorial(valor_valido('Digite o número a calcular... '), mostrar())



# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que criar uma função chamada fatorial() que vai receber dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. Se show for True, o cálculo será exibido. Se show for False, apenas o resultado será exibido.

# Vamos alterar um pouco em relação ao exercício do vídeo do professor. Vamos criar uma função chamada mostrar() que vai perguntar ao usuário se ele quer exibir o cálculo ou não. Se ele digitar S, o cálculo será exibido. Se ele digitar N, apenas o resultado será exibido.
def valor_valido(mensagem):
	while True:
    # Ainda não vimos o uso de try e except, mas é uma forma de tratar exceções. Se o usuário digitar um valor que não seja numérico, o programa vai exibir uma mensagem de erro e pedir para digitar novamente. Se o bloco try for executado com sucesso, o programa vai retornar o valor digitado pelo usuário.
		try:
			return int(input(mensagem))
		except ValueError:
			print('Apenas valores numéricos.')

def mostrar():
	while True:
		print('Exibir o cálculo?')
		continuar = input('[S] SIM [N] NÃO').strip().upper()
		if continuar not in ['S', 'N']:
			print('Digite S ou N')
		else:
			if continuar == 'S':
				return True
			else:
				return False

# Já fizemos um exercício para mostrar o fatorial de um número. Aqui nós apenas criamos uma função para isso
def fatorial(valor, mostrar_calculo):
	"""
	Calcula o fatorial de um número
	:param valor: número a ser calculado
	:param mostrar_calculo: exibe ou não o cálculo
	"""
	resultado = 1
	if mostrar_calculo:
		print(f'{valor}! = ', end='')
		for i in range(valor, 0, -1):
			print(i, end=' x ' if i > 1 else f' = ')
			resultado *= i
		print(resultado)
	else:
		for i in range(valor, 0, -1):
			resultado *= i
		print(f'{valor}! = {resultado}')

# Por fim, vamos chamar a função fatorial() passando o número a ser calculado e o valor lógico que indica se o cálculo deve ser exibido ou não.
fatorial(valor_valido('Digite o número a calcular... '), mostrar())

# Entenda, usamos duas funções para definir os parâmetros de outra função. Isso é completamente comum