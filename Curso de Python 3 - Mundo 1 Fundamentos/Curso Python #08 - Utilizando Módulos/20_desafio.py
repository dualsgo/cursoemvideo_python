# Exercício Python #020 - Sorteando uma ordem na lista - Aula 00 até 08 - Mundo 1
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle, sample
from emoji import emojize
from time import sleep

# Versão 1 - Com shuffle

turma = [input(f'{i}º aluno: ') for i in range(1, 5)]
shuffle(turma)
print('Ordem: ', end='')
for aluno in turma:
	print(aluno, end=' ')

# Versão 2 - Com sample

while True:
	try:
		nomes = [input(f'Digite o nome do {i}º aluno: ').strip().title() for i in range(1, 5)]
		for _, n in enumerate(sample(nomes, 4), 1):
			print(f'{_}º a apresentar: {n}')
		break
	except Exception as e:
		print(f'Ocorreu o erro: {e}')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário o nome de quatro alunos e sorteia a ordem de apresentação dos trabalhos.

# Diferente do exercício anterior, onde sorteamos um aluno aleatório, agora queremos sortear a ordem de apresentação dos trabalhos. Para isso, utilizamos a função shuffle() do módulo random. A função shuffle() embaralha os elementos de uma sequência, como uma lista. Dessa forma, a ordem dos elementos é alterada aleatoriamente.

# Como antes, importamos a função que iremos utilizar do módulo random. Nesse caso, a função shuffle().
# shuffle() não retorna nada, então não precisamos armazenar o resultado em uma variável. Quando nos aprofundarmos em funções, veremos que existem funções que retornam valores e funções que não retornam nada.

# Em seguida, utilizamos a função input() para solicitar o nome dos quatro alunos. Os nomes são armazenados em uma lista chamada turma.
# Como ainda não falamos sobre listas, vamos armazenar os nomes em variáveis separadas e só usaremos lista no final, quando chamarmos a função shuffle().
aluno1 = input('Digite o nome do primeiro aluno: ').strip().title()
aluno2 = input('Digite o nome do segundo aluno: ').strip().title()
aluno3 = input('Digite o nome do terceiro aluno: ').strip().title()
aluno4 = input('Digite o nome do quarto aluno: ').strip().title()

# NOTA: A função input() retorna um valor do tipo string, então não é necessário utilizar a função str() para converter o valor digitado em string. Estamos utilizando para deixar claro que o valor digitado é uma string.
# strip() e title() são métodos de strings que podem ser encadeados, ou seja, chamados em sequência. O método strip() remove espaços em branco no início e no final da string, enquanto o método title() deixa a primeira letra de cada palavra em maiúscula.

# Com os nomes dos alunos armazenados, utilizamos a função shuffle() para embaralhar a ordem dos alunos na lista turma.
turma = [aluno1, aluno2, aluno3, aluno4]

# turma é uma lista de strings que contém os nomes dos alunos. Ela é exibida na tela na mesma ordem em que foi digitada.
# Em seguida, utilizamos a função shuffle() para embaralhar a ordem dos alunos na lista turma. Dessa forma, a ordem dos alunos é alterada aleatoriamente.
shuffle(turma)

# Por fim, exibimos na tela a ordem de apresentação dos alunos.
print(f'Ordem: {turma}')

# A exibição será feita em uma única linha, separando os nomes dos alunos por vírgula e espaço. O resultado será algo como "Ordem: ['Alice', 'Bob', 'Carol', 'David']".

# Podemos formatar a saída para exibir os nomes dos alunos separados por vírgula e espaço. Para isso, utilizamos a função join() para concatenar os elementos da lista turma em uma única string.

# A função join() recebe como argumento uma string que será utilizada como separador e uma lista de strings que será concatenada. Ela retorna uma única string com os elementos da lista concatenados.
# A função join() é chamada a partir da string que será utilizada como separador. A sintaxe é: separador.join(lista).
# O separador é a string que será utilizada para separar os elementos da lista. No caso, queremos separar os nomes dos alunos por vírgula e espaço, então o separador é ", ".
# A lista é a lista de nomes dos alunos que queremos concatenar. No caso, a lista é turma, que contém os nomes dos alunos embaralhados.

# Por fim, exibimos na tela a ordem de apresentação dos alunos.
print(f'Ordem: {", ".join(turma)}')

# Um laço de repetição também pode ser usado para exibir os nomes dos alunos em uma única linha. O laço percorre a lista turma e exibe cada nome na tela. O resultado é o mesmo, mas a exibição é feita de forma diferente. Laços de repetição serão abordados em aulas futuras.

# Outra função que poderia ser utilizada para sortear a ordem de apresentação dos alunos é a função sample(). A função sample() é utilizada para escolher uma amostra aleatória de uma sequência, como uma lista. A função recebe como argumento uma sequência e um número de elementos a serem escolhidos. Ela retorna uma lista com os elementos escolhidos aleatoriamente.

# Em nosso exercício, sample() seria útil se quiséssemos escolher uma amostra aleatória de alunos para apresentar o trabalho. Como queremos sortear a ordem de apresentação dos alunos, a função shuffle() é mais adequada.