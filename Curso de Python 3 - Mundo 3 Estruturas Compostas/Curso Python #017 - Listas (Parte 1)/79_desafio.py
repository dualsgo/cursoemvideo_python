# Exercício Python #079 - Valores únicos em uma Lista - Aula 00 até 17 - Mundo 3
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


def adicionar_valores(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print(f'{'Apenas valores numéricos!':^30}')


lista = []

while True:
	valor = adicionar_valores(f'\033[1;34m{'Digite um valor: ':^30}\033[m')
	if valor not in lista:
		print(f'\033[1;32m{'-' * 30}')
		print(f'{'Valor adicionado!':^30}')
		print(f'{'-' * 30}\033[m')
		lista.append(valor)
	else:
		print(f'\033[1;31m{'-' * 30}')
		print('Valor repetido! Vou desconsidera-lo...')
		print(f'{'-' * 30}\033[m')
	while True:
		continuar = input(f'\033[1m{'Deseja continuar? S/N':^30}\033[m').strip().upper()
		print(f'\033[1;34m{'-' * 30}\033[m')
		if continuar not in 'SN':
			continue
		else:
			break
	if continuar == 'N':
		break

lista.sort()

print(f'Os valores digitados foram: ', end='')
for a, i in enumerate(sorted(lista), 1):
	print(i, end=', ' if a != len(lista) else '.')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Existem várias formas de resolver esse exercício.  Nossa abordagem será a seguinte: Vamos avaliar se o valor digitado já está na lista. Se não estiver, vamos adicionar o valor na lista. Se estiver, vamos desconsiderar o valor. No final, vamos exibir os valores únicos digitados, em ordem crescente.

# Primeiro, criar uma lista vazia para armazenar os valores.
lista = []

# Em seguida, vamos criar um laço de repetição para adicionar os valores na lista. Como o usuário pode digitar vários valores, vamos usar um laço while True para continuar solicitando valores ao usuário até que ele decida parar.
while True:
	valor = int(input('Digite um valor: ')) # Solicitando um valor numérico ao usuário.
	if valor not in lista: # Se o valor não estiver na lista, adicionar o valor na lista.
		print('-' * 30)
		print('Valor adicionado!')
		print('-' * 30)
		lista.append(valor)
	else: # Se o valor já estiver na lista, desconsiderar o valor.
		print('-' * 30)
		print('Valor repetido! Vou desconsidera-lo...')
		print('-' * 30)
	while True:
		continuar = input('Deseja continuar? [S/N]').strip().upper() # Perguntando se o usuário deseja continuar.
		print('-' * 30)
		if continuar not in 'SN': # Se a resposta for diferente de S ou N, continuar perguntando.
			continue
		else:
			break
	if continuar == 'N': # Se a resposta for N, sair do laço de repetição.
		break

# Vamos exibir os valores digitados em ordem crescente.
# Existem duas de ordenar a lista: usando o método sort() ou a função sorted(). 

# Um método é uma função que pertence a um objeto. O método sort() ordena a lista em ordem crescente e altera a lista original. A sintaxe é: lista.sort()

# Um função é um bloco de código que executa uma tarefa específica e pode retornar um valor ou causar um efeito colateral.
# A função sorted() ordena a lista em ordem crescente e retorna uma nova lista ordenada. A sintaxe é: sorted(lista)

# Resumindo: lista.sort() altera a lista original e sorted(lista) retorna uma nova lista ordenada.

lista.sort() # Ordenando a lista de valores.

print('Os valores digitados foram: ', end='') # Exibindo os valores digitados.
for a, i in enumerate(sorted(lista), 1):
	print(i, end=', ' if a != len(lista) else '.') # Exibindo os valores. Se o índice for diferente do tamanho da lista, exibimos uma vírgula, senão, exibimos um ponto.

# Para treinar a lógica, você pode estudar sobre o bubble sort. É um algoritmo de ordenação simples que percorre a lista várias vezes, comparando elementos adjacentes e trocando-os de posição se estiverem na ordem errada. O bubble sort é um algoritmo lento e ineficiente, mas é um bom exercício para entender como os algoritmos de ordenação funcionam.

# Vamos a um pequeno exemplo com 5 valores:
lista = [5, 3, 2, 4, 1]

# A lista está na ordem decrescente. Vamos ordenar a lista em ordem crescente usando o bubble sort.
# O bubble sort compara os elementos adjacentes e troca de posição se estiverem na ordem errada.

# Primeira passagem:
# 5 > 3? Sim. Trocar 5 por 3.
# 5 > 2? Sim. Trocar 5 por 2.
# 5 > 4? Sim. Trocar 5 por 4.
# 5 > 1? Sim. Trocar 5 por 1.
# Resultado: [3, 2, 4, 1, 5]

# Segunda passagem:
# 3 > 2? Sim. Trocar 3 por 2.
# 3 > 4? Não.
# 4 > 1? Sim. Trocar 4 por 1.
# 4 > 5? Não.
# Resultado: [2, 3, 1, 4, 5]

# Já deu para entender como o bubble sort funciona? Vamos ao código:

for i in range(len(lista)): # len(lista) retorna o tamanho da lista.
    print(i)
    for j in range(len(lista) - 1): # len(lista) - 1 para não ultrapassar o tamanho da lista.
        print(j)
        if lista[j] > lista[j + 1]: # Se o elemento atual for maior que o próximo elemento.
            lista[j], lista[j + 1] = lista[j + 1], lista[j] # Trocar os elementos de posição.

# Para ficar mais claro, veja essa versão com a explicação passo a passo:

lista = [5, 4, 3, 2, 1]

for i in range(len(lista)):
    print(f'Passagem {i + 1}:') # Exibindo o número da passagem.

    for j in range(len(lista) - 1 - i):  # A cada passagem, não precisamos verificar os últimos elementos já ordenados
        print(f'  Comparando {lista[j]} e {lista[j + 1]}...', end=' ') # Exibindo os elementos que estão sendo comparados.
        
        if lista[j] > lista[j + 1]: # Se o elemento atual for maior que o próximo elemento.
            print('Troca feita!')
            lista[j], lista[j + 1] = lista[j + 1], lista[j] # Trocando os elementos de posição.
        else: # Se o elemento atual não for maior que o próximo elemento.
            print('Sem troca.') # Exibindo que não houve troca.
        
        print(f'  Estado atual da lista: {lista}') # Exibindo o estado atual da lista.
    
    print(f'Fim da passagem {i + 1}. Lista: {lista}') # Exibindo o fim da passagem e o estado atual da lista.
    print('-' * 40)
