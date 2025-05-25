# Exercício Python #032 - Ano Bissexto - Aula 00 até 09 - Mundo 1
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from random import randint
from datetime import date

# Tarefa 1: Ler um ano
ano = randint(1582, 2024)
if ano == 0:
    ano = date.today().year
# Tarefa 2: Verificar se é bissexto
# É um número divisível por 4, mas não é divisível por 100.
caso_1 = ano % 4 == 0 and ano % 100 != 0
# É um número divisível por 4, por 100 e por 400.
caso_2 = ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0

if caso_1 or caso_2:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
    
    
# Versão 2 - Completa


def recebe_ano(mensagem):
    """
    Pede ao usuário para digitar um ano e garante que o valor digitado seja um número inteiro.
    """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Valor de tipo inválido! Por favor, digite um número inteiro.')


def verifica_ano(year):
    """
    Verifica se o ano fornecido é bissexto.
    Um ano é bissexto se for divisível por 4 e (não divisível por 100 ou divisível por 400).
    """
    if year > 1582:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    else:
        return False


# Pede ao usuário para digitar um ano
ano = recebe_ano('Digite o ano que deseja verificar: ')

# Verifica se o ano é bissexto
bissexto = verifica_ano(ano)

# Exibe o resultado formatado
if bissexto:
    print(f'O ano {ano} \033[1;32mé bissexto!\033[m')
else:
    print(f'O ano {ano} \033[1;31mnão é bissexto!\033[m')


ano_atual = date.today().year

# Laço para exibir a lista de anos
#for i in range(1582, ano_atual + 1):
#	print(f'O ano {i}', '\033[1;32mé bissexto!\033[m' if verifica_ano(i) else '\033[1;31mnão é bissexto!\033[m')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler um ano qualquer e verificar se ele é bissexto.
# Um ano bissexto é divisível por 4, mas não é divisível por 100, a menos que seja divisível por 400. Agora precisamos escrever isso em código.

# Vamos usar uma estrutura de decisão para verificar se o ano é bissexto. Primeiro, vamos ler o ano digitado pelo usuário com a função input() e converter o valor para inteiro com a função int().
ano = int(input('Digite um ano: '))

# Em seguida, vamos verificar se o ano é bissexto. Para isso, vamos utilizar uma estrutura condicional com a palavra-chave if. Vamos criar duas variáveis chamadas caso_1 e caso_2 para representar as duas condições que definem um ano bissexto.

# A primeira condição é que o ano seja divisível por 4 e não seja divisível por 100. A segunda condição é que o ano seja divisível por 4, por 100 e por 400.
caso_1 = ano % 4 == 0 and ano % 100 != 0
# Se ano for divisível por 4 (resto da divisão por 4 igual a zero) e não for divisível por 100 (resto da divisão por 100 diferente de zero), então é um ano bissexto.

caso_2 = ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0
# Se ano for divisível por 4 (resto da divisão por 4 igual a zero), por 100 (resto da divisão por 100 igual a zero) e por 400 (resto da divisão por 400 igual a zero), então é um ano bissexto.

# Agora, vamos verificar se o ano é bissexto. Se uma das condições for verdadeira, o ano é bissexto.
if caso_1 or caso_2:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

# Podemos capturar o ano atual com a função date.today().year do módulo datetime e exibir uma lista de anos bissextos.
# Para isso, vamos importar a função date do módulo datetime.
from datetime import date

# Em seguida, vamos capturar o ano atual com a função date.today().year.
ano_atual = date.today().year
