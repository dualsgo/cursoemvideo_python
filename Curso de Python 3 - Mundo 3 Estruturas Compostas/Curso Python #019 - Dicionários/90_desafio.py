# Exercício Python #090 - Dicionário em Python - Aula 00 até 19 - Mundo 3
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


def obter_nota(mensagem):
	while True:
		try:
			média = float(input(mensagem))
			if 0 <= média <= 10:
				return média
			else:
				print('Entre 0 e 10')
		except ValueError:
			print('Tente novamente')


def obter_nome(mensagem):
	while True:
		entrada = input(mensagem).strip().title()
		condição = entrada.replace(' ', '').isalpha()

		while not condição:
			print('Somente caracteres alfabéticos')
			break

		if condição:
			return entrada


boletim = []

while True:
	aluno = dict(nome=obter_nome('Digite o nome do aluno: '), media=obter_nota('Digite a nota do aluno: '))

	aluno['situação'] = '\033[1;31mREPROVADO\033[m' if aluno['media'] < 5 else "\033[1;33mEM RECUPERAÇÃO\033[m" if aluno['media'] < 7 else '\033[1;32mAPROVADO\033[m'

	boletim.append(aluno.copy())

	continuar = str(input('Continuar? S/N ')).strip().upper()
	if continuar not in 'SN':
		continuar = str(input('Continuar? S/N ')).strip().upper()
	else:
		if continuar == 'S':
			print('Prosseguindo...')
		elif continuar == 'N':
			print('Encerrando...')
			break

for i, aluno in enumerate(boletim):
	print(f"Aluno {aluno['nome']} teve a média {aluno['media']} e está {aluno['situação']}.")

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o professor pede para criar um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostrar o conteúdo da estrutura na tela.

# Um dicionário é uma estrutura de dados que permite armazenar um conjunto de valores, cada um identificado por uma chave. Para criar um dicionário, usamos chaves {} e separamos os pares chave-valor por dois pontos :. Por exemplo, aluno = {'nome': 'Pedro', 'média': 9.5, 'situação': 'Aprovado'}.

# Vamos criar um dicionário chamado aluno e dentro dele vamos armazenar o nome, a média e a situação do aluno. Para isso, vamos criar uma lista chamada boletim para armazenar todos os alunos.
aluno = dict()
boletim = []

# Vamos criar um laço de repetição para adicionar vários alunos ao boletim. Dentro do laço, vamos pedir o nome e a média do aluno.

while True:
    
    # Vamos adicionar os valores para as chaves nome e média do dicionário aluno.
	aluno['nome'] = str(input('Nome: ')).strip().title()
	aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

	# Vamos adicionar a situação do aluno de acordo com a média. Se a média for menor que 5, o aluno está reprovado. Se a média for maior ou igual a 5 e menor que 7, o aluno está de recuperação. Se a média for maior ou igual a 7, o aluno está aprovado.
	if aluno['média'] < 5:
		aluno['situação'] = 'Reprovado'
	elif 5 <= aluno['média'] < 7:
		aluno['situação'] = 'Recuperação'
	else:
		aluno['situação'] = 'Aprovado'

	# Por fim, vamos adicionar o dicionário aluno à lista boletim. Para isso, vamos usar o método copy() para criar uma cópia do dicionário aluno.
	boletim.append(aluno.copy())

	# Verificamos se o usuário quer continuar adicionando alunos ao boletim. Se a resposta for 'N', o laço de repetição é interrompido.
	continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
	if continuar in 'N':
		break

# No final, vamos mostrar o conteúdo do boletim na tela.
for aluno in boletim:
	print(f'O aluno {aluno["nome"]} teve a média {aluno["média"]} e está {aluno["situação"]}.')
