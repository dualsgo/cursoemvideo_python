# Exercício Python #069 - Análise de dados do grupo - Aula 00 até 15 - Mundo 2
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cadastros = mais_18 = homens = mulheres_menos_20 = 0


def recebe_idade(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Erro. Tente novamente...')


def define_sexo(mensagem):
	escolha = input(mensagem).strip().upper()
	while escolha not in ['F', 'M']:
		print('Sexo deve ser M para masculino ou F para feminino')
		escolha = input(mensagem).strip().upper()
	return escolha


def continuar_cadastros(mensagem):
	opção = input(mensagem).strip().upper()
	while opção not in ['S', 'N']:
		print('Escolha S para continuar ou N para encerrar')
		opção = input(mensagem).strip().upper()
	return opção


while True:
	idade = recebe_idade('Digite a idade: ')
	sexo = define_sexo('Digite o sexo: ')

	cadastros += 1
	mais_18 += 1 if idade > 18 else 0
	homens += 1 if sexo == 'M' else 0
	mulheres_menos_20 += 1 if sexo == 'F' and idade < 20 else 0

	continuar = continuar_cadastros('Deseja continuar? ')

	if continuar == 'S':
		print('Próximo cadastro')
	elif continuar == 'N':
		print('Encerrando o programa...')
		break

if cadastros == 1:
	print(f'Somente uma pessoa foi cadastrada.\nSexo: {sexo}\nIdade: {idade}')
else:
	print(f'Foram cadastradas {cadastros} pessoas')
	print(f'Homens: {homens}\nMaiores de 18 anos: {mais_18}\nMulheres com menos de 20 anos: {mulheres_menos_20}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, o programa deve mostrar:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# Primeiro vamos criar uma variável cadastros para contar quantas pessoas foram cadastradas, e outras três variáveis para contar quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.
cadastros = mais_18 = homens = mulheres_menos_20 = 0

# Vamos criar um laço while True para que o programa fique em loop até que o usuário decida encerrá-lo.
while True:
    # Dentro do laço while, vamos pedir para o usuário digitar a idade.
	idade = int(input('Digite a idade: '))
	
	# Vamos pedir para o usuário digitar o sexo.
	sexo = input('Digite o sexo: ').strip().upper()
	
	# Vamos incrementar a variável cadastros para contar quantas pessoas foram cadastradas.
	cadastros += 1
	
	# Vamos verificar se a idade é maior que 18. Se for, incrementamos a variável mais_18.
	mais_18 += 1 if idade > 18 else 0
	
	# Vamos verificar se o sexo é masculino. Se for, incrementamos a variável homens.
	homens += 1 if sexo == 'M' else 0
	
	# Vamos verificar se o sexo é feminino e a idade é menor que 20. Se for, incrementamos a variável mulheres_menos_20.
	mulheres_menos_20 += 1 if sexo == 'F' and idade < 20 else 0
	
	# Vamos perguntar ao usuário se ele deseja continuar.
	continuar = input('Deseja continuar? ').strip().upper()
	
	# Se o usuário digitar N, o programa será encerrado.
	if continuar == 'N':
		print('Encerrando o programa...')
		break

# Vamos exibir o resultado do programa.
if cadastros == 1:
	print(f'Somente uma pessoa foi cadastrada.\nSexo: {sexo}\nIdade: {idade}')
else:
	print(f'Foram cadastradas {cadastros} pessoas')
	print(f'Homens: {homens}\nMaiores de 18 anos: {mais_18}\nMulheres com menos de 20 anos: {mulheres_menos_20}')

