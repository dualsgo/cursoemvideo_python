# Exercício Python #054 - Grupo da Maioridade - Aula 00 até 13 - Mundo 2
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from time import sleep  # Importa a função sleep para pausas temporizadas
from random import randint  # Importa a função randint para gerar anos de nascimento aleatórios
from datetime import date  # Importa a classe date para obter o ano atual

ano_atual = date.today().year  # Obtém o ano atual

maiores = menores = 0  # Inicializa os contadores de maiores e menores de idade

for i in range(1, 8):  # Loop para iterar sobre 7 pessoas
    print(f'Pessoa {i}, seu ano de nascimento é: ', end='')
    sleep(1)  # Pausa por 1 segundo
    ano_nascimento = randint(1950, 2023)  # Gera um ano de nascimento aleatório entre 1950 e 2023
    print(ano_nascimento)
    idade = ano_atual - ano_nascimento  # Calcula a idade
    print(f'{idade} anos de idade')
    sleep(1)  # Pausa por 1 segundo
    if idade >= 21:
        print('\033[1;32mMaior de idade\033[m')  # Exibe em verde se for maior de idade
        maiores += 1
    else:
        print('\033[1;31mMenor de idade\033[m')  # Exibe em vermelho se for menor de idade
        menores += 1
    sleep(1)  # Pausa por 1 segundo

print(f'Ao todo temos {menores} menores e {maiores} maiores de idade.')


# Versões extras

from random import randint
from datetime import date
from time import sleep

ano_atual = date.today().year
maiores = menores = 0
while True:
	try:
		ano_inicial = int(input('Digite o início do intervalo: '))
		print(f'{'-'*40}')
		print(f'{'PESSOA':^10}{'ANO NASC':^10}{'IDADE':^10}{'MAIOR?':^10}')
		print(f'{'-'*40}')
		for pessoa in range(1,8):
			sleep(1)
			ano_nascimento = randint(ano_inicial, ano_atual)
			idade = ano_atual - ano_nascimento
			maioridade = 'SIM' if idade >= 18 else 'NÃO'

			if idade >= 18:
				print(f'\033[1;32m{pessoa:^10}{ano_nascimento:^10}{idade:^10}{maioridade:^10}\033[1;32m')
				maiores += 1
			else:
				print(f'\033[1;31m{pessoa:^10}{ano_nascimento:^10}{idade:^10}{maioridade:^10}\033[m')
				menores += 1
		print(f'{'-'*40}')
		print(f'Total de maiores de idade: {maiores}')
		print(f'Total de menores de idade: {menores}')
		print(f'{'-'*40}')

		break
	except ValueError:
		print('ERRO')

	"""from datetime import date
ano_atual = date.today().year
ano_nascimento = [int(input(f'Ano de nascimento da {i}ª pessoa: ')) for i, v in enumerate(range(7), 1)]
maiores = [i for i in ano_nascimento if ano_atual - i > 17]
print(f'Ao todos temos {len(maiores)} maiores de idade e {len(ano_nascimento) - len(maiores)} menores de idade!')"""


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos ler o ano de nascimento de sete pessoas e mostrar quantas são maiores de idade e quantas são menores de idade.
# Para definir a idade precisamos saber o ano atual. Vamos usar a função date() da classe date para obter o ano atual.
from datetime import date # Importa a classe date para obter o ano atual
from time import sleep as pausa # Importa a função sleep para pausas temporizadas e renomeia para pausa

ano_atual = date.today().year  # Obtém o ano atual

# Inicializamos os contadores de maiores e menores de idade com zero.
maiores = menores = 0

# Vamos usar um laço de repetição for para iterar sobre as sete pessoas.
for i in range(1, 8):  # Loop para iterar sobre 7 pessoas
    print(f'Pessoa {i}, seu ano de nascimento é: ', end='')  # Mostra o nome da pessoa e solicita o ano de nascimento
    pausa(1)  # Pausa por 1 segundo
    
    ano_nascimento = int(input())  # Lê o ano de nascimento da pessoa
    idade = ano_atual - ano_nascimento  # Calcula a idade
    
    print(f'Você tem: {idade} anos de idade')  # Mostra a idade da pessoa
    pausa(1)  # Pausa por 1 segundo
    
    # Verifica se a pessoa é maior ou menor de idade e incrementa o contador correspondente.
    if idade >= 18:
        print('\033[1;32mMaior de idade\033[m')
        maiores += 1 
    else:
        print('\033[1;31mMenor de idade\033[m')
        menores += 1
        
pausa(1)  # Pausa por 1 segundo
print(f'Ao todo temos {menores} menores e {maiores} maiores de idade.')  # Mostra o