# Exercício Python #033 - Maior e menor valores - Aula 00 até 09 - Mundo 1
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Versão 1 - Usando a técnica de sentinela

maior = float('-inf')
menor = float('inf')

for _ in range(1, 4):
	numero = int(input(f'Digite o {_}º valor: '))
	if numero > maior:
		maior = numero
	if numero < menor:
		menor = numero

print(f'Maior: {maior}')
print(f'Menor: {menor}')

# Versão 2 

from random import randint
# Tarefa 1: Ler três números
primeiro = randint(0, 999)
segundo = randint(0, 999)
terceiro = randint(0, 999)
maior = menor = 0

# Tarefa 2: Mostrar o maior e o menor
if primeiro < segundo < terceiro:
    print('Primeiro caso atendido')
    maior = terceiro
    menor = primeiro
if primeiro < segundo > terceiro:
    print('Segundo caso atendido')
    maior = segundo
    if primeiro > terceiro:
        menor = terceiro
    else:
        menor = primeiro
if primeiro > segundo > terceiro:
    print('Terceiro caso atendido')
    maior = primeiro
    if segundo > terceiro:
        menor = terceiro
    else:
        menor = primeiro
if primeiro > segundo < terceiro:
    print('Quarto caso atendido')
    menor = segundo
    if primeiro > terceiro:
        maior = primeiro
    else:
        maior = terceiro

print(f'Entre {primeiro}, {segundo} e {terceiro}.')
print(f'O maior é {maior} e o menor {menor}.')


# Se limitando ao conteúdo até a aula atual:

# Podemos diminuir o número de verificações se considerarmos o primeiro valor como maior e menor
maior = menor = a = int(input('A= '))
b = int(input('B= '))
c = int(input('C= '))

# Depois só precisamos comparar se o segundo é maior que o maior, que atualmente é o valor do primeiro. Se for maior atualizamos, se for menor ou igual fazemos a mesma verificação para o terceiro
if b > maior:
	maior = b
if c > maior:
	maior = c

# Faremos as mesmas verificações para descobrir e precisamos atualizar o menor valor
if b < menor:
	menor = b
if c < menor:
	menor = c

print(f'Maior {maior}\nMenor {menor}')

# Nessa versão usamos um pouco mais de conhecimentos e adicionamos tratamento de erro. Se o primeiro valor for inválido, o programa pede que digite novamente, porém se o usuário digitar o segundo ou o terceiro valor inválido, os anteriores serão perdidos e terá que digitar todos novamente
while True:
	try:
		maior = menor = número = int(input('Digite um valor: '))

		for i in range(2):
			número = int(input('Digite um valor: '))

			if número > maior:
				maior = número
			elif número < menor:
				menor = número

		print(f'O maior é {maior} e o menor é {menor}')
		break

	except ValueError:
		print(f'Valor inválido.')

# Usando uma lista tornamos a tarefa mais fácil, porém sujeita a muitos erros se não forem adicionados tratamentos. Nessa versão, usando uma função para obter cada valor o programa só irá ser concluído quando o usuário digitar os 3 valores. Se um valor não for aceito, o anterior não é perdido
def obter_valor(msg):
	while True:
		try:
			return int(input(msg))
		except ValueError:
			print('Erro')

# Preenchemos a lista e exibimos o maior valor com max() e o menor com min()
lista = [obter_valor('Digite um valor: ') for i in range(3)]
print(f'Maior: {max(lista)}\nMenor: {min(lista)}')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler três números e mostrar qual é o maior e qual é o menor.

# A primeira coisa a ser feita é ler os três números digitados pelo usuário. Para isso, vamos utilizar a função input() para ler os números e a função int() para converter os valores para inteiros.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

# Em seguida, vamos comparar os valores para encontrar o maior e o menor. Para isso, vamos utilizar uma estrutura condicional com a palavra-chave if para verificar as condições.
# Vamos começar definindo o maior e o menor valor como o primeiro valor digitado pelo usuário.
maior = valor1
menor = valor1

# Agora, vamos comparar o segundo valor com o maior e o menor valor. Se o segundo valor for maior que o maior valor, atualizamos o maior valor. Se o segundo valor for menor que o menor valor, atualizamos o menor valor.
if valor2 > maior:
    maior = valor2
if valor2 < menor:
    menor = valor2
    
# Por fim, vamos comparar o terceiro valor com o maior e o menor valor. Se o terceiro valor for maior que o maior valor, atualizamos o maior valor. Se o terceiro valor for menor que o menor valor, atualizamos o menor valor.
if valor3 > maior:
    maior = valor3
if valor3 < menor:
    menor = valor3
    
# Agora, basta exibir o maior e o menor valor na tela.

print(f'O maior valor é {maior} e o menor valor é {menor}')

# Essa é uma forma simples de encontrar o maior e o menor valor entre três números usando os conhecimentos que temos até o momento. Podemos simplificar o código e torná-lo mais eficiente, mas isso envolve o uso de estruturas de dados mais avançadas, como listas e funções. Por enquanto, essa é uma solução válida e funcional para o problema proposto.
