# Exercício Python #015 - Aluguel de Carros - Aula 00 até 07 - Mundo 1
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

from emoji import emojize


def obter_valores(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print(emojize(':xis: Tente novamente. :xis:', language='pt'))


def total_a_pagar(km, dias):
	valor_por_km = .15
	valor_diária = 60

	total_km = km * valor_por_km
	total_diária = dias * valor_diária

	total = total_km + total_diária

	print(
		f'{"Km percorrido:":<20}{km:>10.1f}\n'
		f'{"Valor (Km):":<20}\033[1;32mR${total_km:>8.2f}\033[m\n{"-" * 30}\n'
		f'{"Dias alugado:":<20}{int(dias):>10}\n'
		f'{"Valor (Dias)":<20}\033[1;32mR${total_diária:>8.2f}\033[m\n{"-" * 30}\n'
		f'{"Total a pagar":<20}\033[1;31mR${total:>8.2f}\033[m')


km_percorrido = obter_valores(emojize(':carro: Quantidade de KM percorridos: ', language='pt'))
dias_alugado = obter_valores(emojize(':calendário: Quantidade de DIAS alugados: ', language='pt'))
total_a_pagar(km_percorrido, dias_alugado)


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. O programa calcula o preço a pagar, considerando que o carro custa R$ 60,00 por dia e R$ 0,15 por quilômetro rodado.

# Como o exercício envolve várias operações, é recomendado fazer por partes. Primeiro, solicite a quantidade de quilômetros percorridos e a quantidade de dias alugados ao usuário. Utilize a função input() para solicitar os valores e a função float() para converter os valores em números de ponto flutuante e int() para converter em números inteiros.

quilometros_percorridos = float(input('Quantos quilômetros foram percorridos? ')) # Para quilometros usamos float pois pode ser um número decimal
dias_alugado = int(input('Por quantos dias o carro foi alugado? ')) # Para dias usamos int pois não faz sentido alugar um carro por um número decimal de dias

# Depois, calcule o valor a pagar por quilômetro rodado e o valor a pagar por dia alugado. O valor a pagar por quilômetro rodado é a quantidade de quilômetros percorridos multiplicada por R$ 0,15. O valor a pagar por dia alugado é a quantidade de dias alugados multiplicada por R$ 60,00.

# NOTA: Podemos salvar esses valores em variáveis para facilitar a leitura do código e eventualmente reutilizá-los em outras partes do programa, ou atualizá-los facilmente se necessário.

valor_por_km = 0.15
valor_diária = 60

# Calculando o valor total por quilômetro rodado e por dia alugado
total_km = quilometros_percorridos * valor_por_km
total_diária = dias_alugado * valor_diária

# Por fim, some os valores obtidos para calcular o total a pagar. O total a pagar é a soma do valor total por quilômetro rodado e do valor total por dia alugado.

total = total_km + total_diária

# Exiba o total a pagar na tela. Você pode formatar a saída para exibir os valores de forma mais clara e legível.

print(f'{"Km percorrido:":<20}{quilometros_percorridos:>10.1f}\n'
	f'{"Valor (Km):":<20}R${total_km:>8.2f}\n{"-" * 30}\n'
	f'{"Dias alugado:":<20}{dias_alugado:>10}\n'
	f'{"Valor (Dias)":<20}R${total_diária:>8.2f}\n{"-" * 30}\n'
	f'{"Total a pagar":<20}R${total:>8.2f}')

# Utilizamos uma exibição diferente do print() para mostrar os valores. Isso é opcional e pode ser feito de acordo com a preferência do programador. Nessa versão utilizamos o operador de escape \n para pular linhas. O resultado é o mesmo, mas a formatação é diferente.

# Podemos codificar cada frase em uma instrução print() separada se acharmos mais fácil de entender. A formatação do texto é uma questão de estilo e preferência pessoal.

# Sobre o operador de escape \n: ele é utilizado para pular uma linha na exibição do texto. Isso é útil para organizar a saída do programa e torná-la mais legível. O \n é um caractere especial que indica ao interpretador Python que ele deve pular para a próxima linha ao exibir o texto. A função print() possui um argumento opcional chamado end que permite alterar o caractere de final de linha padrão. Por padrão, o caractere de final de linha é \n, é e por isso que cada chamada de print() imprime em uma nova linha. Se quisermos alterar o caractere de final de linha, podemos fazer o seguinte:

# print('Olá', end=' ')
# print('mundo!')

# Nesse caso, a saída será Olá mundo! sem pular para a próxima linha. O end=' ' substitui o caractere de final de linha padrão \n por um espaço em branco. Isso é útil para concatenar strings em uma única linha ou para controlar a formatação da saída.