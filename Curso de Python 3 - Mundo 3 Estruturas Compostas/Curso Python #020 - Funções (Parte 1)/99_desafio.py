# Exercício Python #099 - Função que descobre o maior - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep
lista_parametros = []


def cria_lista(quantidade, inicio, fim):
    if quantidade == 0:
        print(f'Nenhum valor informado!')
    elif quantidade == 1:
        print(f'Apenas um valor informado.')
    else:
        print(f'Sorteando {quantidade} números entre {inicio} e {fim}')
        for i in range(quantidade):
            lista_parametros.append(randint(inicio, fim))


cria_lista(randint(0, 10), randint(0, 99), randint(100, 999))


def maior(*varios_parametros):
    if len(lista_parametros) == 0:
        print()
    elif len(lista_parametros) == 1:
        print(f'{lista_parametros} é o único número informado.')
    else:
        print(f'Os {len(lista_parametros)} valores adicionados foram: ')
        for v in varios_parametros:
            sleep(.5)
            if v == varios_parametros[-1]:
                print(f'{v}.')
            else:
                print(v, end=', ')
        sleep(1)
        print(f'O menor valor da lista é o {min(varios_parametros)}')
        sleep(1)
        print(f'O maior valor da lista é o {max(varios_parametros)}')


# Usando * para desempacotar a lista ao passá-la como argumento
maior(*lista_parametros)


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, precisamos criar uma função chamada maior() que recebe vários parâmetros com valores inteiros. A função deve analisar todos os valores e dizer qual deles é o maior.

# Vamos criar o programa "auto-suficiente" que sorteia uma quantidade aleatória de números entre 0 e 99 e chama a função maior() passando esses números como argumentos.

from random import randint # Importa a função randint() do módulo random.
from time import sleep # Importa a função sleep() do módulo time.

lista_parametros = [] # Cria uma lista vazia chamada lista_parametros.

# A função cria_lista() recebe três parâmetros: quantidade, início e fim. A função sorteia uma quantidade de números entre início e fim e adiciona esses números à lista lista_parametros.
def cria_lista(quantidade, inicio, fim):
        
        # Se a quantidade de números for igual a zero, exibe a mensagem "Nenhum valor informado!".
        if quantidade == 0:
            print(f'Nenhum valor informado!')
        
        # Se a quantidade de números for igual a um, exibe a mensagem "Apenas um valor informado.".
        elif quantidade == 1:
            print(f'Apenas um valor informado.')
        
        # Se a quantidade de números for maior que um, exibe a mensagem "Sorteando quantidade números entre início e fim" e adiciona os números sorteados à lista lista_parametros.
        else:
            print(f'Sorteando {quantidade} números entre {inicio} e {fim}')
            for i in range(quantidade):
                lista_parametros.append(randint(inicio, fim))
                
                
# A função cria_lista() é chamada com três argumentos: um número aleatório entre 0 e 10, um número aleatório entre 0 e 99 e um número aleatório entre 100 e 999.
cria_lista(randint(0, 10), randint(0, 99), randint(100, 999))

# randint(0, 10) sorteia um número aleatório entre 0 e 10 que será a quantidade de números a serem sorteados.
# randint(0, 99) sorteia um número aleatório entre 0 e 99 que será o início do intervalo dos números a serem sorteados.
# randint(100, 999) sorteia um número aleatório entre 100 e 999 que será o fim do intervalo dos números a serem sorteados.

# A função maior() recebe vários parâmetros. A função exibe os valores adicionados à lista lista_parametros, o menor valor da lista e o maior valor da lista.

# O *
def maior(*varios_parametros):
        
        # Se a lista de parâmetros estiver vazia, exibe uma linha em branco.
        if len(lista_parametros) == 0:
            print()
        
        # Se a lista de parâmetros tiver apenas um valor, exibe o valor da lista.
        elif len(lista_parametros) == 1:
            print(f'{lista_parametros} é o único número informado.')
        
        # Se a lista de parâmetros tiver mais de um valor, exibe os valores da lista, o menor valor e o maior valor.
        else:
            print(f'Os {len(lista_parametros)} valores adicionados foram: ')
            for v in varios_parametros:
                sleep(.5)
                if v == varios_parametros[-1]:
                    print(f'{v}.')
                else:
                    print(v, end=', ')
            sleep(1)
            print(f'O menor valor da lista é o {min(varios_parametros)}')
            sleep(1)
            print(f'O maior valor da lista é o {max(varios_parametros)}')

# Usando * para desempacotar a lista ao passá-la como argumento
maior(*lista_parametros)

# Desempacotar é o processo de converter uma lista em uma sequência de argumentos. O operador * é usado para desempacotar uma lista ao passá-la como argumento para uma função. O operador * é colocado antes do nome da lista. Quando a função é chamada, os elementos da lista são passados como argumentos separados.

# Então se a lista_parametros for [1, 2, 3], ao chamar a função maior(*lista_parametros), a função maior() receberá os argumentos 1, 2 e 3. Se a lista for maior, a função receberá todos os elementos da lista como argumentos.