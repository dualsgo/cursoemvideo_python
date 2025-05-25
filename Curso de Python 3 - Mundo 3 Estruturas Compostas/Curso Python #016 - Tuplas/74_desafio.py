# Exercício Python #074 - Maior e menor valores em Tupla - Aula 00 até 16 - Mundo 3
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = tuple(randint(0, 99) for i in range(5))

print(f'Os números são: ', end='')
for i, elemento in enumerate(tupla, 1):
	print(f'{elemento}', end=', ' if i < len(tupla) else '.\n')
print(f'O maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, o programa deve mostrar a listagem de números gerados e indicar o menor e o maior valor que estão na tupla.

# Primeiro vamos importar a função randint da biblioteca random para gerar números aleatórios.
from random import randint

# Vamos criar uma tupla com cinco números aleatórios.
tupla = tuple(randint(0, 99) for i in range(5))

# Vamos analisar a forma que criamos a tupla. Usamos uma compressão de lista para criar a tupla. A função randint(0, 99) gera números aleatórios entre 0 e 99. O laço for i in range(5) vai repetir cinco vezes a função randint(0, 99) e criar uma tupla com esses cinco números.

# A sintaxe de uma compressão de lista é a seguinte:
# tupla = tuple(expressão for variável in iterável)
# tupla é a variável que vai armazenar os valores da expressão.
# expressão é a operação que será realizada.
# variável é a variável que vai percorrer o iterável.
# iterável é a sequência de valores que a variável vai percorrer. Pode ser uma lista, tupla, dicionário, etc.

# Seguindo com o código, vamos exibir os números gerados.
print(f'Os números são: ', end='')
for i, elemento in enumerate(tupla, 1):
	print(f'{elemento}', end=', ' if i < len(tupla) else '.\n')

# Usamos enumerate para percorrer a tupla e exibir os elementos. A função enumerate retorna um objeto enumerado. O parâmetro 1 indica que a contagem começa em 1. O parâmetro elemento vai receber o valor da tupla. Se o índice i for menor que o tamanho da tupla, exibimos uma vírgula, senão, exibimos um ponto.

# o resultado será algo como "Os números são: 1, 2, 3, 4, 5."

# Por fim, vamos exibir o maior e o menor valor da tupla.
print(f'O maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')
