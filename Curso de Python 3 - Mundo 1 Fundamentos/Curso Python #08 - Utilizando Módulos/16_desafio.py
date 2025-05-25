# Exercício Python #016 - Quebrando um número - Aula 00 até 08 - Mundo 1
# Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.

# Tarefa 1: Ler um número pelo teclado.
from math import trunc
numero = float(input('Digite um número: '))

# Tarefa 2: Mostrar na tela a sua porção inteira.
print(f'A parte inteira do número {numero} é {trunc(numero)}.')
print(f'A parte decimal é {numero - trunc(numero):.3f}.')

# Versão 2

while True:
    try:
        número = float(input('Digite um valor: '))
        parte_inteira = número // 1
        parte_decimal = número % 1
        convertido = str(número)
        tamanho = len(convertido)
        tamanho_decimal = len(convertido[convertido.index('.'):])
        print(f'{"Número:":<10}\033[1;33m{número:>{tamanho}}\033[m\n'
              f'{"Inteiro:":<10}\033[1;31m{parte_inteira:<{tamanho}.1g}\033[m\n'
              f'{"Decimal:":<10}\033[1;32m{parte_decimal:>{tamanho}.{tamanho_decimal}g}\033[m')
        break

    except ValueError:
        print('Valor inválido!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário um número qualquer e exibe na tela a sua porção inteira. A porção inteira de um número é a parte inteira do número, ou seja, a parte que não contém a parte decimal.

# Primeiro, utilizamos a função input() para solicitar um valor ao usuário. O valor digitado é convertido para ponto flutuante e armazenado na variável número.
número = float(input('Digite um valor: '))

# Em seguida, para obter a parte inteira do número, podemos utilizar a função int() para converter o número para inteiro. Isso remove a parte decimal do número, deixando apenas a parte inteira.
parte_inteira = int(número)

# Outra forma seria utilizando a operação de divisão inteira (//) do Python. A divisão inteira de um número por 1 resulta na parte inteira do número. Por exemplo, a divisão inteira de 5.7 por 1 é 5, pois a parte inteira de 5.7 é 5.
parte_inteira = número // 1

# Existe também a possibilidade de utilizar a função trunc() do módulo math para obter a parte inteira de um número. A função trunc() retorna a parte inteira de um número, removendo a parte decimal. Por exemplo, trunc(5.7) é 5.

# Para utilziar a função trunc(), é necessário importar o módulo math no início do programa.
# Podemos importar todo o módulo math com a instrução import math
# A sintaxe de invoção da função trunc() é math.trunc(número), onde número é o valor do qual queremos obter a parte inteira.

# Ou importar apenas a função trunc() com a instrução from math import trunc.
# A sintaxe de invocação da função trunc() é trunc(número), onde número é o valor do qual queremos obter a parte inteira.
parte_inteira = trunc(número)

# Agora basta exibir na tela o número digitado e a sua parte inteira.
print(f'O número digitado foi {número} e a sua parte inteira é {parte_inteira}.')

# ATENÇÃO: round(), floor() e ceil() são outras funções do módulo math que podem ser utilizadas para arredondar números. A função round() arredonda um número para o inteiro mais próximo, a função floor() arredonda para baixo e a função ceil() arredonda para cima. Nesse exercício elas não são adequadas, pois não se trata de arredondamento, mas sim de obter a parte inteira do número.
