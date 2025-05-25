# Exercício Python #087 - Mais sobre Matriz em Python - Aula 00 até 18 - Mundo 3
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from random import randint

from cisco_fundamentos_python.python_essentials_1.modulo_2.m2_aula_1 import soma
matriz = [[], [], []]
soma_pares = 0

for linha in range(3):
    for coluna in range(3):
        numero = randint(0, 99)
        print(f'Digite o valor da posição [{linha}][{coluna}] - {numero}')
        if numero % 2 == 0:
            soma_pares += numero
        matriz[linha].append(numero)

for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:2} ] ', end='')
    print()

print(f'\nA soma de todos os valores pares é {soma_pares}')

terceira_coluna = 0
for linha in range(3):
    terceira_coluna += matriz[linha][2]
print(f'A soma de todos os valores na terceira coluna é {terceira_coluna}')

maior_segunda_linha = max(matriz[1])
print(f'O maior valor da segunda linha é {maior_segunda_linha}')

# Resumida

matriz = [[randint(0, 9) for i in range(3)] for i in range(3)]

pares = coluna = 0
maior = max(matriz[1])
for linha in matriz:
    print(*[f'[{valor:^3}]' for valor in linha], sep='', end='\n')
    for i, valor in enumerate(linha):
        pares += valor if valor % 2 == 0 else 0
        if i == 2:  # Se for a terceira coluna
            coluna += valor


print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {maior}')

# Atual

matriz = [[randint(0, 9) for valor in range(3)] for linha in range(3)]

soma_pares = soma_terceira_coluna = 0
maior_segunda_linha = max(matriz[1])

for linha in matriz:
	soma_terceira_coluna += linha[2]
	for valor in linha:

		if not valor % 2:
			soma_pares += valor

		print(f'[{valor:^3}]', end=' ')
	print('')

print(f'A soma de todos os valores pares é igual a: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Esse exercício complementa o anterior. Aqui, vamos aprimorar o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Vamos iniciar as variáveis soma_pares, terceira_coluna e maior_segunda_linha com zero para atender as condições do enunciado.
soma_pares = terceira_coluna = maior_segunda_linha = 0

# Em seguida criar a matriz 3x3 e preencher com valores digitados pelo usuário. Vamos aproveitar as iterações para calcular a soma dos valores pares, a soma dos valores da terceira coluna e o maior valor da segunda linha.
matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        numero = int(input(f'Digite o valor da posição [{linha}][{coluna}]: '))
        if numero % 2 == 0:
            soma_pares += numero
        
        # Se o valor for da terceira coluna, vamos somar na variável terceira_coluna.
        if coluna == 2:
            terceira_coluna += numero
        
        # Se for da segunda linha, vamos verificar se é o maior valor.
        if linha == 1:
            if numero > maior_segunda_linha:
                maior_segunda_linha = numero
                
        # Adicionando o valor na matriz.
        matriz[linha].append(numero)

# Exibindo a matriz na tela.
for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print()
    
# Exibindo os resultados.
print(f'\nA soma de todos os valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')

# Fizemos um programa mais detalhado, afim de mostrar o passo a passo do cálculo das variáveis. No entanto, podemos simplificar o código, como no exemplo abaixo:

# Vamos preencher a matriz com valores aleatórios de 0 a 9.
from random import randint
matriz = [[randint(0, 9) for valor in range(3)] for linha in range(3)]

# Inicializando as variáveis soma_pares, soma_terceira_coluna e maior_segunda_linha com zero.
soma_pares = soma_terceira_coluna = 0
maior_segunda_linha = max(matriz[1]) # Diferente de antes, aqui usamos a função max() para encontrar o maior valor da segunda linha. Evitando a necessidade de um laço de repetição e verificar cada valor.

# Percorrendo a matriz e exibindo os valores na tela.
for linha in matriz:
    for valor in linha:
        if not valor % 2:
            soma_pares += valor
        
        soma_terceira_coluna += linha[2]
        print(f'[{valor:^3}]', end=' ')
    print('')

# Exibindo os resultados.
print(f'A soma de todos os valores pares é igual a: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')
