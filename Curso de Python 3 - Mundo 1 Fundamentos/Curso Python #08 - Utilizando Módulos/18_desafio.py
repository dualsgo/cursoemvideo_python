# Exercício Python #018 - Seno, Cosseno e Tangente - Aula 00 até 08 - Mundo 1
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

while True:
	try:
		angulo = radians(float(input('Digite o valor do ângulo:')))
		seno = sin(angulo)
		cosseno = cos(angulo)
		tangente = tan(angulo)
		print(f'{'Seno:':<12}{seno:>5.2f}\n{'Cosseno:':<12}{cosseno:>5.2f}\n{'Tangente:':<12}{tangente:>5.2f}')
		break
	except ValueError:
		print('Valor inválido!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário um ângulo em graus e exibe na tela o valor do seno, cosseno e tangente desse ângulo. Para calcular o seno, cosseno e tangente de um ângulo, é necessário converter o ângulo de graus para radianos. Isso porque as funções sin(), cos() e tan() do Python utilizam ângulos em radianos.

# O seno de um ângulo é a razão entre o cateto oposto e a hipotenusa de um triângulo retângulo. 
# O cosseno é a razão entre o cateto adjacente e a hipotenusa. 
# A tangente é a razão entre o cateto oposto e o cateto adjacente.

# Para calcular o seno, cosseno e tangente de um ângulo, precisamos dos valores dos catetos oposto e adjacente e da hipotenusa de um triângulo retângulo.

# Primeiro, pegamos o valor do ângulo em graus e convertemos para radianos
angulo = float(input('Digite o valor do ângulo: '))

# Como estamos fazendo manualmente, a fórmula para converter graus para radianos é: radianos = graus * pi / 180
pi = 3.14159265359
angulo_rad = angulo * pi / 180

# Vamos calcular as aproximações do seno e cosseno usando as séries de Taylor
# Série de Taylor para seno: sen(x) ≈ x - x³/3! + x⁵/5! - x⁷/7! + ...
# Série de Taylor para cosseno: cos(x) ≈ 1 - x²/2! + x⁴/4! - x⁶/6! + ...

# Para simplificação, consideraremos até o terceiro termo da série
# Calculando o valor do seno
seno = angulo_rad - (angulo_rad**3) / 6 + (angulo_rad**5) / 120

# Calculando o valor do cosseno
cosseno = 1 - (angulo_rad**2) / 2 + (angulo_rad**4) / 24

# A tangente é a razão entre o seno e o cosseno
tangente = seno / cosseno

# Agora mostramos os resultados
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')

# Porém o Python nos oferece funções embutidas que facilitam o cálculo do seno, cosseno e tangente de um ângulo. Para isso, utilizamos as funções sin(), cos() e tan() do módulo math. # Como iremos trabalhar com radianos, é necessário converter o ângulo de graus para radianos. Para isso, utilizamos a função radians() do módulo math.

# Primeiro, importamos as funções que iremos utilizar do módulo math.
# from math import sin, cos, tan, radians

# Em seguida, solicitamos ao usuário o valor do ângulo em graus e convertemos para radianos.
angulo = radians(float(input('Digite o valor do ângulo: ')))

# Note que em apenas uma instrução, convertemos o valor digitado para float(), já que queremos realziar uma operação matemática e o input() retorna uma string, e em seguida convertemos o valor para radianos com a função radians().

# Agora, calculamos o seno, cosseno e tangente do ângulo utilizando as funções sin(), cos() e tan().
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

# Por fim, exibimos os resultados na tela.
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')

# Usamos a notação de dois pontos (:) para indicar que queremos exibir o valor com duas casas decimais. O .2f é uma formatação específica para números reais.
