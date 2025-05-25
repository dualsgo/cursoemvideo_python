# Exercício Python #042 - Analisando Triângulos v2.0 - Aula 00 até 12 - Mundo 2
# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

# Tarefa 1: Ler três retas
a = int(input('Digite o valor do segmento A: '))
b = int(input('Digite o valor do segmento B: '))
c = int(input('Digite o valor do segmento C: '))

# Tarefa 2: Avaliar se formam um triângulo
print('\033[1;32mPara que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois\033[m')
triangulo = a < b + c and c < b + a and b < a + c
print(triangulo)
print(f'\033[1mA {a} < B {b} + C {c}')
print(f'B {b} < C {c} + A {a}')
print(f'C {c} < A {a} + B {b}\033[m\n')

# Tarefa 2: Definir as condições para cada topo de triângulo

# EQUILÁTERO: todos os lados iguais
equilatero = a == b == c
# ESCALENO: todos os lados diferentes
escaleno = a != b and b != c and a != c
# ISÓSCELES: dois lados iguais, um diferente
isosceles = not equilatero and not escaleno


if triangulo:
    print(f'\033[1mOs segmentos de comprimento a = {a}, b = {b} e c = {c} podem formar um\033[m', end=' ')
    if equilatero:
        print('\033[1;31mTRIÂNGULO EQUILÁTERO - TODOS OS LADOS IGUAIS\033[m')
    elif escaleno:
        print('\033[1;31mTRIÂNGULO ESCALENO - TODOS OS LADOS DIFERENTES\033[m')
    elif isosceles:
        print('\033[1;31mTRIÂNGULO ISÓSCELES - DOIS LADOS IGUAIS E UM DIFERENTE\033[m')
else:
    print(f'Não é possível formar um triângulo com os segmentos a = {a}, b = {b} e c = {c}.')

# Versão 2 - Mais simple e om validação

while True:
	try:
		a, b, c = float(input('Segmento A: ')), float(input('Segmento B: ')), float(input('SegmentoC: '))
	except ValueError:
		print('Apenas valores numéricos')
	else:
		triangulo = a + b > c and a + c > b and a < b + c
		tipo = 'equilátero' if a == b == c else 'escaleno' if a != b != c != a else 'isósceles'

	print(f'{a}, {b} e {c}', f'formam um triângulo {tipo}!' if triangulo else 'não formam um triângulo!')
	break

# Versão mais completa
from emoji import emojize


def segmento_reta(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Erro...')


def verificação(a, b, c):
	if a + b > c and a + c > b and b + c > a:
		return True
	else:
		return False


def tipo_triangulo(a, b, c):
	if a == b == c == a:
		return 'EQUILÁTERO'
	elif a != b != c != a:
		return 'ESCALENO'
	else:
		return 'ISÓSCELES'


segmento_a = segmento_reta(emojize(':régua_reta: Comprimento do segmento A: ', language='pt'))
segmento_b = segmento_reta(emojize(':régua_reta: Comprimento do segmento B: ', language='pt'))
segmento_c = segmento_reta(emojize(':régua_reta: Comprimento do segmento C: ', language='pt'))
triangulo = verificação(segmento_a, segmento_b, segmento_c)

print(
	emojize(f'Os segmentos de reta de comprimento \033[1;33m{segmento_a:.3g}, {segmento_b:.3g} e {segmento_c:.3g}\033[m '
			f'{"\033[1;32mPODEM FORMAR :régua_triangular:\033[m" if triangulo else "\033[1;31mNÃO PODEM FORMAR\033[m"} '
			f'um triângulo{f" do tipo {tipo_triangulo(segmento_a, segmento_b, segmento_c)}" if triangulo else "!"}', language='pt')
)


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler o comprimento de três retas e verificar se elas podem formar um triângulo. Para que três segmentos possam formar um triângulo, cada lado deve ser menor que a soma dos outros dois.

# Você pode copiar o código do exercício 35 e adicionar a verificação do tipo de triângulo. Para isso, você pode criar uma função que recebe os três segmentos de reta e verifica se eles formam um triângulo. Em seguida, você pode criar outra função que recebe os três segmentos de reta e verifica o tipo de triângulo que eles formam.

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
    
# Para verificar o tipo de triângulo, vamos comparar os lados do triângulo.
# Se os três lados forem iguais, o triângulo é equilátero.
# Se dois lados forem iguais e um diferente, o triângulo é isósceles.
# Se os três lados forem diferentes, o triângulo é escaleno.

# Como a comparação de isósceles é mais complexa, vamos verificar primeiro se o triângulo é equilátero ou escaleno. Se não for nenhum dos dois, então é isósceles.

# Para isso, vamos utilizar uma estrutura condicional que verifica se os três lados são iguais, se dois lados são iguais e um diferente ou se os três lados são diferentes.
if segmento_a == segmento_b and segmento_c == segmento_a and segmento_b == segmento_c:
	print('O triângulo é equilátero.')
elif segmento_a != segmento_b and segmento_c != segmento_a and segmento_b != segmento_c:
	print('O triângulo é escaleno.')

# Se os três lados forem diferentes, o triângulo é escaleno.

else:
	print('O triângulo é isósceles.')

# Se não for equilátero nem escaleno, então é isósceles.