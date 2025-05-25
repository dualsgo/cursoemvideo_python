# Exercício Python #078 - Maior e Menor valores na Lista - Aula 00 até 17 - Mundo 3
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


def obter_valores(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print(f'Ops, apenas valores numéricos...')


valores = [obter_valores(f'Digite o {i}º valor: ') for i, valor in enumerate(range(5), 1)]

print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == max(valores):
		print(índice, end='... ')

print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == min(valores):
		print(índice, end='... ')

# Versão 2

from random import randint

lista = [randint(1, 10) for valores in range(5)]
posições_maior = []
posições_menor = []

maior = max(lista)
menor = min(lista)

for posição, valor in enumerate(lista, 1):
	if valor == maior:
		posições_maior.append(posição)
	if valor == menor:
		posições_menor.append(posição)

print(f'O maior valor é o {maior}: Apareceu nas posições: {posições_maior}')
print(f'O menor valor é o {menor}: Apareceu nas posições: {posições_menor}')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, o programa deve mostrar qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.c

# Se tratando de criar listas, um método interessante é usar list comprehension. Vamos criar uma lista com 5 valores numéricos digitados pelo usuário.

# list comprehension é uma forma de criar listas de forma mais compacta. A sintaxe é: 
# nome_da_lista = [expressão for item in iterável]

# Vamos criar uma lista com 5 valores numéricos digitados pelo usuário.
valores = [int(input(f'Digite o {i}º valor: ')) for i in range(1, 6)]

# Como estamos usando um laço de repetição, só precisamos de um comando para adicionar os valores na lista.
# Dessa forma não precisamos criar uma lista vazia e usar o método append() para adicionar os valores.

# Vamos exibir a lista de valores digitados.
print(valores) # Os valroes serão exibidos em forma de lista, entre colchetes e separados por vírgula.

# Se quisermos separar os valores por reticências, podemos usar um laço de repetição.
# Vamos exibir os valores digitados separados por reticências.
for índice, valor in enumerate(valores, 1):
	print(valor, end='... ' if índice < len(valores) else '') # Exibindo os valores. Se o índice for menor que o tamanho da lista, exibimos reticências, senão, exibimos nada.

# Para saber o maior e o menor valor respectivamente, podemos usar as funções max() e min().
# min() retorna o menor valor de uma lista, e max() retorna o maior valor de uma lista.

# Vamos exibir o maior e o menor valor digitado.
print(f'\nO maior valor digitado foi {max(valores)}')
print(f'O menor valor digitado foi {min(valores)}')

# Para saber a posição do maior e do menor valor, podemos usar o método enumerate().
# enumerate() retorna um objeto enumerado. A função enumerate() pega um iterável (por exemplo, uma lista) e o transforma em um objeto enumerado. A função retorna um objeto enumerate que produz uma série de tuplas, e cada tupla é um par índice-valor.

# Vamos exibir a posição do maior e do menor valor digitado.
print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == max(valores):
		print(índice, end='... ')

print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')
for índice, valor in enumerate(valores, 1):
	if valor == min(valores):
		print(índice, end='... ')

