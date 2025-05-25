# Exercício Python #089 - Boletim com listas compostas - Aula 00 até 18 - Mundo 3
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from emoji import emojize

boletim = []

# Loop para entrada de dados
while True:
    nome = str(input(emojize(':aluno: Aluno: ', language='pt'))).strip().title()
    nota1 = float(input(emojize(':memorando: NOTA 1: ', language='pt')))
    nota2 = float(input(emojize(':memorando: NOTA 2: ', language='pt')))
    media = (nota1 + nota2) / 2

    # Adiciona os dados do aluno à lista composta
    boletim.append([nome, [nota1, nota2, media]])

    continuar = str(input('Continuar? S/N ')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()

    # Se o usuário escolher 'N', exibe o boletim e encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        print(f'{"BOLETIM DA TURMA":^20}')
        print(f'{"Número":<8}{"Nome":<10}{"Média":>8}')
        for i, aluno in enumerate(boletim):
            nome = aluno[0]
            nota1, nota2, media = aluno[1]
            # Formatação melhorada usando f-strings
            print(f'{i:<8}{nome:<10}{media:>8.1f}')
        break

# Loop para visualizar as notas de cada aluno individualmente
while True:
    ident = int(input('Digite o ID do aluno:'))

    # Verifica se o ID do aluno é válido
    if 0 <= ident < len(boletim):
        # Desempacotamento dos valores para nome e notas
        nome, notas = boletim[ident]

        # Atribuição de valores individuais para nota1, nota2 e media
        nota1, nota2, media = notas

        # Formatação melhorada usando f-strings para imprimir as informações do aluno
        print(f'O aluno {nome} teve as notas {nota1} e {nota2}. Sua média foi {media}')
    else:
        # Caso o ID seja inválido, exibe uma mensagem de erro
        print('ID do aluno inválido. Tente novamente.')

    continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Se o usuário escolher 'N', encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        break


"""**Desempacotamento:**

No Python, o desempacotamento é um recurso que permite atribuir os elementos de uma sequência (como uma lista ou tupla) a variáveis individuais. No trecho de código mencionado:

```python
# Desempacotamento dos valores para nome e notas
nome, notas = boletim[ident]
```

- `boletim[ident]` retorna uma lista que representa as informações de um aluno específico no boletim.
- `nome, notas` realiza o desempacotamento, atribuindo o primeiro elemento da lista (nome) à variável `nome` e o segundo elemento (que é uma lista de notas) à variável `notas`.

**Atribuição de valores individuais:**

Após o desempacotamento, a linha seguinte realiza a atribuição de valores individuais às variáveis `nota1`, `nota2`, e `media`:

```python
# Atribuição de valores individuais para nota1, nota2 e media
nota1, nota2, media = notas
```

- `notas` é a lista que contém as notas do aluno, onde `notas[0]` é a primeira nota, `notas[1]` é a segunda nota, e `notas[2]` é a média.
- `nota1, nota2, media` realiza a atribuição desses valores individuais às variáveis correspondentes.

Então, após essa linha de código, você tem acesso direto às notas individuais do aluno através das variáveis `nota1` e `nota2`, bem como à média através da variável `media`. Isso facilita o uso desses valores posteriormente no código, como na linha seguinte onde eles são usados na impressão formatada.

Em resumo, o desempacotamento e a atribuição de valores individuais ajudam a tornar o código mais legível e a facilitar o acesso a elementos específicos dentro de listas ou tuplas."""


# V2

boletim = []

while True:
    try:
        aluno = []  # Cria uma nova lista para cada aluno
        nome = input('Digite o nome do aluno: ').strip().title()
        aluno.append(nome)
        nota_1 = float(input('1º Bimestre: '))
        nota_2 = float(input('2º Bimestre: '))
    except ValueError:
        print(f'Ops... Valores inválidos. Tente novamente.')
        continue

    aluno.append(nota_1)
    aluno.append(nota_2)
    media = (nota_1 + nota_2) / 2
    aluno.append(media)
    boletim.append(aluno)

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = input('Outro aluno? S/N').strip().upper()

    if continuar == 'S':
        continue
    if continuar == 'N':
        break

print('-' * 46)
print(f'|{"No":^8}|{"Nome":^8}|{"Nota 1":^8}|{"Nota 2":^8}|{"Média":^8}|')
print('-' * 46)

for i, aluno in enumerate(boletim):
    print(f'|{i:^8}|{aluno[0]:^8}|{aluno[1]:^8}|{aluno[2]:^8}|{aluno[3]:^8}|')

print('-' * 46)

while True:
    try:
        escolha = int(input('Verificar informações de qual aluno? '))
    except ValueError:
        print(f'Valor inválido.')
        continue

    if escolha >= len(boletim):
        print(f'Aluno não localizado.')
        continue

    else:
        print('-' * 46)
        print(f'|{"No":^8}|{"Nome":^8}|{"Nota 1":^8}|{"Nota 2":^8}|{"Média":^8}|')
        print('-' * 46)
        print(f'|{escolha:^8}|{boletim[escolha][0]:^8}|{boletim[escolha][1]:^8}|{boletim[escolha][2]:^8}|{boletim[escolha][3]:^8}|')
        print('-' * 46)

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = input('Outro aluno? S/N').strip().upper()

    if continuar == 'S':
        continue
    if continuar == 'N':
        print('Encerrando...')
        break

# V3 INCOMPLETO

def obtem_nota(mensagem):
	while True:
		try:
			valor = float(input(mensagem))
			if 0 <= valor <= 10:
				return valor
			else:
				print('Valor deve estar entre 0 e 10')
		except ValueError:
			print('Valor inválido!')

def obtem_nome(mensagem):
	while True:
		digitado = input(mensagem).strip().title()
		nome_sem_espaços = digitado.replace(' ', '')
		if nome_sem_espaços.isalpha():
			return digitado
		else:
			print('Nome inválido!')

def obtem_valor(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Valor inválido!')

boletim = []

while True:
	nome = obtem_nome('Nome do aluno: ')

	# Obtém as 4 notas do aluno
	notas = [obtem_nota('Primeira nota do aluno: '),
			 obtem_nota('Segunda nota do aluno: '),
			 obtem_nota('Terceira nota do aluno: '),
			 obtem_nota('Quarta nota do aluno: ')]
	aluno = [nome, notas]
	boletim.append(aluno)

	while True:
		continuar = input('Continuar? S/N ').strip().upper()
		if continuar in 'SN':
			break

	if continuar == 'N':
		break

print('-' * 40)
for indice, aluno in enumerate(boletim):
	print(f'Aluno: {aluno[0]:^20}')
	print('-' * 40)
	print('Notas dos 4 bimestres:'.center(40))
	print('-' * 40)
	for bim, nota in enumerate(aluno[1], 1):  # Corrigido para aluno[1]
		print(f'{bim}º bimestre: {nota:>20.1f}')
	print('-' * 40)
	print(f'Média: {sum(aluno[1])/4:>20.1f}')  # Corrigido para aluno[1]
	print('-' * 40)

# Nesse exercício, vamos criar um programa que ajude um professor a ler o nome e as duas notas de vários alunos e guarde tudo em uma lista composta. No final, vamos mostrar um boletim contendo a média de cada um e permitir que o usuário possa mostrar as notas de cada aluno individualmente.

# Irei utilizar o módulo emoji para adicionar emojis às mensagens de entrada de dados.
from emoji import emojize

# Primeiro, vamos criar uma lista  para armazenar os dados dos alunos que será o boletim.
boletim = []

# Em seguida, vamos criar um loop para entrada de dados dos alunos.

while True:
    
    # Solicita o nome do aluno e suas duas notas.
    nome = str(input(emojize(':aluno: Aluno: ', language='pt'))).strip().title()
    nota1 = float(input(emojize(':memorando: NOTA 1: ', language='pt')))
    nota2 = float(input(emojize(':memorando: NOTA 2: ', language='pt')))
    
    # Calcula a média das notas
    media = (nota1 + nota2) / 2

    # Após receber os valores, adiciona o nome e as notas à lista boletim.
    boletim.append([nome, [nota1, nota2, media]])
    # Observer que estamos adicionando uma lista com o nome e uma lista com as notas e a média.
    # Então cada elemento da lista boletim é uma lista com duas posições: o nome do aluno e uma lista com as notas e a média.
    
    # Pergunta ao usuário se deseja continuar adicionando alunos.
    continuar = str(input('Continuar? S/N ')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()

    # Se o usuário escolher 'N', exibe o boletim e encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        print(f'{"BOLETIM DA TURMA":^20}')
        print(f'{"Número":<8}{"Nome":<10}{"Média":>8}')
        for i, aluno in enumerate(boletim):
            nome = aluno[0]
            nota1, nota2, media = aluno[1]
            # Formatação melhorada usando f-strings
            print(f'{i:<8}{nome:<10}{media:>8.1f}')
        break

# Loop para visualizar as notas de cada aluno individualmente. Vamos solicitar o ID do aluno e exibir suas notas. O ID será o índice do aluno na lista boletim.
while True:
    ident = int(input('Digite o ID do aluno:'))

    # Verifica se o ID do aluno é válido, analisando se está dentro do intervalo de índices da lista boletim
    if 0 <= ident < len(boletim):
        
        # Desempacotamento dos valores para nome e notas para facilitar o acesso. Vou falar sobre o desempacotamento no final.
        nome, notas = boletim[ident]

        # Atribuição de valores individuais para nota1, nota2 e media. Nessa técnica, cada valor da lista notas é atribuído a uma variável individual na ordem em que aparecem na lista.
        nota1, nota2, media = notas

        # Formatação melhorada usando f-strings para imprimir as informações do aluno
        print(f'O aluno {nome} teve as notas {nota1} e {nota2}. Sua média foi {media}')
    else:
        # Caso o ID seja inválido, exibe uma mensagem de erro
        print('ID do aluno inválido. Tente novamente.')

    # Pergunta ao usuário se deseja ver as notas de outro aluno individualmente
    continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Se o usuário escolher 'N', encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        break

# Sobre o desempacotamento:

# No Python, o desempacotamento é um recurso que permite atribuir os elementos de uma sequência (como uma lista ou tupla) a variáveis individuais. No trecho de código mencionado:


# Por exemplo, no desempacotamento dos valores para nome e notas
# nome, notas = boletim[ident]

# boletim[ident] retorna uma lista que representa as informações de um aluno específico no boletim.
# nome, notas realiza o desempacotamento, atribuindo o primeiro elemento da lista (nome) à variável nome e o segundo elemento (que é uma lista de notas) à variável notas.

# Após o desempacotamento, a linha seguinte realiza a atribuição de valores individuais às variáveis nota1, nota2, e media:

# nota1, nota2, media = notas

# notas é a lista que contém as notas do aluno, onde notas[0] é a primeira nota, notas[1] é a segunda nota, e notas[2] é a média.
# nota1, nota2, media realiza a atribuição desses valores individuais às variáveis correspondentes.

# Depois dessa linha de código, você tem acesso direto às notas individuais do aluno através das variáveis nota1 e nota2, bem como à média através da variável media. Isso facilita o uso desses valores posteriormente no código, como na linha seguinte onde eles são usados na impressão formatada.