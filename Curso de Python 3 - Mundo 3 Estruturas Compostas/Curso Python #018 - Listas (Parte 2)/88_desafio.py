# Exercício Python #088 - Palpites para a Mega Sena - Aula 00 até 18 - Mundo 3
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos = []  # Lista principal

quantidade_jogos = int(input('Digite a quantidade de jogos que deseja simular: '))

for jogo in range(quantidade_jogos):
    bilhete = []  # Lista com cada bilhete de seis números

    while len(bilhete) < 6:
        n = randint(1, 60)
        if n in bilhete:
            n = randint(1, 60)
        else:
            bilhete.append(n)

        jogos.append(bilhete[:])

    bilhete.sort()
    print(f'Jogo {jogo+1}: {bilhete}')
    sleep(1)
    bilhete.clear()


    # V2

    while True:
        try:
            jogos = int(input('Quantos jogos deseja simular? '))
        except ValueError:
            print(f'Valor inválido.')
            continue
        break

    bilhetes = []
    for _ in range(jogos):
        numeros_unicos = set()
        while len(numeros_unicos) < 6:
            numeros_unicos.add(randint(1, 60))
        bilhete = sorted(list(numeros_unicos))
        bilhetes.append(bilhete)

    for ordem, jogo in enumerate(bilhetes, 1):
        print(f'{f" Jogo {ordem} ":=^23}')
        print(*[f'{valor:^3}' for valor in jogo], sep=' ', end='\n')

# V3

while True:
	try:
		quantidade_de_jogos = int(input('Quantos jogos deseja realizar? '))
		break
	except ValueError:
		print('Essa valor não é válido para essa operação!')

jogos = []

for sorteio in range(quantidade_de_jogos):
	bilhete = []

	while True:
		valor = randint(1, 60)

		if valor not in bilhete:
			bilhete.append(valor)

		if len(bilhete) == 6:
			bilhete.sort()
			jogos.append(bilhete)
			break

for _, bilhetes in enumerate(jogos, 1):
	print(f'{f'{_}º JOGO':^30}')
	print(f'{'-'*30}')
	for valor in bilhetes:
		print(f'{valor:^5}', end='')

	print(f'\n{'-'*30}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Vamos importar a função randint da biblioteca random e a função sleep da biblioteca time. A função randint vai ser utilizada para sortear os números e a função sleep vai ser utilizada para dar um intervalo de tempo entre os sorteios.
from random import randint
from time import sleep

# Vamos começar criando uma lista vazia chamada jogos. Essa lista vai armazenar todos os jogos gerados.
jogos = []

# Vamos solicitar ao usuário a quantidade de jogos que ele deseja simular. O valor digitado será convertido para inteiro e armazenado na variável quantidade_jogos.
quantidade_jogos = int(input('Digite a quantidade de jogos que deseja simular: '))
# Em seguida, vamos criar um laço de repetição para gerar os jogos. Para cada jogo, vamos criar uma lista vazia chamada bilhete.
for jogo in range(quantidade_jogos):
    bilhete = []  # Lista com cada bilhete de seis números. Iniciamos ela vazia para cada jogo.

    # Em seguida, vamos criar um laço de repetição para sortear os seis números do bilhete. Vamos sortear um número entre 1 e 60 e verificar se ele já está na lista bilhete. Se não estiver, vamos adicionar na lista. Se estiver, vamos sortear outro número.
    while len(bilhete) < 6:
        n = randint(1, 60)
        if n in bilhete:
            n = randint(1, 60)
        else:
            bilhete.append(n)

        jogos.append(bilhete[:]) # Adicionando o bilhete na lista jogos. É uma cópia para evitar que a lista seja alterada.

    # Por fim, vamos ordenar a lista bilhete e exibir na tela o jogo gerado.
    bilhete.sort()
    print(f'Jogo {jogo+1}: {bilhete}')
    sleep(1)

# Versão avançada - Vamos validar a entrada do usuário e utilizar um laço de repetição para garantir que o usuário digite um valor válido.

from random import randint # Importando a função randint da biblioteca random

# Vamos solicitar ao usuário quantos jogos ele deseja simular. O valor digitado será convertido para inteiro e armazenado na variável jogos.
while True:
    # Vamos utilizar um laço de repetição para garantir que o usuário digite um valor válido.
    
    # try: Vamos tentar converter o valor digitado para inteiro. Se o valor digitado não for um número inteiro, uma exceção ValueError será lançada.
    try:
        jogos = int(input('Quantos jogos deseja simular? ')) # Solicitando a quantidade de jogos ao usuário
        
    # except ValueError: Se uma exceção ValueError for lançada, vamos exibir uma mensagem de erro e continuar o laço.
    except ValueError:
        print(f'Valor inválido.')
        continue

    # break: Se o valor digitado for um número inteiro, vamos sair do laço.
    break

# Após a validação, vamos criar uma lista chamada bilhetes para armazenar os jogos gerados.
bilhetes = []

# Vamos criar um laço de repetição para gerar os jogos. Para cada jogo, vamos criar um conjunto chamado numeros_unicos para garantir que os números sorteados sejam únicos.
for _ in range(jogos):
    numeros_unicos = set() # Conjunto para garantir números únicos
    
    # Vamos criar um laço de repetição para sortear os seis números do bilhete. Vamos sortear um número entre 1 e 60 e adicionar no conjunto numeros_unicos. O laço vai continuar até o conjunto ter seis números únicos.
    while len(numeros_unicos) < 6:
        numeros_unicos.add(randint(1, 60))
        
    # Por fim, vamos ordenar os números sorteados, converter o conjunto para uma lista e adicionar na lista bilhetes.
    bilhete = sorted(list(numeros_unicos))
    bilhetes.append(bilhete)

# Por fim, vamos exibir os jogos gerados na tela.
for ordem, jogo in enumerate(bilhetes, 1):
    print(f'{f" Jogo {ordem} ":=^23}')
    print(*[f'{valor:^3}' for valor in jogo], sep=' ', end='\n')
    

# NOTA: Conjuntos (set()) são uma coleção de elementos únicos e não ordenados. Essa estrutura de dados não é abordada neste curso mas vale a pena pesquisar sobre ela.

# Tratamento de exceções são abordados mais adiante no curso. Se você não entendeu, não se preocupe. O importante é entender a lógica do código.