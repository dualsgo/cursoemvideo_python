# Exercício Python #034 - Aumentos múltiplos - Aulas 00 até 09 - Mundo 1
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('Simulador de aumento')
# Tarefa 1: Perguntar o salário de um funcionário
salario_atual = float(input('Digite o seu salário atual: R$ '))

# Tarefa 2: Calcular o valor do aumento
quinze_porcento = salario_atual <= 1250
dez_porcento = salario_atual > 1250

# Se for menor ou igual a 1250, aumenta 15%
if quinze_porcento:
    aumento = 0.15
    print('Seu aumento será de 15%')
# Se for maior que 1250, aumenta 10%
else:
    aumento = 0.10
    print('Seu aumento será de 10%')

novo_salario = salario_atual + (salario_atual * aumento)
print(f'O seu salário de R$ {salario_atual:.2f} com aumento será R$ {novo_salario:.2f}')

# Versão 2 - Com validação

salário = 0
while salário <= 0:
	try:
		salário = float(input('Digite o valor do salário: R$ '))
		aumento = .15 if salário <= 1250 else .10
		print(
			f'{'Salário atual:':<20}R${salário:>8.2f}\n'
			f'{'Aumento:':<20}{aumento:>10.2%}\n'
			f'{'Valor do aumento':<20}R${salário*aumento:>8.2f}\n'
			f'{'-' * 30}\n'
			f'{'Salário atualizado:':<20}R${salário * (1+aumento):>8.2f}')
	except ValueError:
		print(f'Apenas valores numéricos.')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve perguntar o salário de um funcionário e calcular o valor do seu aumento. Para salários superiores a R$1250,00, o aumento é de 10%. Para salários inferiores ou iguais a R$1250,00, o aumento é de 15%.

# A primeira coisa a ser feita é perguntar o salário do funcionário. Para isso, vamos utilizar a função input() para ler o salário e a função float() para converter o valor para ponto flutuante.
salário = float(input('Digite o salário do funcionário: R$ '))

# Em seguida, vamos calcular o valor do aumento. Se o salário for superior a R$1250,00, o aumento será de 10%. Caso contrário, o aumento será de 15%.
aumento = .10 if salário > 1250 else .15
# Novamente simplificamos o cálculo do aumento usando uma estrutura condicional que define o valor do aumento com base no salário do funcionário. Se o salário for superior a R$1250,00, o aumento será de 10%. Caso contrário, o aumento será de 15%.

# Com o valor do aumento definido, podemos calcular o valor do aumento multiplicando o salário pelo aumento.
valor_aumento = salário * aumento
# Agora, basta multiplicar o salário pelo aumento para obter o valor do aumento.

print(f'Seu salário atual é de R$ {salário:.2f}')
print(f'O valor do aumento de {aumento:.0%} será de R$ {valor_aumento:.2f}')
# A formatação :.0% é usada para exibir a porcentagem sem casas decimais. A formatação :.2f é usada para exibir o valor do aumento com duas casas decimais.

# Se quisermos saber qual foi o valor do aumento e o salário atualizado, basta somar o salário ao valor do aumento.
salário_atualizado = salário + valor_aumento
print(f'Seu salário atualizado será de R$ {salário_atualizado:.2f}')