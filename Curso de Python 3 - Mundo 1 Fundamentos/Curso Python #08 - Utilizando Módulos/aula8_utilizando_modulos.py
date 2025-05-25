# Curso Python #08 - Utilizando Módulos
# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.
import math
from math import sqrt
from random import randint
from emoji import emojize

# Módulos (pacotes, bibliotecas) - São pacotes de comandos e recursos, que são funcionalidades extras.

# Usamos o comando "import biblioteca" para importar esses módulos
# Se quisermos importar apenas algumas funcionalidades específicas, usamos o comando "from biblioteca import funcionalidade"

# Exemplo de biblioteca padrão math - Sintaxe

"""import math
print(math.pow(4,2))"""
"""from math import pow
print(pow(4, 2))"""

# Exemplos de funcionalidades

# ceil - arredondamento para cima
# floor - arredondamento para baixo
# trunc - remove os decimais (não é arredondamento)
# pow - exponenciação
# sqrt - raiz quadrada
# factorial - fatorial
# randint - gera um número aleatório

num = int(input('Digite um número: '))
# Calcular a raiz quadrada
print(f'A raiz quadrada de {num} é {sqrt(num)}.')

num = randint(1, 99)
# Calcular a raiz quadrada com número aleatório
print(f'A raiz quadrada de {num} é {sqrt(num)}.')
print('❤️‍🔥')

print(dir(math))
print(help(math))


print(emojize(':coração_preto:', language='pt'))
# Aliasing - Podemos atribuir um apelido para um módulo
# import math as m torna o módulo math acessível como m, facilitando a digitação.
# from math import sqrt as s torna a função sqrt acessível como s, facilitando a digitação.

# Se quisermos importar vários módulos, podemos usar o comando "import biblioteca1, biblioteca2, biblioteca3"
# Se quisermos importar todas as funcionalidades de um módulo, podemos usar o comando "from biblioteca import *" ou simplesmente "import biblioteca"