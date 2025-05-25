# Python Exercício #041 - Classificando Atletas - Aula 00 até 12 - Mundo 2
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
# Tarefa 1: Ler o ano de nascimento
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'Idade: {idade} anos')
# Tarefa 2: Definir as categorias conforme a idade
print('Sua categoria é: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
    
# Versão 2
from datetime import date
atual = date.today().year

while True:
	try:
		idade = atual - int(input('Digite o ano de nascimento: '))
		categoria = 'MIRIM' if idade < 10 else 'INFANTIL' if idade < 14 else 'JÚNIOR' if idade < 19 else 'SÊNIOR' if idade < 25 else 'MASTER'

		if 4 < idade < 81:
			print(f'Idade: {idade} ANOS - Categoria: {categoria}')
			break
		else:
			print(f'Idade fora do intervalo permitido (5 ATÉ 80 ANOS). ')

	except ValueError:
		print('Ano de nascimento inválido: ')


# Versão 3

from datetime import date
from emoji import emojize


def obtem_idade(mensagem):
	while True:
		try:
			ano_nascimento = int(input(mensagem))
			if 1980 <= ano_nascimento <= 2015:
				return ano_nascimento
			else:
				print("O ano deve estar entre 1980 e 2015")
		except ValueError:
			print('Apenas números são aceitos')


ano_atual = date.today().year
idade = ano_atual - obtem_idade('Digite o seu ano de nascimento: ')

categorias = emojize(
	f'MIRIM :bebê:' if idade < 10
	else 'INFANTIL :criança:' if idade < 14
	else 'JÚNIOR :menino:' if idade < 19
	else 'SÊNIOR :pessoa:' if idade < 25
	else 'MASTER :homem_cabelo_branco:', language='pt')

print(f'{'Idade:':<10}{idade:>15}\n{'Categoria:':<10}{categorias:>15}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler o ano de nascimento de um atleta e mostrar a categoria dele conforme a idade. As categorias são:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

# Para isso, vamos utilizar a função input() para ler o ano de nascimento do atleta e a função int() para converter o valor para inteiro.
ano_nascimento = int(input('Digite o ano de nascimento: '))

# Em seguida, vamos calcular a idade do atleta subtraindo o ano de nascimento do atleta do ano atual. Para isso, vamos utilizar a função date.today().year para obter o ano atual.
from datetime import date
ano_atual = date.today().year

# Por fim, vamos verificar a categoria do atleta conforme a idade. Para isso, vamos utilizar uma estrutura condicional que verifica se a idade do atleta é menor ou igual a 9, menor ou igual a 14, menor ou igual a 19, menor ou igual a 25 ou maior que 25. Em cada caso, vamos exibir a categoria correspondente.
print('Sua categoria é: ', end='')

# Podemos usar o operador de comparação <= para verificar se a idade do atleta é menor ou igual a um determinado valor ou o operador de comparação > para verificar se a idade do atleta é maior que um determinado valor.
if idade <= 9:
	print('MIRIM')
# Poderia ser feito com idade < 10,o resultado seria o mesmo.
elif idade <= 14:
	print('INFANTIL')
# Poderia ser feito com idade < 15,o resultado seria o mesmo.
elif idade <= 19:
	print('JÚNIOR')
# Poderia ser feito com idade < 20,o resultado seria o mesmo.
elif idade <= 25:
	print('SÊNIOR')
# Poderia ser feito com idade < 26,o resultado seria o mesmo.
else:
	print('MASTER')

