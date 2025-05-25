# Exercício Python #008 - Conversor de Medidas - Aula 00 até 07 - Mundo 1
# Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.

def conversões(m):
	print(
		f'\033[1m{'Kilômetros:':<15}{m / 1000:>12}{'km':<3}\n'
		f'{'Hectometros:':<15}{m / 100:>11}{'hm':<3}\n'
		f'{'Decâmetros:':<15}{m / 10:>10}{'dam':<3}\n'
		f'{'Metros:':<15}{m:>10}{'m':<3}\n'
		f'{'Decímetros:':<15}{m * 10:>10}{'dm':<3}\n'
		f'{'Centímetros:':<15}{m * 100:>10}{'cm':<3}\n'
		f'{'Milímetros:':<15}{m * 1000:>10}{'mm':<3}\033[m')


while True:
	try:
		metros = float(input('Digite o valor da medida em metros: '))
		conversões(metros)
		break
	except ValueError:
		print('O valor informado não é válido para essa operação!')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário um valor em metros e exibe na tela o equivalente em centímetros e milímetros. Para isso, são utilizadas as operações de multiplicação e divisão. Vamos exibir também a conversão para outras unidades de medida de comprimento.

# Assim como antes, utilizamos a função input() para solicitar um valor ao usuário. O valor digitado é convertido para ponto flutuante e armazenado na variável metros. Usaremos float() para permitir que o usuário informe valores decimais como 1.5, por exemplo.
metros = float(input('Digite o valor da medida em metros: '))

# A conversão de metros para centímetros e milímetros é feita multiplicando o valor em metros por 100 e 1000, respectivamente. A conversão para outras unidades de medida de comprimento segue a mesma lógica, multiplicando ou dividindo o valor em metros pela quantidade de metros correspondente a cada unidade. Podemos fazer a conversão diretamente na função print() ou armazenar os resultados em variáveis para exibição posterior.

# Vamos exibir as conversões na tela.
print(f'Kilômetros: {metros / 1000} km')
print(f'Hectômetros: {metros / 100} hm')
print(f'Decâmetros: {metros / 10} dam')
print(f'Metros: {metros} m')
print(f'Decímetros: {metros * 10} dm')
print(f'Centímetros: {metros * 100} cm')
print(f'Milímetros: {metros * 1000} mm')

# A explicação matemática é a seguinte:
# Ao dividir um valor por multiplos de 10, estamos deslocando a vírgula para a esquerda. Por exemplo, ao dividir por 10, estamos transformando metros em decâmetros. Ao dividir por 100, estamos transformando metros em hectômetros. Ao dividir por 1000, estamos transformando metros em quilômetros.
# A lógica inversa se aplica ao multiplicar por multiplos de 10. Ao multiplicar por 10, estamos deslocando a vírgula para a direita, transformando metros em decímetros. Ao multiplicar por 100, estamos transformando metros em centímetros. Ao multiplicar por 1000, estamos transformando metros em milímetros.

