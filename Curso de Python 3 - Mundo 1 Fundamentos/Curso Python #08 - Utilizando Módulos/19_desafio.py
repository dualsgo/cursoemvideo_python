# Exercício Python #019 - Sorteando um item na lista - Aula 00 até 08 - Mundo 1
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
from emoji import emojize
from time import sleep

# Tarefa 1: Ler o nome dos alunos
alunos = [str(input(emojize(':estudante: Digite o nome do primeiro aluno: ', language='pt'))), str(input(emojize(':estudante: Digite o nome do segundo aluno: ', language='pt'))), str(input(emojize(':estudante: Digite o nome do terceiro aluno: ', language='pt'))), str(input(emojize(':estudante: Digite o nome do quarto aluno: ', language='pt')))]

# Tarefa 2: Exibir o nome do aluno escolhido.
escolhido = choice(alunos)
print('O aluno escolhido foi: ', end='')
sleep(1)
print(emojize(f'{escolhido} :professora:', language='pt'))

# Versão 2

while True:
	try:
		nomes = [input(f'Digite o nome do {i}º aluno: ').strip().title() for i in range(1, 5)]
		escolhido = choice(nomes)
		print(f'Uni, duni, tê...')
		print(f'O aluno escolhido foi você: {escolhido}')
		break
	except Exception as e:
		print(f'Ocorreu o erro: {e}')

# Versão 3 - Resumida

print(f'O aluno escolhido foi: \033[1;32m{choice([input(f'{i}º aluno: ').strip().title() for i in range(1, 5)])}\033[m')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário o nome de quatro alunos e sorteia um deles para apagar o quadro.

# Vamos aprender mais uma função do módulo random, a função choice(). A função choice() é utilizada para escolher um elemento aleatório de uma sequência, como uma lista. A função recebe como argumento uma sequência e retorna um elemento aleatório dessa sequência.

# Primeiro, como sempre importamos a função que iremos utilizar do módulo random.
from random import choice

# Em seguida, utilizamos a função input() para solicitar o nome dos quatro alunos. Os nomes são armazenados em uma lista chamada alunos.
# Como ainda não falamos sobre listas, vamos armazenar os nomes em variáveis separadas e só usaremos lista no final, quando chamarmos a função choice().
aluno1 = str(input('Digite o nome do primeiro aluno: ')).strip().title()
aluno2 = str(input('Digite o nome do segundo aluno: ')).strip().title()
aluno3 = str(input('Digite o nome do terceiro aluno: ')).strip().title()
aluno4 = str(input('Digite o nome do quarto aluno: ')).strip().title()

# NOTA: A função input() retorna um valor do tipo string, então não é necessário utilizar a função str() para converter o valor digitado em string. Estamos utilizando para deixar claro que o valor digitado é uma string.

# strip() e title() são métodos de strings que podem ser encadeados, ou seja, chamados em sequência. O método strip() remove espaços em branco no início e no final da string, enquanto o método title() deixa a primeira letra de cada palavra em maiúscula.

# Com os nomes dos alunos armazenados, utilizamos a função choice() para escolher um aluno aleatório da lista alunos. O nome do aluno escolhido é armazenado na variável escolhido.
escolhido = choice([aluno1, aluno2, aluno3, aluno4])

# A função choice() recebe uma lista de alunos como argumento e retorna um dos nomes aleatoriamente. O nome do aluno escolhido é armazenado na variável escolhido. Dessa forma, fica fácil exibir o nome do aluno escolhido na tela.

# Por fim, exibimos na tela o nome do aluno escolhido.
print(f'O aluno escolhido foi: {escolhido}')

# NOTA: listas são um tipo de dado que armazena uma coleção de elementos. Cada elemento da lista é separado por vírgula e a lista é delimitada por colchetes. No exemplo acima, a lista alunos contém os nomes dos quatro alunos digitados pelo usuário. Falaremos mais sobre listas em aulas futuras. 