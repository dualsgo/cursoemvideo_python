# Exercício Python #070 - Estatísticas em produtos - Aula 00 até 15 - Mundo 2
#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

cadastros = quantidade_produtos_mais_mil = valor_total = valor_produto_mais_mil = 0
descrição_mais_barato = descrição_produto_mais_mil = ''
valor_produto_mais_barato = float('+inf')
def obter_preço(mensagem):
	try:
		return float(input(mensagem))
	except ValueError:
		print('Dados inválidos')


print(f'{'-'*30}')
print(f'{'CADASTRO DE PRODUTOS':^30}')
print(f'{'-'*30}')

while True:
	descrição = input('Descrição do produto: ').strip().upper()
	valor = obter_preço('Valor do produto: R$ ')

	if valor < valor_produto_mais_barato: # type: ignore
		valor_produto_mais_barato = valor
		descrição_mais_barato = descrição

	if valor > 1000: # type: ignore
		quantidade_produtos_mais_mil += 1
		descrição_produto_mais_mil = descrição
		valor_produto_mais_mil = valor
	print('Cadastro realizado com sucesso!')
	print(f'{'Descrição:':<20}{descrição:>25}\n{'Valor:':<20}{f'{'R$':>15}{valor:>10.2f}'}')
	print(f'{'-' * 45}')
	valor_total += valor # type: ignore
	continuar = input('Digite S para continuar ou N para encerrar: S / N').strip().upper()
	while continuar not in ['S', 'N']:
		print('Você escolheu uma opção inválida@!')
		continuar = input('Digite S para continuar ou N para encerrar: S / N').strip().upper()
	print(f'{'-' * 45}')
	if continuar == 'S':
		print('Próximo cadastro: ')

	else:
		print('Encerrando o programa...')
		break

print(f'{'-' * 45}')
print(f'{'VALOR TOTAL':^45}')
print(f'{'-' * 45}')
print(f'{'Valor total:':<30}{f'{'R$':>5}{valor_total:>10.2f}'}')
print(f'{'-' * 45}')
print(f'{'Produtos que custam mais de MIL REAIS:':<40} {quantidade_produtos_mais_mil:>5}')
print(f'{'-' * 45}')
print(f'{'PRODUTO MAIS BARATO':^45}')
print(f'{'Descrição:':<20}{descrição_mais_barato:>25}\n{'Valor:':<20}{f'{'R$':>15}{valor_produto_mais_barato:>10.2f}'}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, o programa deve mostrar:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Primeiro vamos criar as variáveis que serão utilizadas no programa.

# cadastros: contador de produtos cadastrados.
cadastros = 0	
# quantidade_produtos_mais_mil: contador de produtos que custam mais de R$1000.
quantidade_produtos_mais_mil = 0
# valor_total: acumulador do valor total gasto na compra.
valor_total = 0
# valor_produto_mais_mil: valor do produto mais caro.
valor_produto_mais_mil = 0
# descrição_mais_barato: nome do produto mais barato. Será inicializado com uma string vazia.
descrição_mais_barato = ''
# descrição_produto_mais_mil: nome do produto mais caro. Será inicializado com uma string vazia.
descrição_produto_mais_mil = ''
# valor_produto_mais_barato: valor do produto mais barato. Será inicializado com infinito, assim qualquer valor digitado será menor que ele.
valor_produto_mais_barato = float('+inf')

# NOTA: Para as variáveis que iniciaram com zero, poderemos também atribuir em uma linha só
# cadastros, quantidade_produtos_mais_mil, valor_total, valor_produto_mais_mil = 0, 0, 0, 0
# ou cadastros = quantidade_produtos_mais_mil = valor_total = valor_produto_mais_mil = 0

# Seguindo com o código, vamos inciar o programa com um cabeçalho.
print('-' * 30)
print('CADASTRO DE PRODUTOS'.center(30))
print('-' * 30)

# Vamos criar um laço while True para que o programa fique em loop até que o usuário decida encerrá-lo.
while True:
	# Dentro do laço while, vamos pedir para o usuário digitar a descrição do produto. Tratamos a descrição com o método strip() para remover espaços em branco no início e no final da string, e com o método upper() para transformar a descrição em letras maiúsculas.
	descrição = input('Descrição do produto: ').strip().upper()
	# Vamos pedir para o usuário digitar o valor do produto.
	valor = float(input('Valor do produto: R$ '))

	# Vamos verificar se o valor do produto é menor que o valor do produto mais barato.
	# Obs.: A primeira vez que o usuário digitar um valor, ele será menor que infinito, então a condição será verdadeira e isso atualizará o valor do produto mais barato.
	if valor < valor_produto_mais_barato:
		# Se for, a variável valor_produto_mais_barato vai receber o valor do produto e a variável descrição_mais_barato vai receber a descrição do produto.
		valor_produto_mais_barato = valor
		descrição_mais_barato = descrição

	# Vamos verificar se o valor do produto é maior que R$1000.
	if valor > 1000:
		# Se for, a variável quantidade_produtos_mais_mil vai receber mais 1 e as variáveis descrição_produto_mais_mil e valor_produto_mais_mil vão receber a descrição e o valor do produto.
		quantidade_produtos_mais_mil += 1
		descrição_produto_mais_mil = descrição
		valor_produto_mais_mil = valor

	# Vamos exibir uma mensagem de sucesso.
	print('Cadastro realizado com sucesso!')
	print(f'Descrição: {descrição:>25}\nValor: {"R$":>15}{valor:>10.2f}')
	print('-' * 45)

	# A variável valor_total vai acumular o valor do produto.
	valor_total += valor

	# Vamos perguntar ao usuário se ele deseja continuar.
	continuar = input('Digite S para continuar ou N para encerrar: ').strip().upper()

	# Vamos criar um laço while para garantir que o usuário digite apenas S ou N.
	while continuar not in ['S', 'N']:
		# Se a resposta for diferente de S ou N, o programa vai exibir uma mensagem de erro e pedir para o usuário digitar novamente.
		print('Você escolheu uma opção inválida!')
		continuar = input('Digite S para continuar ou N para encerrar: ').strip().upper()

	print('-' * 45)

	# Se o usuário escolher continuar, o programa vai pedir para ele fazer um novo cadastro.
	if continuar == 'S':
		print('Próximo cadastro: ')

	# Se o usuário escolher encerrar, o programa vai exibir uma mensagem de encerramento e sair do laço while.
	else:
		print('Encerrando o programa...')
		break

# Vamos exibir o valor total gasto na compra.
print('-' * 45)
print('VALOR TOTAL'.center(45))
print('-' * 45)
print(f'Valor total: {"R$":>5}{valor_total:>10.2f}')
print('-' * 45)

# Vamos exibir a quantidade de produtos que custam mais de R$1000.
print(f'Produtos que custam mais de MIL REAIS: {quantidade_produtos_mais_mil:>5}')
print('-' * 45)

# Vamos exibir o produto mais barato.
print('PRODUTO MAIS BARATO'.center(45))
print(f'Descrição: {descrição_mais_barato:>25}\nValor: {"R$":>15}{valor_produto_mais_barato:>10.2f}')
