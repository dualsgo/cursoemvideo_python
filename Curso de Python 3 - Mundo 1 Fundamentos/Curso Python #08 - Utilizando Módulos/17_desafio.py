# Exercício Python #017 - Catetos e Hipotenusa - Aula 00 até 08 - Mundo 1
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de uma triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

"""O teorema de Pitágoras descreve a relação entre os lados de um triângulo retângulo. Ele afirma que, para qualquer triângulo retângulo com lados de comprimento a e b, e hipotenusa de comprimento c, a2 + b2 = c2"""

from emoji import emojize
from math import hypot

from cisco_fundamentos_python.python_essentials_1.modulo_4.m4_aula_2 import hi

# Tarefa 1: Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
cateto_oposto = float(input(emojize(':régua_triangular: Digite o comprimento do cateto oposto: ', language='pt')))
cateto_adjacente = float(input(emojize(':régua_triangular: Digite o comprimento do cateto adjacente: ', language='pt')))

# Tarefa 2: Calcular e mostrar o comprimento da hipotenusa.
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f'O comprimento da hipotenusa de cateto oposto {cateto_oposto} e cateto adjacente {cateto_adjacente} é {hipotenusa:.2f}.')


# Versão 2


def comprimento(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Valor inválido!')


oposto = comprimento('Comprimento do cateto oposto: ')
adjacente = comprimento('Comprimento do cateto adjacente: ')
hipotenusa = (oposto ** 2 + adjacente ** 2) ** .5

print(f'{'Cateto oposto:':<20}{oposto:>10.3g}\n{'Cateto adjacente:':<20}{adjacente:>10.3g}\n{'Hipotenusa:':<20}{hipotenusa:>10.3g}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e calcula o comprimento da hipotenusa. O teorema de Pitágoras é utilizado para realizar o cálculo.

# A fórmla do teorema de Pitágoras é a² + b² = c², onde a e b são os comprimentos dos catetos oposto e adjacente, respectivamente, e c é o comprimento da hipotenusa.

# Sendo assim, podemos fazer manualmente o cálculo da hipotenusa utilizando a fórmula do teorema de Pitágoras. Primeiro, lemos os comprimentos dos catetos oposto e adjacente do usuário.
a = float(input('Digite o comprimento do cateto oposto: ')) # Cateto oposto
b = float(input('Digite o comprimento do cateto adjacente: ')) # Cateto adjacente

# Em seguida, calculamos o quadrado do comprimento de cada cateto.
a_quadrado = a ** 2
b_quadrado = b ** 2

# Somamos os quadrados dos catetos entre parenteses e calculamos a raiz quadrada do resultado para obter o comprimento da hipotenusa. A raiz será obtida atravez do expoente 0.5.
hipotenusa = (a_quadrado + b_quadrado) ** .5

# Matematicamente, como falado no exercíco 13, a raiz quadrada de um número é o mesmo que elevar o número a 1/2 pois a raiz quadrada é a operação inversa da exponenciação.

# 2 pode ser escrito como 2/1, então o recíproco é 1/2. Portanto, é por isso que a raiz quadrada de um número é o mesmo que elevar o número a 1/2 (ou 0.5).

# É importante aprender a lógica por trás do cálculo da hipotenusa, mas o Python já possui funções embutidas que facilitam a realização desse cálculo.

# Por exemplo, para obter a exponenciação de um número, podemos utilizar o operador **. Para calcular a raiz quadrada de um número, podemos utilizar a função sqrt() do módulo math.

# Poderíamos substituir nosso cálculo anterior pela função sqrt() para obter o mesmo resultado. Devemos importar o módulo math no início do programa para utilizar a função sqrt().
# hipotenusa = sqrt(a ** 2 + b ** 2)

# Mas para facilitar mais ainda, podemos utilizar a função hypot() do módulo math para calcular a hipotenusa diretamente. A função hypot() calcula a hipotenusa de um triângulo retângulo a partir dos comprimentos dos catetos oposto e adjacente.

# A função hypot() recebe dois argumentos, que são os comprimentos dos catetos oposto e adjacente, e retorna o comprimento da hipotenusa.
# hipotenusa = hypot(a, b)