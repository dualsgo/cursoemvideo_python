# Exercício Python #004 - Dissecando uma Variável - Aula 00 até 07 - Mundo 1
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

from emoji import emojize
from time import sleep

# Versão com loop
while True:
	try:
		número = int(input('Digite o valor que deseja ver a tabuada: '))
		for i in range(1, 11):
			print(emojize(f'{número}:xis:{i:2}:sinal_de_igual:{número * i:2}', language='pt'))
		break
	except ValueError:
		print('O valor digitado não é válido para essa operação!')

# Versão do exercício

# Tarefa 1: Ler um número.
numero = int(input(emojize(':teclado: Digite o valor: ', language='pt')))

# Tarefa 2: Criar a tabuada.
print(emojize(f'Tabuada de :sinal_de_multiplicação: {numero}', language='pt'))
sleep(1)
print(emojize(f'{numero} :sinal_de_multiplicação: {1:2} = {numero * 1:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {2:2} = {numero * 2:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {3:2} = {numero * 3:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {4:2} = {numero * 4:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {5:2} = {numero * 5:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {6:2} = {numero * 6:2}', language='pt'))
sleep(.5)

print(emojize(f'{numero} :sinal_de_multiplicação: {7:2} = {numero * 7:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {8:2} = {numero * 8:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {9:2} = {numero * 9:2}', language='pt'))
sleep(.5)
print(emojize(f'{numero} :sinal_de_multiplicação: {10:2} = {numero * 10:2}', language='pt'))

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário um número inteiro e exibe na tela a tabuada desse número. Como estamos no início do aprendizado não iremos utilizar loops, então vamos exibir a tabuada manualmente.

# Assim como antes, utilizamos a função input() para solicitar um valor ao usuário. O valor digitado é convertido para inteiro e armazenado na variável número.

número = int(input('Digite o valor que deseja ver a tabuada: '))

# A tabuada é uma tabela de multiplicação que mostra o resultado da multiplicação de um número por todos os números inteiros de 1 a 10. Para exibir a tabuada, multiplicamos o número digitado pelo número de 1 a 10 e exibimos o resultado na tela.

# Mostraremos o resultado utilizando dez print()s, um para cada linha da tabuada. Cada print() exibirá o número multiplicado por um dos números de 1 a 10. Não salvaremos os resultados em variáveis.

# Vamos exibir a tabuada na tela.
print(f'Tabuada de {número}')
print(f'{número} x 1 = {número * 1:2}')
print(f'{número} x 2 = {número * 2:2}')
print(f'{número} x 3 = {número * 3:2}')
print(f'{número} x 4 = {número * 4:2}')
print(f'{número} x 5 = {número * 5:2}')
print(f'{número} x 6 = {número * 6:2}')
print(f'{número} x 7 = {número * 7:2}')
print(f'{número} x 8 = {número * 8:2}')
print(f'{número} x 9 = {número * 9:2}')
print(f'{número} x 10 = {número * 10:2}')

# Utilizamos o operador de multiplicação (*) para calcular o resultado da multiplicação. O operador de multiplicação é representado pelo asterisco (*). Como sabemos, uma variável é um nome que se refere a um valor. No caso, a variável número se refere ao valor digitado pelo usuário e por ter sido convertido para inteiro, podemos realizar operações matemáticas com ele.

# Note que utilizamos um :2 após a expressão de multiplicação para garantir que o resultado seja exibido com dois espaços. Isso é feito para alinhar os resultados na tela, facilitando a leitura da tabuada. O :2 é uma formatação específica para números inteiros que reserva dois espaços para a exibição do valor. Se o valor tiver menos de dois dígitos, espaços em branco são adicionados à esquerda para completar o espaço reservado.

