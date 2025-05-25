# Exercício Python #076 - Lista de Preços com Tupla - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""produtos = (('Notebook', 3399.99), ('Playstation 5', 4799.99), ('TV 52', 2499.99), ('Cadeira', 999.99), ('Mesa', 699.99), ('Monitor', 1199.99), ('Iphone 15', 7999.99))

for item in produtos:
    print(item)"""

# Lista de itens do carrinho com seus respectivos preços
carrinho = ('Notebook', 3399.99, 'Playstation 5', 4799.99, 'TV 52', 2499.99, 'Cadeira', 999.99, 'Mesa', 699.99, 'Monitor', 1199.99, 'Iphone 15', 7999.99)

# Imprime a nota fiscal
print('-'*45)
print(f'{"NOTA FISCAL": ^45}')
total = 0  # Inicializa a variável total para calcular o valor total da compra
print('-'*45)

# Itera sobre os itens do carrinho e imprime a descrição e o preço
for indice, item in enumerate(carrinho):
    if indice % 2 == 0:  # Se o índice for par (posição da descrição)
        print(f'{item:.<30}', end='')  # Imprime a descrição com ponto final e alinhado à esquerda
    elif indice % 2 == 1:  # Se o índice for ímpar (posição do preço)
        print(f' R${item:>10.2f}')  # Imprime o preço alinhado à direita com duas casas decimais
        total += item  # Soma o preço ao total

# Imprime a linha final da nota fiscal
print('-'*45)

# Imprime o valor total da compra
print(f'{"Valor total": <30} R${total: >10.2f}')

# Versão 2

tupla = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

for índice, valor in enumerate(tupla, 1):
	print(f'{valor:.<15}' if índice % 2 else f'R${valor:>8.2f}\n', end='')

# Versão 3

produtos_precos = (
	"Arroz", 20.50,
	"Feijao", 8.75,
	"Macarrao", 4.20,
	"Acucar", 3.40,
	"Cafe", 12.80,
	"Leite", 5.30,
	"Manteiga", 7.90,
	"Oleo", 6.45,
	"Sal", 1.85,
	"Farinha", 4.70
)
print(f'{'-' * 30}')
print(f'{'NOTA FISCAL':^30}')
print(f'{'-' * 30}')

total = 0
for índice, produto in enumerate(produtos_precos, 1):
	if índice % 2:
		print(f'{produto:<15}', end='')
	else:
		print(f'{f'R$ {produto:5.2f}':>15}')
		total += produto
print(f'{'-' * 30}')
print(f'{'Total:':<15}{f'R$ {total:5.2f}':>15}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, o programa deve mostrar uma listagem de preços, organizando os dados em forma tabular.

# Primeiro vamos criar uma tupla com os produtos e seus respectivos preços. Você pode adicionar quantos produtos quiser.
produtos = (
	'Notebook', 3399.99,
	'Playstation 5', 4799.99,
	'TV 52', 2499.99,
	'Cadeira', 999.99,
	'Mesa', 699.99,
	'Monitor', 1199.99,
	'Iphone 15', 7999.99
)


# Vamos percorrer a tupla com um laço de repetição for e exibir os produtos e preços. Os produtos estão nos índices pares e os preços nos ímpares.

# Imprime a nota fiscal
print('-'*45)
print(f'{"NOTA FISCAL": ^45}')
total = 0  # Inicializa a variável total para calcular o valor total da compra
print('-'*45)

# Itera sobre os itens do carrinho e imprime a descrição e o preço
for indice, item in enumerate(carrinho):
    if indice % 2 == 0:  # Se o índice for par (posição da descrição)
        print(f'{item:.<30}', end='')  # Imprime a descrição com ponto final e alinhado à esquerda
    elif indice % 2 == 1:  # Se o índice for ímpar (posição do preço)
        print(f' R${item:>10.2f}')  # Imprime o preço alinhado à direita com duas casas decimais
        total += item  # Soma o preço ao total

# Imprime a linha final da nota fiscal
print('-'*45)

# Imprime o valor total da compra
print(f'{"Valor total": <30} R${total: >10.2f}')