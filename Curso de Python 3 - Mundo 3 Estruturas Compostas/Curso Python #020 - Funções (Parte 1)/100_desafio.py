# Exercício Python #100 - Funções para sortear e somar - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

from random import randint
from time import sleep
numeros = []


def sorteia(quantidade):
    for v in range(quantidade):
        numeros.append(randint(0, 9))
    print(f'A lista final é a seguinte: {numeros}')


def somar_pares():
    soma_pares = 0
    for v in numeros:
        if v % 2 == 0:
            soma_pares += v
    print(f'A soma entre todos os valores pares presentes na lista é {soma_pares}')


sorteia(int(input('Digite a quantidade de números que deseja sortear: ')))

somar_pares()

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, precisamos criar um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A função sorteia() sorteia 5 números e coloca-os dentro da lista. A função somaPar() mostra a soma entre todos os valores pares sorteados pela função sorteia().

from random import randint # Importa a função randint() do módulo random.
from time import sleep # Importa a função sleep() do módulo time.

numeros = [] # Cria uma lista vazia chamada números.

# A função sorteia() recebe um parâmetro chamado quantidade. A função sorteia uma quantidade de números entre 0 e 9 e adiciona esses números à lista números.
def sorteia(quantidade):
        
        # A função append() é usada para adicionar um número à lista números.
        for v in range(quantidade):
            numeros.append(randint(0, 9))
        print(f'A lista final é a seguinte: {numeros}')
        
# A função somar_pares() calcula a soma de todos os valores pares presentes na lista números.
def somar_pares():
    soma_pares = 0
    for v in numeros:
        if v % 2 == 0:
            soma_pares += v
    print(f'A soma entre todos os valores pares presentes na lista é {soma_pares}')
    
# A função sorteia() é chamada com o argumento quantidade que é a quantidade de números que o usuário deseja sortear.
sorteia(int(input('Digite a quantidade de números que deseja sortear: ')))

# A função somar_pares() é chamada para calcular a soma de todos os valores pares presentes na lista números.
somar_pares()