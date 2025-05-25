# Exercício Python #060 - Cálculo do Fatorial - Aula 00 até 14 - Mundo 2
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial  # Importa a função factorial do módulo math

# Solicita e converte um número para inteiro, em seguida, imprime o fatorial usando a função factorial
numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é {factorial(numero)}.')

print(f'{numero}! = ', end='')  # Exibe o início da expressão do fatorial
fatorial = 1  # Inicializa o acumulador com o número fornecido

# Utilizando WHILE

while numero > 0:
    print(f'{numero}', end='')  # Exibe cada multiplicador
    print(' x ' if numero > 1 else ' = ', end='')  # Exibe ' x ' para multiplicadores intermédios e '=' para o último
    fatorial *= numero  # Atualiza o acumulador multiplicando pelo próximo número
    numero -= 1  # Decrementa o número a ser multiplicado

print(fatorial)  # Exibe o resultado final do fatorial

# Utilizando FOR

while True:
	try:
		número = int(input('Digite um valor para verificar seu fatorial: '))
		fatorial = 1
		print(f'{número}! = ', end='')
		for valor in range(número, 0, -1):
			print(valor, end=' X ' if valor > 1 else ' = ')
			fatorial *= valor
		print(fatorial)
		break
	except ValueError:
		print('Valor inválido')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que lê um número qualquer e mostra o seu fatorial. O fatorial de um número é o produto de todos os números inteiros positivos de 1 até o número fornecido.

# Vamos usar a função factorial() do módulo math para calcular o fatorial de um número. A função factorial() retorna o fatorial de um número inteiro. Se o número for negativo, a função gera um ValueError.

# Primeiro, vamos importar a função factorial() do módulo math. O módulo math fornece funções matemáticas para operações numéricas. A função factorial() calcula o fatorial de um número inteiro.
from math import factorial

# Vamos solicitar um número ao usuário e converter para inteiro. Em seguida, vamos calcular o fatorial do número fornecido usando a função factorial() e exibir o resultado.
numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é {factorial(numero)}.')

# Usando um laço de repetição while, vamos calcular o fatorial do número fornecido. Vamos inicializar o acumulador fatorial com 1 e decrementar o número a ser multiplicado até chegar a 1.
print(f'{numero}! = ', end='')  # Exibe o início da expressão do fatorial

fatorial = 1  # Inicializa o acumulador com o número fornecido. Esse é o valor inicial do fatorial, que é iniciado com o fator neutro da multiplicação, que é 1.

while numero > 0:  # Enquanto o número for maior que 0, o laço de repetição continuará.

    print(f'{numero} x ' if numero > 1 else f'{numero} = ', end='') # Exibe cada multiplicador e ' x ' para multiplicadores intermédios e '=' para o último. Assim teremos a expressão completa do fatorial.
    # Por exemplo, se digitar 5 o programa exibirá: 5 x 4 x 3 x 2 x 1 =
    
    fatorial *= numero  # Atualiza o acumulador multiplicando pelo próximo número
    numero -= 1  # Decrementa o número a ser multiplicado
    
print(fatorial)  # Exibe o resultado final do fatorial fora do laço de repetição
