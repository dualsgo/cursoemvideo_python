# Exercício Python #035 - Analisando Triângulo v1.0 - Aula 00 até 09 - Mundo 1
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# b + c > a
from random import randint
# Tarefa 1: Ler três retas
a = randint(1, 99)
b = randint(1, 99)
c = randint(1, 99)

# Tarefa 2: Avaliar se formam um triângulo
print('Para que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois')
triangulo = b + c > a and b + a > c and a + c > b

print(f'A {a} + B {b} > C {c}')
print(f'B {b} + C {c} > A {a}')
print(f'C {c} + A {a} > B {b}')

if triangulo:
    print(f'Os segmentos de comprimento a={a}, b={b} e c={c} podem formar um triângulo!')
else:
    print(f'Não é possível formar um triângulo com os segmentos a={a}, b={b} e c={c}.')
    
    
# Versão 2 - Com validaçãO

def segmento_reta(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Erro...')

def verificação(a, b, c):
		return '\033[1;32mPODEM FORMAR\033[m' if a + b > c and a + c > b and b + c > a else '\033[1;31mNÃO PODEM FORMAR\033[m'



segmento_a = segmento_reta('Comprimento do segmento A: ')
segmento_b = segmento_reta('Comprimento do segmento B: ')
segmento_c = segmento_reta('Comprimento do segmento C: ')
triangulo = verificação(segmento_a, segmento_b, segmento_c)

print(f'Os segmentos de reta de comprimento \033[1;33m{segmento_a:.3g}, {segmento_b:.3g} e {segmento_c:.3g}\033[m {triangulo} um triângulo!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler o comprimento de três retas e verificar se elas podem formar um triângulo. Para que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois.

# A primeira coisa a ser feita é ler o comprimento dos três segmentos de reta. Para isso, vamos utilizar a função input() para ler os valores e a função float() para converter os valores para ponto flutuante.
segmento_a = float(input('Comprimento do segmento A: '))
segmento_b = float(input('Comprimento do segmento B: '))
segmento_c = float(input('Comprimento do segmento C: '))

# Em seguida, vamos verificar se os segmentos de reta podem formar um triângulo. Para isso, vamos utilizar uma estrutura condicional que verifica se cada lado é menor que a soma dos outros dois.
triangulo = segmento_a + segmento_b > segmento_c and segmento_a + segmento_c > segmento_b and segmento_b + segmento_c > segmento_a

# Temos que comparar todas as possibilidades: Se a soma de A e B for maior que C, se a soma de A e C for maior que B e se a soma de B e C for maior que A. Se todas essas condições forem verdadeiras, os segmentos podem formar um triângulo. Caso contrário, não é possível formar um triângulo.

# Por fim, vamos exibir uma mensagem informando se os segmentos de reta podem ou não formar um triângulo.
if triangulo:
    print(f'Os segmentos de reta de comprimento {segmento_a}, {segmento_b} e {segmento_c} podem formar um triângulo!')
else:
    print(f'Não é possível formar um triângulo com os segmentos de reta de comprimento {segmento_a}, {segmento_b} e {segmento_c}.')