# Exercício Python #014 - Conversor de Temperaturas - Aula 00 até 07 - Mundo 1
# Escreva um programa que converta uma temperatura digitada em °C para °F

# Fórmula °F = °C x 9  5 + 32
# Fórmula °C = 5 ÷ 9 (°C - 32)

# Tarefa 1: Receber a temperatura em °C
while True:
	try:
		celsius = float(input('Temperatura em Celsius ºC: '))
		fahrenheit = celsius * 1.8 + 32
		print(f'{'Temperatura em Celsius:':<30}ºC{celsius:>10.1f}\n{'Temperatura em Fahrenheit:':<30}ºF{fahrenheit:>10.1f}')
		break
	except ValueError:
		print('Valor inválido!')

# Versão 2

f = c = 0

while True:
	try:
		temperatura = float(input('Digite a temperatura: '))
		c_ou_f = 2
		while 0 != c_ou_f != 1:
			c_ou_f = int(input(
				f'{'-'*30}\n'
				f'[0] Converter de °C para °F\n'
				f'[1] Converter de °F para °C\n'
				f'{'-'*30}'))

		if c_ou_f:
			f = (temperatura - 32) * (5/9)
			print(f'{temperatura}°F corresponde a {f:.1f}°C')
		else:
			c = (temperatura * 1.8) + 32
			print(f'{temperatura}°C corresponde a {c:.1f}°F')
		break

	except ValueError:
		print('Valor inválido. Tente novamente.')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário uma temperatura em graus Celsius e converte para Fahrenheit. 


# A fórmula de conversão de Celsius para Fahrenheit é a seguinte:
# °F = °C * 1.8 + 32

# Nota: Você pode encontrar a fórmula de conversão de Fahrenheit para Celsius sendo exibida de outras formas, mas que são equivalentes.

# °C = 9/5 * (°F - 32)
# Nessa fórmula, subtraímos 32 do valor em Fahrenheit e multiplicamos o resultado por 9/5 (9/5 é o mesmo que 1.8).

# °C = (°F - 32) / 1.8
# Essa fórmula é equivalente à anterior. Subtraímos 32 do valor em Fahrenheit e dividimos o resultado por 1.8 (1.8 é o resultado de 9/5)

# Primeiro, solicitamos a temperatura em graus Celsius ao usuário. Utilizamos a função input() para solicitar o valor e a função float() para converter o valor em um número de ponto flutuante. O valor digitado é armazenado na variável celsius.
temperatura_celsius = float(input('Digite a temperatura em Celsius: '))

# Em seguida, convertemos a temperatura de Celsius para Fahrenheit utilizando uma das fórmulas apresentadas. O resultado é armazenado na variável fahrenheit.
fahrenheit = temperatura_celsius * 1.8 + 32

print(f'{"Temperatura em Celsius:":<30}ºC{temperatura_celsius:>10.1f}')
print(f'{"Temperatura em Fahrenheit:":<30}ºF{fahrenheit:>10.1f}')

# Usamos a notação de dois pontos seguida de um número inteiro e um ponto flutuante para exibir o valor com uma casa decimal após a vírgula. O número inteiro representa o número mínimo de caracteres que a string deve ter. O ponto flutuante representa o número de casas decimais que a string deve ter.

# Nesse caso, utilizamos 30 para garantir que a string tenha pelo menos 30 caracteres. O número 10.1f garante que o valor seja exibido com uma casa decimal após a vírgula e que ocupe 10 caracteres. Os sinais de maior e menor que (< e >) são utilizados para alinhar o texto à esquerda e à direita, respectivamente.

# Note que podemos realizar essa formatação tanto com variáveis quanto com valores diretamente na função print(). No caso, utilizamos variáveis para facilitar a leitura do código.