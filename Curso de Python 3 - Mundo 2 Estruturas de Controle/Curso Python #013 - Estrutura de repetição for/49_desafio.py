# Exercício Python #049 - Tabuada v.2.0 - Aula 00 até 13 - Mundo 2
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

def tabuada(mensagem):
	while True:
		try:
			fator = int(input(mensagem))
			for i in range(1, 11):
				print(f'{fator:^3} x {i:^3} = {fator * i:3}')
			break
		except ValueError:
			print('Valor de tipo inválido.')


tabuada('Digite o valor que deseja verificar a tabuada: ')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos refazer o DESAFIO 009, que pedia para mostrar a tabuada de um número que o usuário escolhesse. A diferença é que agora vamos usar um laço de repetição for para fazer a tabuada.

# Vamos usar um laço de repetição for para mostrar a tabuada de um número que o usuário escolher. O laço de repetição for é usado quando sabemos quantas vezes queremos repetir um bloco de código. No caso, queremos repetir 10 vezes, de 1 até 10, pois queremos mostrar a tabuada de 1 até 10. Sabendo do comportamento do range(), podemos definir o intervalo de 1 a 11, pois o número 11 não será incluído.

# Primeiro solicitamos ao usuário que digite o número que deseja verificar a tabuada. Em seguida, usamos um laço de repetição for para mostrar a tabuada desse número. A cada iteração do laço, mostramos o resultado da multiplicação do número escolhido pelo número da iteração.
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
	print(f'{num} x {i} = {num * i}')
# Assim, a cada iteração do laço, o valor de i é incrementado em 1 e o resultado da multiplicação é mostrado na tela. O resultado é formatado para que os números fiquem alinhados. O número digitado pelo usuário é multiplicado por cada número de 1 a 10 e o resultado é mostrado na tela.
