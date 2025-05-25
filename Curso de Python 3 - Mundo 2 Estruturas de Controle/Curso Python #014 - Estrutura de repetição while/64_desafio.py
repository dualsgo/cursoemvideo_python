# Exercício Python #064 - Tratando vários valores v1.0 - Aula 00 até 14 - Mundo 2
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

flag = 999
contador = soma = 0

while True:
	try:
		print(f'{'-'*30}')
		número = int(input('\033[1mDigite um valor:\033[m \033[7;37;40m 999 encerra \033[m '))

		if número == flag:
			print(f'Programa encerrado!')
			print(f'{'-' * 30}')
			if contador:
				if contador == 1:
					print(f'Apenas um valor foi digitado! Foi o valor {soma}')
				elif contador > 1:
					print(f'Foram digitados {contador} valores! A soma entre eles é {soma}')
			else:
				print(f'Nenhum valor foi digitado!')
			break

		contador += 1
		soma += número
		print(f'{'-'*30}')
		print(f'{f'{contador}º valor: {número}':^30}')
		print(f'{f'A soma é {soma}':^30}')

	except ValueError:
		print('Este valor não e válido para essa operação.')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que lê vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, o programa deve mostrar quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag.

# A condição de parada é o valor 999. Vamos usar uma expressão como condição do laço de repetição while para continuar lendo números até que o usuário digite o valor 999.

flag = 999  # Define o valor 999 como flag para encerrar o programa.
numero = contador = soma = 0  # Inicializa o contador de números digitados e a soma dos números.

# Usamos um laço de repetição while para ler vários números inteiros e calcular a soma.
while numero != flag:  # Enquanto o número digitado for diferente de 999, o laço de repetição continuará.
	numero = int(input('Digite um valor: '))  # Solicita ao usuário que digite um valor inteiro.
	
	# Verificamos se o número digitado é igual ao flag para encerrar o programa.
	if numero == flag:  # Se o número digitado for 999, o programa encerra.
		print('Programa encerrado!')  # Exibe uma mensagem informando que o programa foi encerrado.
		print(f'Foram digitados {contador} valores! A soma entre eles é {soma}')  # Exibe o número de valores digitados e a soma dos números.

	# Se o número digitado for diferente de 999, continuamos a leitura dos números.
	else:
		# Atualizamos os valores do contador e da soma dos números digitados a cada iteração do laço de repetição.
		contador += 1  # Incrementa o contador de números digitados.
		soma += numero  # Acumula a soma dos números digitados.
		
		# Vamos atualizando a contagem e a soma dos números digitados a cada iteração do laço de repetição.
		print(f'{contador}º valor: {numero}')  # Exibe o número digitado e a posição do número na sequência.
		print(f'A soma é {soma}')  # Exibe a soma dos números digitados até o momento.


