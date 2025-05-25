# Exercício Python #061 - Progressão Aritmética v2.0 - Aula 00 até 14 - Mundo 2
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

while True:
	try:
		primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritimética: '))
		razão = int(input('Digite a razão da progressão: '))
		contador = 0
		termo = primeiro_termo
		while contador < 10:
			print(f'{termo} ⮕ ' if contador < 9 else f'{termo} ⮕ FIM!', end='')
			contador += 1
			termo += razão
		break
	except ValueError:
		print('Tipo de dado inválido!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos refazer o DESAFIO 051, lendo o primeiro termo e a razão de uma Progressão Aritmética (PA) e mostrando os 10 primeiros termos da progressão usando a estrutura de repetição while.

# Como antes, primeiro vamos solicitar ao usuário que digite o primeiro termo e a razão da PA. Em seguida, vamos usar um laço de repetição while para mostrar os 10 primeiros termos da PA.
primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritimética: '))  # Solicitamos ao usuário que digite o primeiro termo da PA.
razão = int(input('Digite a razão da prograssão: '))  # Solicitamos ao usuário que digite a razão da PA.

# Inicializamos um contador para controlar o número de termos mostrados e uma variável para armazenar o valor do termo atual.
contador = 0  # Inicializa o contador de termos mostrados
termo = primeiro_termo  # Inicializa o termo atual com o primeiro termo da PA

# Usamos um laço de repetição while para mostrar os 10 primeiros termos da PA.
while contador < 10:  # Enquanto o contador for menor que 10, o laço de repetição continuará.
    print(f'{termo} ⮕ ' if contador < 9 else f'{termo} ⮕ FIM!', end='')  # Exibe o termo atual e a seta se o contador for menor que 9, senão, exibe o termo atual e a seta com a palavra FIM.
    
    contador += 1  # Incrementa o contador para controlar o número de termos mostrados
    termo += razão  # Atualiza o valor do termo atual somando a razão da PA