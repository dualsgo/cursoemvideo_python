# Exercício Python #082 - Dividindo valores em várias listas - Aula 00 até 17 - Mundo 3
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


def obter_valores_válidos(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Valor inválido!')


lista_de_valores = []
while True:
	lista_de_valores.append(obter_valores_válidos('Digite um valor: '))
	while True:
		continuar = input('Outro valor? S/N ').strip().upper()
		if continuar in 'SN':
			break

	if continuar == 'N':
		break


pares = [valor for valor in lista_de_valores if valor % 2 == 0]
ímpares = [valor for valor in lista_de_valores if valor not in pares]

print('Lista principal:')
for i, v in enumerate(lista_de_valores, 1):
	print(v, end=', ' if i < len(lista_de_valores) else '.')
print('\nLista de números pares:')
for i, v in enumerate(pares, 1):
	if pares:
		print(v, end=', ' if i < len(pares) else '.')
	else:
		print('Lista vazia!')
print('\nLista de números ímpares:')
for i, v in enumerate(ímpares, 1):
	if ímpares:
		print(v, end=', ' if i < len(ímpares) else '.')
	else:
		print('Lista vazia!')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que vai ler vários números e colocar em uma lista. Depois disso, o programa deve criar duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, o programa deve mostrar o conteúdo das três listas geradas.

# Para solucionar este exercício, podemos usar list comprehension. List comprehension é uma forma de criar listas de forma mais compacta. Vamos criar uma lista principal com os valores digitados pelo usuário. Em seguida, vamos criar duas listas extras, uma para armazenar os valores pares e outra para armazenar os valores ímpares.

# Primeiro, vamos criar com list comprehension solicitar os valores ao usuário e adicionar na lista principal.
lista_de_valores = [int(input('Digite um valor: ')) for _ in range(5)]

# Em seguida, vamos criar duas listas extras, uma para armazenar os valores pares e outra para armazenar os valores ímpares.
pares = [valor for valor in lista_de_valores if valor % 2 == 0]
ímpares = [valor for valor in lista_de_valores if valor not in pares]

# A seguir, vamos exibir o conteúdo das três listas geradas.
print('Lista principal:')
for i, v in enumerate(lista_de_valores, 1):
	print(v, end=', ' if i < len(lista_de_valores) else '.')

print('\nLista de números pares:')
for i, v in enumerate(pares, 1):
	if pares:
		print(v, end=', ' if i < len(pares) else '.')
	else:
		print('Lista vazia!')

print('\nLista de números ímpares:')
for i, v in enumerate(ímpares, 1):
	if ímpares:
		print(v, end=', ' if i < len(ímpares) else '.')
	else:
		print('Lista vazia!')
