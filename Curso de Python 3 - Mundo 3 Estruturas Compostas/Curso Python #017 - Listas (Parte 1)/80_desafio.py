# Exercício Python #080 - Lista ordenada sem repetições - Aula 00 até 17 - Mundo 3
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Versão -
def obter_valor_válido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Valor inválido!')


lista = []

for i in range(5):
	valor = obter_valor_válido('Digite um valor: ')
	if i == 0 or valor >= lista[-1]:
		lista.append(valor)
	else:
		pos = 0
		while pos < len(lista):
			if valor <= lista[pos]:
				lista.insert(pos, valor)
				break
			pos += 1

	posição = lista.index(valor)
	print(f'Valor {valor} adicionado na posição {posição}')
	print(lista)
	print(lista)


# Minha solução - Melhor
lista = []

for r in range(5):
	valor = int(input('Valor: '))
	if r == 0:
		lista.append(valor)
		print('Primeiro valor adicionado!')
	else:
		if valor > lista[-1]:
			lista.append(valor)
			print(f'Valor adicionado no fim da lista.')
		elif valor < lista[0]:
			lista.insert(0, valor)
			print('Valor adicionado no início da lista.')
		else:
			for i in range(len(lista) - 1):
				if lista[i] < valor <= lista[i + 1]:
					lista.insert(i + 1, valor)
					print(f'Valor adicionado na posição {i + 1}')
					break
print(lista)

# Solução GPT
from random import randint

numeros_ordenados = []

for _ in range(0, 5):
	novo_numero = randint(0, 99)

	if not numeros_ordenados or novo_numero > numeros_ordenados[-1]:
		numeros_ordenados.append(novo_numero)
		print(f'Número {novo_numero} adicionado ao final da lista.')
	else:
		posicao = 0

		while posicao < len(numeros_ordenados):
			if novo_numero <= numeros_ordenados[posicao]:
				numeros_ordenados.insert(posicao, novo_numero)
				print(f'Número {novo_numero} adicionado na posição {posicao} da lista.')
				break
			posicao += 1

print(f'Os números gerados em ordem foram: {numeros_ordenados}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, o programa deve mostrar a lista ordenada na tela.

# append() é um método que adiciona um item ao final da lista. Se quisermos adicionar um item em uma posição específica da lista, podemos usar o método insert(). A sintaxe é: lista.insert(posição, valor). Onde posição é a posição que queremos adicionar o valor e valor é o valor que queremos adicionar.

# Para resolver esse exercício, teremos que avaliar a posição correta para adicionar o valor na lista. Se o valor for o primeiro da lista ou maior que o último valor da lista, adicionamos o valor no final da lista. Se não for o primeiro valor ou maior que o último valor da lista, avaliamos a posição correta para adicionar o valor.

for i in range(5):
	valor = int(input('Digite um valor: '))

	if i == 0 or valor >= lista[-1]: # Se for o primeiro valor ou maior que o último valor da lista, adicionar o valor no final da lista.
		lista.append(valor)
		print(f'Valor {valor} adicionado no final da lista.')

	else: # Se não for o primeiro valor ou maior que o último valor da lista, avaliar a posição correta para adicionar o valor.
		pos = 0 # Inicializando a variável pos com 0.

		while pos < len(lista): # Enquanto pos for menor que o tamanho da lista, fazer:

			if valor <= lista[pos]: # Se o valor for menor ou igual ao valor na posição pos da lista, adicionar o valor na posição pos da lista.
				lista.insert(pos, valor) # Adicionando o valor na posição pos da lista.
				break
			pos += 1 # Incrementando a variável pos.

# Se você resolveu o exercício usando outra lógica, parabéns! Se a sua resposta ficou maior ou mais complexa, não tem problema. O importante é entender a lógica por trás da solução. Futuramente, você poderá refatorar o código e deixá-lo mais simples e enxuto.