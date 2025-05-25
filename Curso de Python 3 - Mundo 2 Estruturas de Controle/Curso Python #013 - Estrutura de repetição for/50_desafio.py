# Exercício Python #050 - Soma dos pares - Aula 00 até 13
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

acumulador = contador = 0
for número in range(1, 7):
	while True:
		try:
			valor = int(input(f'Digite o {número}º valor: '))
			if valor % 2:
				print('\033[1;31mValor ímpar desconsiderado\033[m')
			else:
				print('\033[1;32mValor par considerado\033[m')
				acumulador += valor
				contador += 1
			break
		except ValueError:
			print('Você digitou um valor de tipo inválido!')
print(f'Entre os 6 números, consideramos {contador} e a soma entre eles é igual a {acumulador}.')

# Com lista
nmbrs = [int(input('Digite um número: ')) for i in range(6)]
soma = [i for i in nmbrs if i % 2 == 0]
print(f'A soma entre os {len(soma)} números pares digitados é {sum(soma)}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos ler seis números inteiros e mostrar a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsideramos.

# Vamos usar um laço de repetição for para ler os seis números. A cada iteração, vamos solicitar ao usuário que digite um número. Em seguida, vamos verificar se o número é par. Se for par, vamos somar ao acumulador e incrementar o contador. Se for ímpar, vamos mostrar uma mensagem informando que o valor foi desconsiderado.

# Combinaremos o laço de repetição for com a estrutura de decisão if/else para verificar se o número é par.

acumulador = contador = 0  # Iniciamos o acumulador e o contador com zero.
for número in range(1, 7):  # Vamos ler seis números.
    valor = int(input(f'Digite o {número}º valor: '))  # Solicitamos ao usuário que digite um valor. Número é a variável de controle do laço de repetição que indica a iteração atual.
    
    if valor % 2 == 0:  # Se o número for par
        print('Valor par considerado')  # Mostramos uma mensagem informando que o valor foi considerado.	
        acumulador += valor  # Somamos o valor ao acumulador.
        contador += 1
    else:  # Se o número for ímpar
        print('Valor ímpar desconsiderado')
        
print(f'Entre os 6 números, consideramos {contador} e a soma entre eles é igual a {acumulador}.')  # Mostramos a quantidade de números considerados e a soma entre eles.