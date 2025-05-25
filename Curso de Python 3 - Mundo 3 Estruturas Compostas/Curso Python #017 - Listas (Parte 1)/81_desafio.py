# Exercício Python #081 - Extraindo dados de uma Lista - Aula 00 até 17 - Mundo 3
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


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

print(f'A lista com {len(lista_de_valores)} valores em ordem decrescente é: ')
lista_de_valores.sort(reverse=True)
for i, v in enumerate(lista_de_valores, 1):
	print(v, end=', ' if i < len(lista_de_valores) else '.')
print(f'\nO valor 5 {f'não ' if 5 not in lista_de_valores else ''}está na lista!')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que vai ler vários números e colocar em uma lista. Depois disso, o programa deve mostrar:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# Para solucionar este exercício, podemos usar métodos como append() e sort(). O método append() adiciona um item ao final da lista. O método sort() ordena a lista em ordem crescente. Se quisermos ordenar a lista em ordem decrescente, podemos usar o parâmetro reverse=True. Para saber se um valor está na lista, podemos usar o operador in.

# Primeiro, vamos criar uma lista vazia para armazenar os valores.
lista_de_valores = []

# Em seguida vamos criar um laço de repetição para adicionar os valores na lista. Como o usuário pode digitar vários valores, vamos usar um laço while True para continuar solicitando valores ao usuário até que ele decida parar.

# OBS.: Aqui poderíamos criar uma variável para armazenar a quantidade de valores digitados, mas como a lista tem o método len(), podemos usá-lo para obter a quantidade de valores digitados.

while True:
	valor = int(input('Digite um valor: ')) # Solicitando um valor numérico ao usuário.
	lista_de_valores.append(valor) # Adicionando o valor na lista.
	while True:
		continuar = input('Outro valor? S/N ').strip().upper() # Perguntando se o usuário deseja continuar.
		if continuar in 'SN': # Se a resposta for S ou N, sair do laço.
			break
	if continuar == 'N': # Se a resposta for N, sair do laço.
		break

# Quando o usuário decidir parar de digitar valores, vamos exibir a quantidade de valores digitados.
print(f'A lista com {len(lista_de_valores)} valores em ordem decrescente é: ')
print(sorted(lista_de_valores, reverse=True)) # Exibindo a lista de valores em ordem decrescente.
print(f'O valor 5 {f"não " if 5 not in lista_de_valores else ""}está na lista!') # Exibindo se o valor 5 está ou não na lista.

# Obs.: Também seria possível exibir os elementos da lista em ordem decrescente usando a notação de fatiamento lista[::-1]. A expressão lista[::-1] retorna uma nova lista com os elementos da lista original em ordem inversa. A expressão lista[::-1] é equivalente a lista.reverse(). A diferença é que lista.reverse() altera a lista original, enquanto lista[::-1] retorna uma nova lista com os elementos em ordem inversa.

# Mas atenção, essa exibição será de trás para frente e não garante que os itens estejam em ordem decrescente. Para garantir que os itens estejam em ordem decrescente, é melhor usar o método sort() com o parâmetro reverse=True. Ou ordenar a lista em ordem crescente e exibir a lista de trás para frente.

# Exemplo:

# Primeiro caso:
lista = [1, 2, 3, 4, 5]
print(lista[::-1]) # Exibindo a lista de trás para frente.
# Saída: [5, 4, 3, 2, 1]

# Segundo caso:
lista = [2, 1, 3, 5, 4]
print(lista[::-1]) # Exibindo a lista de trás para frente.
# Saída: [4, 5, 3, 1, 2]

# Teríamos que ordenar a lista antes de exibir a lista de trás para frente.
lista.sort()
print(lista[::-1]) # Exibindo a lista de trás para frente.
# Saída: [5, 4, 3, 2, 1]