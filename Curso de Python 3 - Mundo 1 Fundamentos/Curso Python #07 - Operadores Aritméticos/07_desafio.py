# Exercício Python #007 - Média Aritmética - Aula 00 até 07 - Mundo 1
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

from emoji import emojize


def obtem_nota(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print(emojize(f':xis: Valores inválidos! :xis:', language='pt'))


primeira_nota = obtem_nota(emojize(':memorando: Digite a primeira nota: ', language='pt'))
segunda_nota = obtem_nota(emojize(':memorando: Digite a segunda nota: ', language='pt'))
média = (primeira_nota + segunda_nota) / 2


print(f'{'Primeira nota:':<15}{primeira_nota:>5}\n{'Segunda nota:':<15}{segunda_nota:>5}\n{'Média:':<15}{média:>5}')

print(f'{'\033[1;31mREPROVADO\033[m'}' if média < 5 else f'{'\033[1;33mEM RECUPERAÇÃO\033[m'}' if média < 7 else f'{'\033[1;32mAPROVADO\033[m'}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário duas notas e calcula a média aritmética entre elas. A média aritmética é a soma de todos os valores dividida pela quantidade de valores.

# Assim como antes, utilizamos a função input() para solicitar um valor ao usuário. Como as notas podem ser números reais, utilizamos a função float() para converter o valor digitado em um número de ponto flutuante.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# A média aritmética é calculada somando as duas notas e dividindo o resultado por 2. O resultado é armazenado na variável média.
média = (nota1 + nota2) / 2

# Note que colocamos a soma entre parênteses para garantir que ela seja feita antes da divisão. Isso é necessário porque a divisão tem prioridade sobre a adição na ordem de operações matemáticas.

# Em Python, o operador de divisão é representado pela barra (/)

# Vamos exibir as notas e a média na tela.
print(f'Primeira nota: {nota1}')
print(f'Segunda nota: {nota2}')
print(f'Média: {média}') # A saída será formatada com uma casa decimal, pois a média é um número real.

# Podemos controlar o número de casas decimais exibidas utilizando a função format() ou f-string. Por exemplo, para exibir a média com duas casas decimais, podemos usar a seguinte formatação:
print(f'Média: {média:.2f}')

# A notação :.2f no f-string indica que queremos exibir a variável média com duas casas decimais. O .2f é uma formatação específica para números reais.