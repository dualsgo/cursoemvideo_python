# Exercício Python #052 - Números primos - Aula 00 até 13 - Mundo 2
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

while True:
	try:
		numero = int(input('Digite um valor: '))
		divisor = 0

		for i in range(1, numero+1):
			if numero % i == 0:
				divisor += 1

				print(f'\033[1;32m{i}\033[m ⮕ ', end='')
			else:
				print(f'\033[1;31m{i}\033[m ⮕ ', end='')

		primo = 'é primo!' if divisor <= 2 else 'não é primo!'
		print(f'O valor {numero} {primo}. Ele possui {divisor} divisores.')

	except ValueError:
		print('Você digitou um valor inválido para essa operação!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos ler um número inteiro e verificar se ele é um número primo. Um número primo é um número natural maior que 1 que possui apenas dois divisores: ele mesmo e o número 1.

# Vamos usar a seguinte abordagem: Salvaremos a quantidade de divisores do número em uma variável. Em seguida, vamos usar um laço de repetição for para verificar se o número é divisível por algum número. Se for divisível, incrementamos a variável que armazena a quantidade de divisores. Ao final, verificamos se a quantidade de divisores é igual a 2. Se for, o número é primo, senão, não é primo.

# Solicitamos ao usuário que digite um número inteiro.
numero = int(input('Digite um valor: '))
divisor = 0  # Iniciamos a variável divisor com zero.

# Usamos um laço de repetição for para verificar se o número é divisível por algum número.
for i in range(1, numero + 1):  # Começamos em 1 e terminamos no número digitado. Devemos incluir o número digitado, por isso usamos o número + 1.
    if numero % i == 0:  # Se o número for divisível por i (i representará o divisor atual no intervalo de 1 até o número digitado)
        divisor += 1  # Incrementamos a variável divisor.
        print(f'\033[1;32m{i}\033[m ⮕ ', end='')  # Mostramos o divisor em verde.
    else:
        print(f'\033[1;31m{i}\033[m ⮕ ', end='') # Mostramos o divisor em vermelho.
        
# Verificamos se o número é primo. Se a quantidade de divisores for igual a 2, o número é primo, senão, não é primo.
# Aqui vamos usar uma estrutura condicional para verificar se o número é primo. Se a quantidade de divisores for menor ou igual a 2, o número é primo, senão, não é primo. O retorno da condição é armazenado na variável primo como uma string.
primo = 'é' if divisor <= 2 else 'não é'

print(f'O valor {numero} {primo} primo! Ele possui {divisor} divisores.')  # Mostramos se o número é primo e a quantidade de divisores.