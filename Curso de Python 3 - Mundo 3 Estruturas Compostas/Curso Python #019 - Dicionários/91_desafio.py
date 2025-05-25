# Exercício Python #091 - Jogo de Dados em Python - Aula 00 até 19 - Mundo 3
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint

# Inicializa uma lista vazia para armazenar os jogadores
jogadores = []

# Loop para criar 4 jogadores
for indice, _ in enumerate(range(4), 1):
    # Cria um dicionário para representar um jogador
    jogador = {'nome': f'Jogador({indice})', 'pontuacao': randint(1, 6)}

    # Imprime a pontuação do jogador
    print(f"O {jogador['nome']} tirou {jogador['pontuacao']}")

    # Aguarda por um segundo para simular um intervalo entre os jogadores
    sleep(1)

    # Adiciona o jogador à lista de jogadores
    jogadores.append(jogador)

# Imprime o título do ranking
print(f'{"Ranking":^20}')

# Ordena a lista de jogadores com base na pontuação, em ordem decrescente
jogadores = sorted(jogadores, key=lambda jogador: jogador['pontuacao'], reverse=True)

# Imprime o ranking com a posição, nome do jogador e pontuação
for indice, jogador in enumerate(jogadores, 1):
    print(f'{indice:<5} {jogador["nome"]} - {jogador["pontuacao"]}')

# V2

from random import randint


def jogada():
    return randint(1, 6)


def obter_nome(mensagem):
    while True:
        entrada = input(mensagem).strip().title()
        condição = entrada.replace(' ', '').isalpha()

        if not condição:
            print('Somente caracteres alfabéticos')
        else:
            return entrada


competidores = []

for jogador in range(1, 5):
    nome = obter_nome(f'Jogador {jogador}: ')
    resultado_jogada = jogada()
    competidor = {nome: resultado_jogada}
    print(f"Adicionando competidor: {nome}")
    competidores.append(competidor.copy())

print(f'{'RANKING':^20}')

competidores = sorted(competidores, key=lambda x: list(x.values())[0], reverse=True)

print(f'{'JOGADOR':^10}{'PONTOS':^10}')
for competidor in competidores:
    for nome, resultado in competidor.items():
        print(f'{nome:^10}{resultado:^10}')



# V3

from random import randint
from time import sleep

jogadores = {f'jogador{i}': randint(1, 6) for i in range(1, 5)}

print(f'{"Sorteio dos jogadores:":^25}')
for jogador, pontuacao in jogadores.items():
    sleep(1)
    print(f'{jogador} tirou o número {pontuacao}')

ranking = sorted(jogadores, key=jogadores.get, reverse=True)

print(f'{"Ranking dos jogadores:":^25}')
for i, jogador in enumerate(ranking, 1):
    print(f'{i}º - {jogador} com {jogadores[jogador]} pontos')


# V4

from time import sleep
from random import randint

# Inicializa uma lista vazia para armazenar os jogadores
jogadores = []

# Loop para criar 4 jogadores
for indice, _ in enumerate(range(4)):
    # Cria um dicionário para representar um jogador
    jogador = {'nome': f'Jogador({indice + 1})', 'pontuacao': randint(1, 6)}

    # Imprime a pontuação do jogador
    print(f"O {jogador['nome']} tirou {jogador['pontuacao']}")

    # Aguarda por um segundo para simular um intervalo entre os jogadores
    sleep(1)

    # Adiciona o jogador à lista de jogadores
    jogadores.append(jogador)

# Imprime o título do ranking
print(f'{"Ranking (sem sorted)":^30}')

# Implementa o algoritmo de ordenação Bubble Sort
# O Bubble Sort é um algoritmo de ordenação simples que percorre repetidamente a lista, compara elementos adjacentes e os troca se estiverem na ordem errada. Esse processo continua até que a lista esteja ordenada.

# n = len(jogadores): Obtém o número total de jogadores na lista. Isso servirá para definir os limites do loop.
n = len(jogadores)

# for i in range(n): O primeiro loop (i) percorre toda a lista.
for i in range(n):

    # for j in range(0, n-i-1): O segundo loop (j) percorre a lista até o elemento n-i-1. A ideia é que após cada passagem do loop externo, o maior elemento já está na posição correta, então podemos reduzir o alcance do loop interno.
    for j in range(0, n - i - 1):

        # Compara as pontuações e troca se necessário
        # if jogadores[j]['pontuacao'] < jogadores[j+1]['pontuacao']:: Compara as pontuações de dois jogadores adjacentes. Se o jogador na posição j tiver uma pontuação menor que o jogador na posição j+1, então precisamos trocar os jogadores para colocar o jogador com a maior pontuação primeiro.

        # jogadores[j], jogadores[j+1] = jogadores[j+1], jogadores[j]: Realiza a troca dos jogadores. Isso é feito usando a técnica de desempacotamento de tuplas no Python. Se a condição do passo anterior for verdadeira, trocamos os jogadores nas posições j e j+1.
        if jogadores[j]['pontuacao'] < jogadores[j + 1]['pontuacao']:
            jogadores[j], jogadores[j + 1] = jogadores[j + 1], jogadores[j]
# Imprime o ranking com a posição, nome do jogador e pontuação
for indice, jogador in enumerate(jogadores, 1):
    print(f'{indice:<5} {jogador["nome"]} - {jogador["pontuacao"]}')
    


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o professor pede para criar um programa que simule um jogo de dados com 4 jogadores. O programa deve sortear um número aleatório para cada jogador e, no final, mostrar o ranking dos jogadores de acordo com a pontuação.

# Primeiramente, vamos importar as bibliotecas necessárias: randint da biblioteca random e sleep da biblioteca time.
from random import randint
from time import sleep

# Vamos criar um dicionário chamado jogadores para armazenar os jogadores e suas pontuações. Para isso, vamos usar um laço de repetição para criar 4 jogadores.

jogadores = {f'jogador{i}': randint(1, 6) for i in range(1, 5)} # Essa linha de código cria um dicionário com 4 jogadores, onde a chave é o nome do jogador e o valor é um número aleatório entre 1 e 6. Os nomes serão 'jogador1', 'jogador2', 'jogador3' e 'jogador4'.

# Vamos imprimir o sorteio dos jogadores. Para isso, vamos percorrer o dicionário jogadores e mostrar o nome do jogador e a pontuação.
print(f'{"Sorteio dos jogadores:":^25}')
for jogador, pontuacao in jogadores.items():
    sleep(1) # Vamos aguardar 1 segundo para simular um intervalo entre os jogadores.
    print(f'{jogador} tirou o número {pontuacao}')

# Para ordenar o dicionário com sorted, precisaremos realizar mais etapas que com uma lista. Primeiro, vamos criar uma lista chamada ranking com as chaves do dicionário jogadores.
ranking = list(jogadores.keys()) # Essa linha de código cria uma lista ranking com as chaves do dicionário jogadores.

# Vamos ordenar a lista ranking com base na pontuação dos jogadores. Para isso, vamos usar a função sorted() com a chave key=jogadores.get para ordenar os jogadores de acordo com a pontuação.
ranking = sorted(ranking, key=jogadores.get, reverse=True) # Essa linha de código ordena a lista ranking com base na pontuação dos jogadores, em ordem decrescente. key=jogadores.get indica que a função de ordenação deve usar o valor da chave (pontuação) para ordenar os jogadores.

# Caso não tenha ficado claro, vamos faser uma função lambda para explicar melhor
# A função lambda é uma função anônima que pode ter qualquer número de argumentos, mas apenas uma expressão. Ela é usada para criar funções simples e pode ser usada em qualquer lugar onde uma função normal seria usada.

# A função lambda é definida com a palavra-chave lambda, seguida pelos argumentos, seguida por dois pontos e, finalmente, pela expressão que será retornada. Por exemplo, lambda x: x + 1 é uma função lambda que recebe um argumento x e retorna x + 1.

# Vamos criar uma função lambda que recebe um jogador e retorna a pontuação desse jogador. Essa função será usada como chave para ordenar os jogadores de acordo com a pontuação.
# key=lambda jogador: jogadores[jogador]: Essa função lambda recebe um jogador e retorna a pontuação desse jogador. Ela será usada como chave para ordenar os jogadores de acordo com a pontuação.

ranking = sorted(ranking, key=lambda jogador: jogadores[jogador], reverse=True) # Essa linha de código ordena a lista ranking com base na pontuação dos jogadores, em ordem decrescente. key=lambda jogador: jogadores[jogador] indica que a função de ordenação deve usar a pontuação do jogador para ordenar os jogadores.

# Vamos imprimir o ranking dos jogadores. Para isso, vamos percorrer a lista ranking e mostrar a posição, o nome do jogador e a pontuação.
print(f'{"Ranking dos jogadores:":^25}')
for i, jogador in enumerate(ranking, 1):
    print(f'{i}º - {jogador} com {jogadores[jogador]} pontos')