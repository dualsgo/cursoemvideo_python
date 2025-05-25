# Exercício Python #063 - Sequência de Fibonacci v1.0 - Aula 00 até 14 - Mundo 2
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

while True:
	try:
		elementos = int(input('Digite a quantidade de elementos que deseja visualizar: '))
		primeiro = 0
		segundo = 1
		enéssimo = elementos
		for e in range(enéssimo):
			próximo = primeiro + segundo
			print(primeiro, end=' - ' if e < enéssimo -1 else ' - FIM!')
			primeiro, segundo = segundo, primeiro + segundo
		break
	except ValueError:
		print('Este valor é de um tipo inválido para essa operação. Tente novamente')

"""
for i in range(termos):

	if i == 0:
		a = i
		print(a, end=' - ')
	elif i == 1:
		b = i
		print(b, end=' - ')
	else:
		termo = a + b
		a = b
		b = termo
		print(termo, end=' ⮕ ' if i < termos-1 else ' ⮕ FIM!')"""

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos escrever um programa que lê um número inteiro N e mostra os N primeiros elementos da Sequência de Fibonacci.

# Uma sequência de Fibonacci é uma sequência de números inteiros em que cada número é a soma dos dois anteriores. Os primeiros números da sequência são 0 e 1, e os próximos números são obtidos somando os dois anteriores. A fórmula geral da sequência de Fibonacci é Fn = Fn-1 + Fn-2, onde Fn é o enésimo termo da sequência.

# Vamos solicitar ao usuário que digite a quantidade de elementos que deseja visualizar da sequência de Fibonacci. Em seguida, vamos usar um laço de repetição for para calcular e mostrar os N primeiros elementos da sequência.

elementos = int(input('Digite a quantidade de elementos que deseja visualizar: '))  # Solicita ao usuário que digite a quantidade de elementos da sequência de Fibonacci.
primeiro = 0  # Inicializa o primeiro termo da sequência de Fibonacci.
segundo = 1  # Inicializa o segundo termo da sequência de Fibonacci.

# Usamos um laço de repetição for para calcular e mostrar os N primeiros elementos da sequência de Fibonacci.
while elementos > 0:  # Enquanto houver elementos a serem mostrados, o laço de repetição continuará.
	próximo = primeiro + segundo  # Calcula o próximo termo da sequência de Fibonacci somando o primeiro e o segundo termo.
	print(primeiro, end=' - ' if elementos > 1 else ' - FIM!')  # Exibe o termo atual e a seta se houver mais elementos a serem mostrados, senão, exibe o termo atual e a seta com a palavra FIM.
	
	primeiro, segundo = segundo, primeiro + segundo  # Atualiza os termos da sequência de Fibonacci para o próximo cálculo.
    # Repare que usamos a técnica de desempacotamento de tuplas para atualizar os termos da sequência de Fibonacci. Isso permite que os valores sejam atualizados simultaneamente sem a necessidade de variáveis temporárias. O primeiro termo recebe o valor do segundo termo e o segundo termo recebe a soma dos dois termos.

	elementos -= 1  # Decrementa o número de elementos a serem mostrados.
	
	# Usamos uma estrutura condicional dentro do print() para decidir se mostramos a seta ou a palavra FIM. Se houver mais elementos a serem mostrados, mostramos o termo atual e a seta, senão, mostramos o termo atual e a seta com a palavra FIM.
	# a sintaxe é bloco_true if condição else bloco_false. Se a condição for verdadeira, o bloco_true é executado, senão, o bloco_false é executado.