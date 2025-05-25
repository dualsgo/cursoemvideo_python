# Exercício Python #095 - Aprimorando os Dicionários - Aula 00 até 19 - Mundo 3
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from random import randint
jogadores = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    jogador['gols'] = []

    for jogo in range(jogos):
        print(f'Gols marcados na {jogo + 1}º partida: ')
        jogador["gols"].append(randint(0, 4))

    jogador["total"] = sum(jogador["gols"])
    jogadores.append(jogador.copy())

    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

media = jogador["total"] / jogos

print(f'{"Nome":^10}|{"Gols":^15}|{"Total":^10}|{"Média":^10}')

for i, v in enumerate(jogadores):
    print(f'{v["nome"]:^10}|{str(v["gols"]):^15}|{v["total"]:^10}|{media:^10}')

# Loop para visualizar estatisticas individualmente
while True:
    ident = int(input('Digite o ID do jogador:'))

    # Verifica se o ID é válido
    if 0 <= ident < len(jogadores):
            print(
                f'{jogadores[ident]["nome"]}, jogou {len(jogadores[ident]["gols"])} partidas e marcou {jogadores[ident]["total"]} gols. Média de {media} gols por partida.')
            for ind, gol in enumerate(jogadores[ident]['gols'], 1):
                print(f'Partida {ind} - {gol} gols')
    else:
        # Caso o ID seja inválido, exibe uma mensagem de erro
        print('ID do aluno inválido. Tente novamente.')

    continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Loop para garantir que o usuário forneça uma entrada válida
    while continuar not in 'SN':
        continuar = str(input('Ver outro aluno? S/N')).strip().upper()

    # Se o usuário escolher 'N', encerra o programa
    if continuar == 'N':
        print('Encerrando...')
        break
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o professor pede para criar um programa que gerencie o aproveitamento de vários jogadores de futebol. O programa deve ler o nome do jogador, a quantidade de partidas disputadas e a quantidade de gols marcados em cada partida. No final, o programa deve mostrar o total de gols marcados pelo jogador.

# Para resolver esse exercício, vamos criar uma lista chamada jogadores para armazenar os dados de vários jogadores. Vamos criar um dicionário chamado jogador para armazenar o nome, a quantidade de partidas e a quantidade de gols por partida. Vamos criar uma lista chamada gols para armazenar a quantidade de gols em cada partida.
jogador = dict()
jogadores = []
gols = []

# Vamos criar um laço de repetição para adicionar vários jogadores à lista jogadores. Dentro do laço, vamos pedir o nome do jogador e a quantidade de partidas disputadas.
while True:
        
        # Vamos adicionar o nome do jogador ao dicionário jogador.
        jogador['nome'] = str(input('Nome do jogador: '))
        jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
        
        # Vamos criar um laço de repetição para adicionar a quantidade de gols em cada partida à lista gols.
        for jogo in range(jogos):
            gols.append(int(input(f'Gols marcados na {jogo + 1}º partida: ')))
        
        # Vamos adicionar a lista gols ao dicionário jogador.
        jogador['gols'] = gols.copy()
        
        # Vamos adicionar o total de gols ao dicionário jogador.
        jogador['total'] = sum(gols)
        
        # Vamos adicionar o dicionário jogador à lista jogadores.
        jogadores.append(jogador.copy())
        
        # Vamos perguntar se o usuário deseja continuar adicionando jogadores.
        continuar = ''
        while continuar not in 'SN':
            continuar = str(input('Continuar? S/N ')).strip().upper()
        else:
            if continuar == 'S':
                print('Prosseguindo...')
            else:
                print('Encerrando...')
                break

# Vamos calcular a média de gols por partida.
media = jogador['total'] / jogos

# Vamos mostrar os dados dos jogadores na tela.
print(f'{"Nome":^10}|{"Gols":^15}|{"Total":^10}|{"Média":^10}')

for i, v in enumerate(jogadores):
    print(f'{v["nome"]:^10}|{str(v["gols"]):^15}|{v["total"]:^10}|{media:^10}')

# Vamos criar um laço de repetição para visualizar as estatísticas de cada jogador individualmente.
while True:
    ident = int(input('Digite o ID do jogador:'))

    # Verificamos se o ID é válido.
    if 0 <= ident < len(jogadores):
            print(
                f'{jogadores[ident]["nome"]}, jogou {len(jogadores[ident]["gols"])} partidas e marcou {jogadores[ident]["total"]} gols. Média de {media} gols por partida.')
            for ind, gol in enumerate(jogadores[ident]['gols'], 1):
                print(f'Partida {ind} - {gol} gols')
    else:
        # Caso o ID seja inválido, exibimos uma mensagem de erro.
        print('ID do aluno inválido. Tente novamente.')

    continuar = str(input('Ver outro jogador? S/N')).strip().upper()

    # Laço para garantir que o usuário forneça uma entrada válida.
    while continuar not in 'SN':
        continuar = str(input('Ver outro jogador? S/N')).strip().upper()

    # Se o usuário escolher 'N', encerramos o programa.
    if continuar == 'N':
        print('Encerrando...')
        break

