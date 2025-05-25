# Exercício Python #093 - Cadastro de Jogador de Futebol - Aula 00 até 19 - Mundo 3
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from time import sleep

jogadores = []

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    jogador['gols'] = []

    for jogo in range(jogos):
        jogador["gols"].append(int(input(f'Quantos gols na partida {jogo + 1}? ')))
    jogador["total"] = sum(jogador["gols"])

    jogadores.append(jogador.copy())

    continuar = str(input('Continuar? S/N ')).strip().upper()

    if continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

sleep(1)

# Calcula a média corretamente
for i, v in enumerate(jogadores):
    media = v["total"] / len(v["gols"])
    print(f'{v["nome"]}, jogou {len(v["gols"])} partidas e marcou {v["total"]} gols. Média de {media:.2f} gols por partida.')
    sleep(1)
    for ind, gol in enumerate(v['gols']):
        print(f'Partida {ind + 1} - {gol} gols')
        sleep(1)


# V2

informações = dict()
partidas = list()

informações['nome'] = input('Nome do jogador: ')
informações['partidas'] = int(input('Quantidade de partidas: '))

for i in range(1, informações['partidas']+1):
	partidas.append(int(input(f'Quantos gols marcados na partida {i}? ')))

informações['gols'] = partidas
informações['total'] = sum(partidas)

for c, v in informações.items():
	print(f'{c}: {v}')

for i, v in enumerate(informações['gols'], 1):
	print(f'Partida {i}: {v} gols')

# V3

def print_error(message):
	print(f'\033[1;31m{message}\033[m')


def obtem_nome():
	while True:
		entrada_nome = input('Digite o nome: ').strip().title()
		if entrada_nome.replace(' ', '').isalpha():
			return entrada_nome
		else:
			print_error('NOME INVÁLIDO! Apenas caracteres alfabéticos.')


def obtem_inteiro(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print_error('Valor inválido para essa operação!')


dados = list()
jogador = dict()
jogos = list()

jogador['nome'] = obtem_nome()
jogador['partidas'] = obtem_inteiro('Digite a quantidade de partidas disputadas: ')
quantidade_partidas = jogador['partidas']

if quantidade_partidas > 1:
	for partida in range(quantidade_partidas):
		jogos.append(obtem_inteiro(f'Gols marcados na {partida + 1}ª partida: '))
else:
	jogador['gols_por_partida'] = obtem_inteiro('Gols marcados na partida: ')

jogador['gols_por_partida'] = jogos
jogador['total_gols'] = sum(jogos)
dados.append(jogador)
print(dados)

titulos = {
	'nome': 'Nome',
	'partidas': 'Partidas disputadas',
	'gols_por_partida': 'Gols por jogo',

	'total_gols': 'Gols marcados'
}

for i in dados:
	for chave, valor in jogador.items():
		titulo = titulos.get(chave, chave)
		if valor == jogador['gols_por_partida']:
			for c, v in enumerate(jogador['gols_por_partida'], 1):
				print(f'{f'Partida {c}':<30}{f'{v} gols':>15}')
		else:
			print(f'{titulo:<30}{valor:>15}')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o professor pede para criar um programa que gerencie o aproveitamento de um jogador de futebol. O programa deve ler o nome do jogador, a quantidade de partidas disputadas e a quantidade de gols marcados em cada partida. No final, o programa deve mostrar o total de gols marcados pelo jogador.

# Para resolver esse exercício, vamos criar um dicionário chamado jogador para armazenar o nome, a quantidade de partidas e a quantidade de gols por partida. Vamos criar uma lista chamada jogos para armazenar a quantidade de gols em cada partida.
jogador = dict()
jogos = []

# Vamos criar uma função chamada obtem_nome para obter o nome do jogador. Essa função deve verificar se o nome contém apenas caracteres alfabéticos.
def obtem_nome():
    while True:
        entrada_nome = input('Digite o nome: ').strip().title()
        if entrada_nome.replace(' ', '').isalpha():
            return entrada_nome
        else:
            print('\033[1;31mNOME INVÁLIDO! Apenas caracteres alfabéticos.\033[m')
            
# Vamos criar uma função chamada obtem_inteiro para obter um valor inteiro. Essa função deve tratar exceções caso o usuário digite um valor inválido.
def obtem_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('\033[1;31mValor inválido para essa operação!\033[m')
            
# Vamos criar uma lista chamada dados para armazenar os dados do jogador.
dados = []

# Vamos obter o nome do jogador e a quantidade de partidas disputadas.
jogador['nome'] = obtem_nome()
jogador['partidas'] = obtem_inteiro('Digite a quantidade de partidas disputadas: ')
quantidade_partidas = jogador['partidas']

# Se o jogador disputou mais de uma partida, vamos obter a quantidade de gols em cada partida.
if quantidade_partidas > 1:
    for partida in range(quantidade_partidas):
        jogos.append(obtem_inteiro(f'Gols marcados na {partida + 1}ª partida: '))
else:
	jogador['gols_por_partida'] = obtem_inteiro('Gols marcados na partida: ')

# Vamos adicionar a quantidade de gols por partida e o total de gols ao dicionário jogador.
jogador['gols_por_partida'] = jogos
jogador['total_gols'] = sum(jogos)

# Vamos adicionar o dicionário jogador à lista dados.
dados.append(jogador)

# Vamos criar um dicionário chamado titulos para armazenar os títulos das colunas E seus respectivos títulos em português para melhorar a visualização dos dados.

titulos = {
    'nome': 'Nome',
    'partidas': 'Partidas',
    'gols_por_partida': 'Gols por partida',
    'total_gols': 'Gols marcados'
}

# Vamos criar um laço de repetição para percorrer a lista dados e mostrar os dados do jogador na tela. Vamos usar a função get() para obter o valor do dicionário titulos ou a chave caso não exista. 

print('-' * 50)
print(f'{"Aproveitamento do jogador":^50}')
print('-' * 50)

for jogador in dados:
    for chave, valor in jogador.items():
        titulo = titulos.get(chave, chave)
        if chave == 'gols_por_partida':
            print('-' * 50)
            for c, v in enumerate(jogador['gols_por_partida'], 1):
                print(f'{f"Partida {c}":<30}{f"{v} gols":>15}')
            print('-' * 50)
        else:
            print(f'{titulo:<30}{valor:>15}')