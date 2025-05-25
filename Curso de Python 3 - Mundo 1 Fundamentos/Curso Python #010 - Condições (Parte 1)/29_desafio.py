# Exercício Python #029 - Radar eletrônico - Aula 00 até 09 - Mundo 1
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from math import e
from random import randint
from time import sleep
from emoji import emojize
# Tarefa 1: Ler a velocidade do carro.
velocidade = randint(40, 110)
print(f'RADAR: Sua velocidade é de {velocidade}Km/h')

velocidade_maxima = 80

# Tarefa 2: Definir o valor da multa
if velocidade > velocidade_maxima:
    print('Você foi multado!')

    acima_do_limte = velocidade - velocidade_maxima
    multa = acima_do_limte * 7

# Tarefa 3: Mostrar a mensagem dizendo se foi multado ou não
    print(f'O limite de velocidade é de 80Km/h. Você foi flagrado a {velocidade}Km/h.')
    print(f'O valor da multa é de R$ 7,00 por Km/h ultrapassado. Sua multa será de R$ {multa:.2f} por trafegar a {acima_do_limte}Km/h além do permitido.')
else:
    print('Você está dentro do limite permitido!')

# EXTRA

print(emojize(':estrada: RADAR ELETÔNICO', language='pt'))
while True:
	try:
		simulações = int(input('Quantas simulações deseja realizar? '))
		break
	except ValueError:
		print('Valor inválido!')

for carro in range(1, simulações+1):
	velocidade = randint(70, 90)

	multado = velocidade - 80 <= 0

	valor = 7 * (velocidade - 80)
	moeda = str(f'{valor:.2f}').replace('.',',')

	print(emojize(f'{f':carro: Veículo {carro} - Velocidade registrada:':<30}{f'{velocidade}Km/h':>20}', language='pt'))

	print(emojize(f'\033[1;32mTenha um bom dia. Dirija com segurança.\033[m' if multado else f'\033[1;31m:sirene: Você foi multado em R$ {moeda} por ultrapassar em {valor/7}Km a velocidade permitida.\033[m', language='pt'))

	sleep(1)
print('Simulações encerradas!')

# Criar sistema de radar eletrônico que verifique a velocidade e aplique multas R$ 7,00 a cada Km excedido e pontos na carteira - Verificar niveis de gravidade da multa

# Infração leve - 3 Pontos - Multa - R$ 5,00 por KM excedido - 10km acima
# Infração moderada - 4 Pontos - Multa - R$ 10,00 por KM excedido - 20km acima
# Infração grave - 6 Pontos - Multa - R$ 15,00 por KM excedido - 30km acima
# Infração gravíssima - 7 Pontos - Multa - R$ 20,00 por KM excedido - 30km+ acima

from random import randint

def verifica(v):
	excedido = v - 80  # Calcula as multas
	acima_limite = (v - 80) > 0  # Verifica se está acima do limite
	multa = (
		excedido * 5 if excedido <= 10 else
		10 if excedido <= 20 else
		15 if excedido <= 30 else 20)  # Define o multiplicador dependendo do grau
	grau = (
		'\033[32mLeve\033[m' if excedido <= 10 else
		'\033[34mModerada\033[m' if excedido <= 20 else
		'\033[33mGrave\033[m' if excedido <= 30 else '\033[31mGravíssima\033[m')
	pontos = (
		3 if excedido <= 10 else
		4 if excedido <= 20 else
		6 if excedido <= 30 else 7)  # Define o multiplicador dependendo do grau

	if acima_limite:

		print(
			f'{'-' * 26}\n'
			f'{'Velocidade:':<11}{v:>13}{'km':<2}\n'
			f'{'Infração:':<11}{grau:>23}\n'
			f'{'Excedido:':<11}{excedido:>13}{'km':>2}\n'
			f'{'Pontos:':<11}{pontos:>15}\n'
			f'{'Multa:':<11}{'R$':>5}{multa:>10.2f}\n'
			f'{'-' * 26}')


for veículos in range(6):
	velocidade = randint(60, 200)  # Define as velocidades
	verifica(velocidade)

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler a velocidade de um carro e se ele ultrapassar 80Km/h, deve mostrar uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# A primeira coisa a ser feita é capturar a velocidade do carro. Para isso, vamos utilizar a função input() para ler a velocidade digitada pelo usuário. Precisamos converter o valor para inteiro com a função int().
velocidade = int(input('Qual é a velocidade atual do carro? '))

# Em seguida, vamos definir o limite de velocidade, que é de 80Km/h.
velocidade_maxima = 80

# Agora, vamos verificar se a velocidade do carro ultrapassou o limite permitido. Vamos salvar a diferença entre a velocidade do carro e o limite em uma variável chamada acima_do_limite pois precisaremos dela para calcular o valor da multa.
acima_do_limte = velocidade - velocidade_maxima

# Se a velocidade do carro for maior que o limite permitido, o carro foi multado. Nesse caso, vamos exibir uma mensagem informando que o carro foi multado e calcular o valor da multa. Para que a multa seja aplicada, acima_do_limite deve ser maior que zero.

# Para calcular o valor da multa, vamos multiplicar a diferença entre a velocidade do carro e o limite pelo valor da multa por Km excedido, que é de R$7,00.
if acima_do_limte > 0:
	print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
	multa = acima_do_limte * 7
	print(f'Você deve pagar uma multa de R${multa:.2f}!')
# Na exibição do valor da multa, utilizamos o f-string para formatar o valor com duas casas decimais.
else:
	print('Tenha um bom dia! Dirija com segurança!')

# Nesse método salvamos as informações em variáveis para facilitar a leitura e a compreensão do código. No entanto, é possível fazer a verificação diretamente na estrutura condicional, sem a necessidade de salvar a diferença entre a velocidade do carro e o limite em uma variável.

velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
	multa = (velocidade - 80) * 7
	print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${multa:.2f}!')
else:
	print('Tenha um bom dia! Dirija com segurança!')
