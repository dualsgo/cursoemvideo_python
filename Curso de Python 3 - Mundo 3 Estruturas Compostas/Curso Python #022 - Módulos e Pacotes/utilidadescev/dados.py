# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

import moeda

def leia_dinheiro(mensagem):
	while True:

		valor_monetario = input(mensagem)
		verificar = valor_monetario.replace(',', '')
		try:
			float(verificar)
			valor_monetario = moeda.formato_monetario(float(valor_monetario.replace(',', '.')))
			return valor_monetario
		except ValueError:
			print('Tipo de valor inválido!')