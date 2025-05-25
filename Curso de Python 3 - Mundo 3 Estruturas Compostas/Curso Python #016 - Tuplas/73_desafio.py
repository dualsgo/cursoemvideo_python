# Exercício Python #073 - Tuplas com Times de Futebol - Aula 00 até 16 - Mundo 3
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

# Versão 1

from random import choice

cores_ansi = {
    'azul_escuro': '\033[44;30m',  # Fundo azul escuro, texto preto
    'azul_claro': '\033[104;30m',  # Fundo azul claro, texto preto
    'verde': '\033[42;30m',        # Fundo verde, texto preto
    'cinza': '\033[47;30m',        # Fundo cinza, texto preto
    'vermelho': '\033[41;30m',     # Fundo vermelho, texto preto
    'reset': '\033[0m'             # Reset para o padrão
}

times = (
    'Flamengo', 'Botafogo', 'Palmeiras', 'Fortaleza', 'Cruzeiro',
    'São Paulo', 'Bahia', 'Athletico-PR', 'Atlético-MG', 'Bragantino',
    'Vasco', 'Criciúma', 'Juventude', 'Internacional', 'Corinthians',
    'Grêmio', 'Vitória', 'Cuiabá', 'Fluminense', 'Atlético-GO'
)

lista_times = list(times)
time_escolhido = choice(lista_times)
posição_time = None

título = f'  Tabela Campeonato Brasileiro 2024 - 20ª Rodada  '
tamanho = len(título)
print(f'{"-" * tamanho}')
print(título)
print(f'{"-" * tamanho}')

for posição, equipe in enumerate(times, 1):
    if equipe == time_escolhido:
        posição_time = posição
    if 1 <= posição <= 4:
        cor = cores_ansi['azul_escuro']
    elif 5 <= posição <= 6:
        cor = cores_ansi['azul_claro']
    elif 7 <= posição <= 12:
        cor = cores_ansi['verde']
    elif 13 <= posição <= 16:
        cor = cores_ansi['cinza']
    else:
        cor = cores_ansi['vermelho']

    print(f'{cor}{posição:2}º | {equipe:<20}{cores_ansi["reset"]}')

print('Times em ordem alfabética:')
em_ordem = sorted(times)

for i, time in enumerate(em_ordem):
    print(time, end=', ' if i < (len(em_ordem) -1) else '.\n')

print(f'Time: {time_escolhido} - Posição atual: {posição_time}')

# Lista de times do Brasileirão 2023
times = ('Palmeiras - SP', 'Gremio - RS', 'Atlético Mineiro - MG', 'Flamengo - RJ', 'Botafogo - RJ', 'Red Bull Bragantino - SP', 'Fluminense - RJ', 'Athletico - PR', 'Internacional - RS', 'Fortaleza - CE', 'São Paulo - SP', 'Cuiaba - MT', 'Corinthians - SP', 'Cruzeiro - MG', 'Vasco da Gama - RJ', 'Bahia - BA', 'Santos - SP', 'Goias - GO', 'Coritiba - PR', 'America - MG')

# Imprime os participantes do Brasileirão 2023 em ordem alfabética
print('\033[1mPARTICIPANTES BRASILEIRÃO 2023\033[m')
times_em_ordem = sorted(times)
for equipe in times_em_ordem:
    print(f'{equipe}')
print('\n')

# Imprime a tabela completa do Brasileirão 2023
print('TABELA BRASILEIRÃO 2023')
for posicao, equipe in enumerate(times):
    print(f'{posicao+1:2}º - {equipe}')
print('\n')

# Separa as equipes nas diferentes zonas (Libertadores, Pré-Libertadores, Sul-Americana, Zona Neutra e Rebaixamento)
libertadores = times[:4]
print('\033[1;32mZona da Libertadores - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(libertadores):
    print(f'{posicao+1:2}º - {equipe}')

pre_libertadores = times[4:6]
print('\033[1;36mZona da Pré Libertadores - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(pre_libertadores, start=4):
    print(f'{posicao+1:2}º - {equipe}')

sulamericana = times[6:14]
print('\033[1;34mZona da Sul-Americana - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(sulamericana, start=6):
    print(f'{posicao+1:2}º - {equipe}')

nada = times[14:16]
print('\033[1;37mZona Neutra - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(nada, start=14):
    print(f'{posicao+1:2}º - {equipe}')

rebaixados = times[16:]
print('\033[1;31mZona de Rebaixamento - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(rebaixados, start=17):
    print(f'{posicao:2}º - {equipe}')
print('\n')

# Letra D - Imprime a posição do CR Vasco da Gama - RJ
print('Posição do CR Vasco da Gama- RJ')
posicao_vasco = times.index('CR Vasco da Gama - RJ') + 1
print(f'O Vasco terminou o campeonato em {posicao_vasco}º')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nessse exercício, vamos criar um programa que tenha uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. O programa deve mostrar:

# Vamos importar a função choice da biblioteca random para escolher um time aleatório.
from random import choice

# Vamos criar um dicionário com as cores ANSI para colorir a saída do programa. Um dicinário é uma coleção de objetos que são indexados por chaves. Este tópicos será abordado em detalhes futuramente
cores_ansi = {
    'azul_escuro': '\033[44;30m',  # Fundo azul escuro, texto preto
    'azul_claro': '\033[104;30m',  # Fundo azul claro, texto preto
    'verde': '\033[42;30m',        # Fundo verde, texto preto
    'cinza': '\033[47;30m',        # Fundo cinza, texto preto
    'vermelho': '\033[41;30m',     # Fundo vermelho, texto preto
    'reset': '\033[0m'             # Reset para o padrão
}

# Vamos criar uma tupla com os times do Campeonato Brasileiro de 2024. A ordem dos times é aleatória.
# OBS.: Você pode organizar a lista de times baseado na tabela atual
times = (
    'Flamengo', 'Botafogo', 'Palmeiras', 'Fortaleza', 'Cruzeiro',
    'São Paulo', 'Bahia', 'Athletico-PR', 'Atlético-MG', 'Bragantino',
    'Vasco', 'Criciúma', 'Juventude', 'Internacional', 'Corinthians',
    'Grêmio', 'Vitória', 'Cuiabá', 'Fluminense', 'Atlético-GO'
)

# Vamos criar uma lista a partir da tupla times para poder manipular os dados.
lista_times = list(times)
# Vamos escolher um time aleatório da lista de times.
time_escolhido = choice(lista_times)
# Vamos criar uma variável para armazenar a posição do time escolhido. O valor inicial é None. None é um tipo de dado que representa a ausência de valor.
posição_time = None

# Vamos criar uma variável título para exibir o título do programa. Assim podemos centralizar o texto.
título = f'  Tabela Campeonato Brasileiro 2024 - 20ª Rodada  '
# Vamos calcular o tamanho do título para centralizar a mensagem.
tamanho = len(título)

# Vamos exibir o título do programa. Como sabemos o tamanho do título, podemos criar uma linha com o mesmo tamanho.
print(f'{"-" * tamanho}')
print(título)
print(f'{"-" * tamanho}')

# Vamos percorrer a lista de times e exibir a posição e o nome do time. Vamos colorir a saída de acordo com a posição do time.
for posição, equipe in enumerate(times, 1):
    if equipe == time_escolhido:
        posição_time = posição
    if 1 <= posição <= 4:
        cor = cores_ansi['azul_escuro']
    elif 5 <= posição <= 6:
        cor = cores_ansi['azul_claro']
    elif 7 <= posição <= 12:
        cor = cores_ansi['verde']
    elif 13 <= posição <= 16:
        cor = cores_ansi['cinza']
    else:
        cor = cores_ansi['vermelho']
# Vamos exibir a posição e o nome do time. Vamos resetar a cor para o padrão.
    print(f'{cor}{posição:2}º | {equipe:<20}{cores_ansi["reset"]}')

# Vamos exibir os times em ordem alfabética.
print('Times em ordem alfabética:')
em_ordem = sorted(times) # Para organizar em ordem alfabética, vamos usar a função sorted. Esta função retorna uma nova lista ordenada a partir dos elementos da sequência, então não altera a lista original. Precisamos armazenar o resultado em uma nova variável.


# Vamos percorrer a lista de times em ordem alfabética e exibir o nome do time. Vamos separar os times por vírgula, exceto o último time que será seguido de um ponto final.
for i, time in enumerate(em_ordem):
    print(time, end=', ' if i < (len(em_ordem) -1) else '.\n')

# Vamos exibir o time escolhido e a posição atual do time na tabela.
print(f'Time: {time_escolhido} - Posição atual: {posição_time}')

