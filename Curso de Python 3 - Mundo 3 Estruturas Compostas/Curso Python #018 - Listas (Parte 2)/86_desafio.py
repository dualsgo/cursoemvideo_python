# Exercício Python #086 - Matriz em Python - Aula 00 até 18 - Mundo 3
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

from random import randint
matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        numero = randint(0, 99)
        print(f'Digite o valor da posição [{linha}][{coluna}] - {numero}')
        matriz[linha].append(numero)

for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:2} ] ', end='')
    print()

# Resumida

matriz = [[randint(0, 9) for i in range(3)] for i in range(3)]
for linha in matriz:
    print(*[f'[{valor:^3}]' for valor in linha], sep='', end='\n')

# Versão atual

matriz = [[randint(0, 9) for valor in range(3)] for linha in range(3)]
for linha in matriz:
	for valor in linha:
		print(f'[{valor:^3}]', end=' ')
	print('')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, vamos exibir a matriz na tela, com a formatação correta.

# Mais uma vez vamos solucionar o problema de duas formas: uma mais resumida e outra mais detalhada.

matriz = [[], [], []] # Criando uma matriz 3x3

# Vamos percorrer cada linha e cada coluna da matriz. Para cada posição, vamos solicitar um valor ao usuário e adicionar na matriz.
for linha in range(3):
    for coluna in range(3):
        numero = int(input(f'Digite o valor da posição [{linha}][{coluna}]: ')) # Solicitando um valor ao usuário
        matriz[linha].append(numero) # Adicionando o valor na matriz
        
# Explicando o laço:
# 1. Vamos percorrer cada linha da matriz com for linha in range(3).
# 2. Para cada linha, vamos percorrer cada coluna da matriz com for coluna in range(3).
# 3. Para cada posição, vamos solicitar um valor ao usuário com input(f'Digite o valor da posição [{linha}][{coluna}]: ').
# 4. O valor digitado será convertido para inteiro e armazenado na variável numero.
# 5. Por fim, vamos adicionar o valor na matriz com matriz[linha].append(numero).

# Ao final das iterações, vamos exibir a matriz na tela com a formatação correta.
for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='') # Exibindo a matriz na tela
    print() # Quebrando a linha

# Explicando o laço:
# 1. Vamos percorrer cada linha da matriz com for linha in range(3).
# 2. Para cada linha, vamos percorrer cada coluna da matriz com for coluna in range(3).
# 3. Para cada posição, vamos exibir o valor da matriz com print(f'[ {matriz[linha][coluna]:^5} ]', end='').
# 4. Por fim, vamos quebrar a linha com print() e exibir a próxima linha.

# Agora vamos fazer uma versão mais resumida, com list comprehension e valores aleatórios.
from random import randint

# Criando uma matriz 3x3 com valores aleatórios
matriz = [[randint(0, 9) for i in range(3)] for i in range(3)]

# Exibindo a matriz na tela
for linha in matriz:
    print(*[f'[ {valor:^5} ]' for valor in linha], sep='', end='\n')
    
# Vamos entender o list comprehension:
# A sinataxe que usamos foi [[randint(0, 9) for i in range(3)] for i in range(3)].

# [randint(0, 9) for i in range(3)] cria uma lista com três valores aleatórios entre 0 e 9.
# for i in range(3) repete o processo três vezes, criando uma lista com três sublistas