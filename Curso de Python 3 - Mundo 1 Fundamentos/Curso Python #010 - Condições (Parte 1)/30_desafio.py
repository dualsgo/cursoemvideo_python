# Exercício Python #030 - Par ou Ímpar? - Aula 00 até 09 - Mundo 1
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from random import randint
# Tarefa 1: Sortear um número
numero = randint(0, 99)

# Tarefa 2: Verificar se é par ou ímpar
par = numero % 2 == 0

print(f"O número {numero} é PAR!" if par else f'O número {numero} é ÍMPAR!')

# Versão 2 - Com validação

while True:
	try:
		número = int(input('Digite um valor (diferente de zero): '))
		if not número:
			continue
		print(f'{número} é', '\033[1;31mÍMPAR\033[m' if número % 2 else '\033[1;32mPAR\033[m')
		break
	except ValueError:
		print('Valor de tipo não válido para essa operação.')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler um número inteiro e verificar se ele é par ou ímpar. Para isso, vamos utilizar o operador módulo (%) para calcular o resto da divisão por 2. Se o resto for igual a zero, o número é par, caso contrário, é ímpar.

# A primeira coisa a ser feita é ler o número inteiro digitado pelo usuário. Para isso, vamos utilizar a função input() para ler o número e a função int() para converter o valor para inteiro.	
número = int(input('Digite um número inteiro: '))

# Em seguida, vamos verificar se o número é par ou ímpar. Para isso, vamos calcular o resto da divisão por 2 com o operador módulo (%). Se o resto for igual a zero, o número é par, caso contrário, é ímpar.
par = número % 2 == 0

# Por fim, vamos exibir uma mensagem informando se o número é par ou ímpar. Para isso, vamos utilizar um operador ternário para simplificar o código.
print(f'O número {número} é PAR!' if par else f'O número {número} é ÍMPAR!')
# Nesse código, utilizamos um operador ternário para exibir a mensagem. Se a condição par for verdadeira, exibimos a mensagem "O número {número} é PAR!", caso contrário, exibimos a mensagem "O número {número} é ÍMPAR!".

# Podemos simplificar ainda mais:
print(f'O número é: {"ÍMPAR" if número % 2 else "PAR"}')
# Essa é uma versão compacta, não significa que seja a melhor opção. A melhor opção é aquela que torna o código mais legível e fácil de entender.
# Mas é uma boa oportunidade para treinar. O if espera um valor booleano, True ou False. Zero é considerado False e qualquer outro valor é considerado True. Portanto, se o resto da divisão por 2 for qualquer valor diferente de zero, o número é ímpar, caso contrário, é par. Assim não precisamos fazer a comparação com zero.