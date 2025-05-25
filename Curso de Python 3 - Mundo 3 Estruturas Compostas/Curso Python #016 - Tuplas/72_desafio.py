# Exercício Python #072 - Número por Extenso - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

from calendar import c


extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
	try:
		print(f"Você digitou o número {extenso[int(input('Digite um valor entre 0 e 20: '))]}")
		continuar = str(input('Continuar? S/N ')).strip().upper()
		if continuar not in 'Ss':
			break
	except IndexError:
		print('Somente valores entre 0 e 20')
	except ValueError:
		print('Apenas valores numéricos.')

# Versão 2

numeros_por_extenso = (
	'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
	'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
	'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
	'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
	try:
		numero = int(input('Digite um valor entre 0 e 20: '))
		if 0 <= numero <= 20:
			break
		else:
			print("Inválido")
	except ValueError:
		print('Este valor é de um tipo de dado inválido para essa operação!')

resultado = f'O número {numero} por extenso é: {numeros_por_extenso[numero]}'
tamanho = len(resultado)
print(resultado)
print(f'{"-" * tamanho}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nessse exercício, vamos criar um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. O programa deve ler um número pelo teclado (entre 0 e 20) e mostrar o número por extenso.

# Primeiro vamos criar uma tupla com os números por extenso. Uma tupla é uma coleção de objetos imutável, ou seja, não podemos alterar os valores de uma tupla.

números_por_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

# Vamos criar um laço de repetição para que o programa continue rodando até que o usuário decida parar.

while True:
	número = int(input('Digite um valor entre 0 e 20: '))

	# Vamos verificar se o número digitado está dentro do intervalo de 0 a 20.
	if 0 <= número <= 20:
		# Se estiver, vamos mostrar o número por extenso.
		print(f'Você digitou o número {números_por_extenso[número]}')
	else:
		# Se não estiver, vamos mostrar uma mensagem de erro.
		print('Tente novamente. ', end='')

		continue # Se o número não estiver entre os valores aceitos o fluxo do programa irár retornar para o início do laço, ignorando o código abaixo.

	# Vamos perguntar ao usuário se ele deseja continuar.
	continuar = str(input('Continuar? S/N ')).strip().upper()

	# Se a resposta for diferente de 'S', o programa vai parar.
	if continuar not in 'Ss':
		break
