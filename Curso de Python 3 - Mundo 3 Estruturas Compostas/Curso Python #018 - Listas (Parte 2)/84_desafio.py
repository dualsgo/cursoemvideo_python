# Exercício Python #084 - Lista composta e análise de dados - Aula 00 até 18 - Mundo 3
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Versão 1

lista_principal = []  # Inicializa a lista principal que irá conter todos os dados

pesado = 0  # Inicializa o mais pesado como zero
leve = 0  # Inicializa o mais leve como zero

while True:  # Inicializa o loop infinito
    pessoa = []  # Inicializa a lista de pessoas que será uma sub-lista dentro da principal
    pessoas_pesadas = []  # Inicializa uma lista para armazenar os dados das pessoas que forem consideradas as mais pesadas
    pessoas_leves = []  # Inicializa uma lista para armazenar os dados das pessoas que forem consideradas as mais leves

    nome = str(input('Nome: '))  # Recebe o nome da pessoa e armazena em uma variável
    pessoa.append(nome)  # Adiciona o valor a lista pessoa

    peso = float(input('Peso: Kg '))  # Recebe o nome da pessoa e armazena em uma variável
    pessoa.append(peso)  # Adiciona o valor a lista pessoa

    lista_principal.append(pessoa[:])  # Após cadastrar nome e peso na lista pessoa, adiciona uma cópia da lista a lista principal

    if len(lista_principal) == 1:  # Verifica se é a primeira pessoa cadastrada
        pesado = leve = peso  # Se for, o peso atribuído a ela será considerado o menor e o maior, já que é o único até o momento e servirá de comparação para os demais se houver

    else:  # Se não for a primeira pessoa, irá verificar se o peso atual é menor que o menor peso e irá atualizar caso seja verdade
        if peso < leve:
            leve = peso
        elif peso > pesado:  # Se a primeira comparação não for verdadeira, irá verificar se o peso atual é maior que o maior peso
            pesado = peso

    pessoa.clear()  # Após todas as verificações irá limpar a lista par adicionar novos dados separadamente

    continuar = str(input('Continuar? S/N')).strip().upper()  # Verificação se deseja continuar

    while continuar not in 'SN':  # Enquanto a resposta não estiver dentro dos parâmetros definidos a pergunta irá se repetir
        continuar = str(input('Continuar? S/N')).strip().upper()

    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

print(f'Foram cadastradas {len(lista_principal)} pessoas.')  # Exibe a quantidade de pessoas cadastradas

for indice, valor in enumerate(lista_principal):  # Itera sobre a lista principal para exibir cada pessoa e seu peso
    print(f'{indice + 1} - {valor[0]} pesando {valor[1]}Kg')
    if valor[1] >= pesado:  # Enquanto isso verifica se o valor do peso é maior ou igual ao valor considerado mais pesado para então adicionar o nome da pessoa em uma lista separada de pessoas mais pesadas
        pessoas_pesadas.append(valor[0])
    if valor[1] <= leve:  # O mesmo para as pessoas mais leves
        pessoas_leves.append(valor[0])
print()

print(f'O maior peso registrado foi {pesado}Kg - Peso de ', end='')
for pessoa in pessoas_pesadas:
    if len(pessoas_pesadas) > 1:
        print(pessoa, end=', ')
    else:
        print(pessoa)
print()
print(f'O menor peso registrado foi {leve}Kg - Peso de ', end='')
for pessoa in pessoas_leves:
    if len(pessoas_leves) > 1:
        print(pessoa, end=', ')
    else:
        print(pessoa)

# Versão 2

pessoas = []
mais_pesado = mais_leve = 0
while True:
	pessoa = []

	nome = input('Nome: ').strip().title()
	pessoa.append(nome)

	while True:
		try:
			peso = float(input('Digite o peso: '))
			break
		except ValueError:
			print('Idade inválida!')

	pessoa.append(peso)


	while True:
		continuar = input('Continuar? S/N ').strip().upper()
		if continuar in 'SN':
			break

	pessoas.append(pessoa)

	if len(pessoas) == 1:
		mais_pesado = mais_leve = peso

	if continuar == 'N':


		for pessoa in pessoas:
			print(pessoa)
			pessoa_peso = pessoa[1]

			if pessoa_peso > mais_pesado:
				mais_pesado = pessoa_peso
			elif pessoa_peso < mais_leve:
				mais_leve = pessoa_peso

		break

print(f'Você cadastrou: {len(pessoas)} pessoas')
print(f'Maior peso: {mais_pesado:.2f}Kg')
for pessoa in pessoas:
	if pessoa[1] == mais_pesado:
		print(pessoa[0], end=' - ')
print(f'\nMenor peso: {mais_leve:.2f}Kg')
for pessoa in pessoas:
	if pessoa[1] == mais_leve:
		print(pessoa[0], end=' - ')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, vamos exibir:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# A lógica é a seguinte: Vamos criar uma lista principal que irá conter todas as pessoas cadastradas. Para cada pessoa, vamos criar uma lista com o nome e o peso. Vamos adicionar essa lista na lista principal. Vamos verificar se o peso da pessoa é o maior ou o menor. No final, vamos exibir a quantidade de pessoas cadastradas, o maior peso e o menor peso. Vamos exibir também as pessoas que possuem o maior e o menor peso.

# Primeiro, vamos criar uma lista principal que irá conter todas as pessoas cadastradas. Vamos criar duas variáveis para armazenar o peso da pessoa mais pesada e da pessoa mais leve. Vamos criar um loop infinito para cadastrar as pessoas.

lista_principal = []  # Inicializa a lista principal que irá conter todos os dados

peso_pesado = 0  # Inicializa o mais pesado como zero
peso_leve = 0  # Inicializa o mais leve como zero

while True:  # Inicializa o loop infinito
    pessoa = []  # Inicializa a lista de pessoas que será uma sub-lista dentro da principal. Como a lista é incializada dentro do loop, a cada iteração ela será uma nova lista e não precisaremos usar o método celar() para limpar a lista a cada iteração

    pessoas_pesadas = []  # Inicializa uma lista para armazenar os dados das pessoas que forem consideradas as mais pesadas
    pessoas_leves = []  # Inicializa uma lista para armazenar os dados das pessoas que forem consideradas as mais leves

    nome = str(input('Nome: ')).strip().title()  # Recebe o nome da pessoa e armazena em uma variável
    pessoa.append(nome)  # Adiciona o valor a lista pessoa

    peso = float(input('Peso: Kg '))  # Recebe o peso da pessoa e armazena em uma variável
    pessoa.append(peso)  # Adiciona o valor a lista pessoa

    lista_principal.append(pessoa[:])  # Após cadastrar nome e peso na lista pessoa, adiciona uma cópia da lista a lista principal

    if len(lista_principal) == 1:  # Verifica se é a primeira pessoa cadastrada
        peso_pesado = peso_leve = peso  # Se for, o peso atribuído a ela será considerado o menor e o maior, já que é o único até o momento e servirá de comparação para os demais se houver

    else:  # Se não for a primeira pessoa, irá verificar se o peso atual é menor que o menor peso e irá atualizar caso seja verdade
        if peso < peso_leve:
            peso_leve = peso
        elif peso > peso_pesado:  # Se a primeira comparação não for verdadeira, irá verificar se o peso atual é maior que o maior peso
            peso_pesado = peso

    continuar = str(input('Continuar? S/N')).strip().upper()  # Verificação se deseja continuar

    while continuar not in 'SN':  # Enquanto a resposta não estiver dentro dos parâmetros definidos a pergunta irá se repetir
        continuar = str(input('Continuar? S/N')).strip().upper()

    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break
        
# Em seguida, vamos exibir a quantidade de pessoas cadastradas e a lista de pessoas com seus respectivos pesos.

print(f'Foram cadastradas {len(lista_principal)} pessoas.')  # Exibe a quantidade de pessoas cadastradas

for indice, valor in enumerate(lista_principal):  # Itera sobre a lista principal para exibir cada pessoa e seu peso
    print(f'{indice + 1} - {valor[0]} pesando {valor[1]}Kg')
    if valor[1] >= peso_pesado:  # Enquanto isso verifica se o valor do peso é maior ou igual ao valor considerado mais pesado para então adicionar o nome da pessoa em uma lista separada de pessoas mais pesadas
        pessoas_pesadas.append(valor[0])
    if valor[1] <= peso_leve:  # O mesmo para as pessoas mais leves
        pessoas_leves.append(valor[0])


# Por fim, vamos exibir o maior peso, o menor peso e as pessoas que possuem o maior e o menor peso.
print(f'O maior peso registrado foi {peso_pesado}Kg - Peso de ', end='')
for pessoa in pessoas_pesadas:
    if len(pessoas_pesadas) > 1:
        print(pessoa, end=', ')
    else:
        print(pessoa)
print()
print(f'O menor peso registrado foi {peso_leve}Kg - Peso de ', end='')
for pessoa in pessoas_leves:
    if len(pessoas_leves) > 1:
        print(pessoa, end=', ')
    else:
        print(pessoa)
        
# Obs.: 
# Imagine que temos o seguinte código:
lista1 = [1, 2, 3, 4, 5]
# E criamos uma lista2 que é uma cópia da lista1:
lista2 = lista1
# Se alterarmos um valor da lista2, o valor da lista1 também será alterado:
lista2[0] = 10
print(lista1)  # [10, 2, 3, 4, 5]
print(lista2)  # [10, 2, 3, 4, 5]

# Isso acontece pois quando atribuímos uma lista a outra, estamos atribuindo o endereço de memória da lista1 para a lista2. Ou seja, as duas listas estão apontando para o mesmo endereço de memória. Portanto, se alterarmos um valor de uma lista, o valor da outra lista também será alterado.

# Se quisermos criar uma cópia da lista1, podemos utilizar o método copy():
lista1 = [1, 2, 3, 4, 5]
lista2 = lista1.copy()

# Ou podemos utilizar o fatiamento:
lista1 = [1, 2, 3, 4, 5]
lista2 = lista1[:]

# Ou  utilizando o método list():
lista1 = [1, 2, 3, 4, 5]
lista2 = list(lista1)

# Dessa forma podemos manipular as listas de forma independente.

# Vamos falar também sobre clear():
# O método clear() remove todos os elementos de uma lista. A lista se torna vazia após a execução do método.
# del é diferente de clear(). O del remove a lista, enquanto o clear() apenas remove os elementos da lista.
# Mas podemos usar del para remover um elemento específico da lista:
lista = [1, 2, 3, 4, 5]
del lista[0]
