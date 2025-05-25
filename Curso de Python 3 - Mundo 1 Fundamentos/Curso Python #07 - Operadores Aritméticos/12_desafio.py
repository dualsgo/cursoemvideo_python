# Exercício Python #012 - Calculando Descontos - Aula 00 até 07 - Mundo 1
# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

from emoji import emojize
while True:
	try:
		preço = float(input(emojize('Digite o valor do produto: :cifrão: ', language='pt')))
		com_desconto = preço * .95
		print(f'{'Valor do produto:':<20} R${preço:>10.2f}\n{'Com desconto (5%):':<20} R${com_desconto:>10.2f}')
		break
	except ValueError:
		print('Inválido! Tente novamente.')
  
# Versão 2

while True:
	try:
		preco = float(input('Digite o valor do produto: R$ '))
		descontar = float(input('Porcentagem de desconto: % '))
		print(f'{'-'*31}')
		print(f'{'Valor original':<15}{'R$':>6}{preco:>10.2f}')
		print(f'{'Desconto':<10}{descontar/100:^8.1%}{'R$':>3}{preco * (descontar/100):>10.2f}')
		print(f'{'-'*31}')
		print(f'{'Valor final':<15}{'R$':>6}{preco * ((100 - descontar)/100):>10.2f}')
		print(f'{'-'*31}')

		break

	except ValueError:
		print('O valor informado não é válido!')
	except ZeroDivisionError:
		print(f'Divisão por zero não é possível!')



# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário o preço de um produto e exibe na tela o preço com 5% de desconto. Para isso, utilizamos a operação de multiplicação.

# Assim como antes, utilizamos a função input() para solicitar um valor ao usuário. O valor digitado é convertido para ponto flutuante e armazenado na variável preço.
preço = float(input('Digite o valor do produto: R$ '))

# O desconto de 5% pode ser calculado multiplicando o preço do produto por 0.95 ou subtraindo 5% do preço original. O resultado é armazenado na variável com_desconto.

# Nessa representação, consideramos que o preço representa 100% do valor original. Se queremos saber qual será o preço com 5% de desconto precisamos subtrair 5% do preço original, ou seja, 100 - 5 = 95%. Portanto, o preço com desconto é 95% do preço original.

# 95/100 = 0.95
com_desconto = preço * .95 # 95% do preço

# Se quiser saber qual é o valor equivalente a 5% do preço original, seguindo a mesma lógica, basta multiplicar o preço por 0.05. O desconto é o valor do produto menos o valor do desconto.
cinco_porcento = preço * .05 # 5% do preço

# Nesse método, colocamos entre parênteses a expressão que representa a porcentagem de desconto. Isso garante que a divisão seja feita antes da multiplicação. Se não colocarmos os parênteses, a expressão será interpretada como preço * 5 / 100, o que não é o que queremos.
com_desconto = preço * (95 / 100) # 95% do preço
cinco_porcento = preço * (5 / 100) # 5% do preço

# Utilize a fórmula que achar mais fácil de entender e de lembrar. O importante é que o resultado seja o mesmo.

# Para exibir o preço original e o preço com desconto na tela, utilizamos a função print(). O valor do produto é exibido com duas casas decimais após a vírgula.

# Vamos exibir os valores na tela.
print(f'Valor do produto: R${preço:.2f}')
print(f'Com desconto (5%): R${com_desconto:.2f}')
print(f'Valor do desconto: R${cinco_porcento:.2f}')