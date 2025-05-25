# Exercício Python #038 - Comparando números - Aula 00 até 12 - Mundo 2
# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

# Tarefa 1: Ler dois números inteiros
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
maior = menor = primeiro

# Tarefa 2: Verificar se há um maior ou se são iguais
if primeiro != segundo:
    if primeiro > segundo:
        print('O primeiro valor é o maior!')
        maior = primeiro
        menor = segundo
    elif primeiro < segundo:
        print('O segundo valor é o maior!')
        maior = segundo
        menor = primeiro
    print(f'O maior é {maior} e o menor é {menor}')
else:
    print('Os números são iguais!')

# Versão 2 - Simplificada

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

print(
	f'{valor1} é maior que {valor2}' if valor1 > valor2 else
	f'{valor1} é menor que {valor2}' if valor1 < valor2 else
	f'{valor1} e {valor2} são iguais.')

# Versão 3 - Com validação  

def obter_valor(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Tipo de dado inválido para essa operação.')


primeiro = obter_valor('Digite o primeiro valor: ')
segundo = obter_valor('Digite o segundo valor: ')
verificação = 'O primeiro valor é o maior!' if primeiro > segundo else 'O segundo valor é o maior' if primeiro < segundo else 'Os valores são iguais!'
print(verificação)

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

#  Nesse exercício, o programa deve ler dois números inteiros e compará-los, mostrando uma mensagem informando qual é o maior ou se os números são iguais.

# A primeira coisa a ser feita é ler dois números inteiros. Para isso, vamos utilizar a função input() para ler os valores e a função int() para converter os valores para inteiros.
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

# Em seguida, vamos verificar se os números são iguais ou se um é maior que o outro. Para isso, vamos utilizar uma estrutura condicional que verifica se os números são iguais, se o primeiro número é maior que o segundo ou se o segundo número é maior que o primeiro.
if valor1 != valor2:
    if valor1 > valor2:
        print(f'{valor1} é maior que {valor2}')
    else:
        print(f'{valor1} é menor que {valor2}')
else:
    print(f'{valor1} e {valor2} são iguais.')
# Temos que comparar todas as possibilidades: Se o primeiro número for diferente do segundo, se o primeiro número for maior que o segundo e se o segundo número for maior que o primeiro. Se os números forem iguais, não é necessário fazer nenhuma comparação.

