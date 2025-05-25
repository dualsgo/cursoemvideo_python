# Exercício Python #031 - Custo da Viagem - Aula 00 até 09 - Mundo 1
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from math import dist
from random import randint
# Tarefa 1: Perguntar a distância de uma viagem em
distancia = randint(100, 500)
print(f'Você está prestes a fazer uma viagem de {distancia}Km')

# Tarefa 2: Calcular o preço da viagem
viagem_curta = distancia <= 200

preco = .5 if viagem_curta else .45
preco_viagem = distancia * preco

print(f'O preço da sua viagem será R$ {preco_viagem:.2f}')

# Versão 2 - Com validação

while True:
	try:
		distancia = float(input('Digite a distância em KM: '))
		print(f'Sua viagem de {distancia}Km irá custar:', f'R$ {distancia * (.5 if distancia < 201 else 0.45):.2f}')
		break
	except ValueError:
		print(f'Apenas valores numéricos')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve perguntar a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

# A primeira coisa a ser feita é perguntar a distância da viagem em Km. Para isso, vamos utilizar a função input() para ler a distância e a função float() para converter o valor para ponto flutuante.
distancia = float(input('Digite a distância da viagem em Km: '))

# Em seguida, vamos calcular o preço da viagem. Se a distância for menor ou igual a 200Km, o preço será R$0,50 por Km. Caso contrário, o preço será R$0,45 por Km.
preco = .5 if distancia <= 200 else .45
# O que fizemos aqui foi simplificar o cálculo do preço da viagem usando uma estrutura condicional que define o valor do preço com base na distância da viagem. Se a distância for menor ou igual a 200Km, o preço será R$0,50 por Km. Caso contrário, o preço será R$0,45 por Km.

# Com a distância e o preço por Km definidos, podemos calcular o preço da viagem multiplicando a distância pelo preço.
preco_viagem = distancia * preco
# Lembre-se, já definimos o preço por Km com base na distância da viagem. Agora, basta multiplicar a distância pelo preço para obter o preço da viagem.

# Agora bastar exibir o preço da viagem na tela.
print(f'A viagem de {distancia}Km custará R$ {preco_viagem:.2f}')

# Fato curioso: Uma viagem de 200Km custará R$ 100,00 e uma viagem de 201Km custará R$ 90,45. Isso porque o preço por Km é diferente para viagens mais longas.	