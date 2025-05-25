# Exercício Python #006 - Dobro, Triplo, Raiz Quadrada - Aula 00 até 07 - Mundo 1
# Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from emoji import emojize

def opção():
	while True:
		global escolha
		escolha = int(input(emojize(':memorando: Sua escolha: ', language='pt')))
		if escolha == 1:
			dobro = número * 2
			return dobro
		elif escolha == 2:
			triplo = número * 3
			return triplo
		elif escolha == 3:
			raiz = número ** .5
			return raiz
		else:
			print(emojize(':xis: Opção inválida! :xis:', language='pt'))
			continue

while True:
	try:
		número = int(input(emojize(':memorando: Digite um valor: ', language='pt')))
		print(emojize(f'Escolha uma opção:\n[1] Dobro\n[2] Triplo\n[3] Raiz Quadrada', language='pt'))
		resultado = opção()
		break
	except ValueError:
		print(emojize(':xis: Valor inválido! :xis:', language='pt'))
print(f'Você escolheu: {'Dobro' if escolha == 1 else 'Triplo' if escolha == 2 else 'Raiz quadrada'}')
print(f'{'Número:':<12}{número:>5}\n{'Resultado:':<12}{resultado:>5}')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nessse exercício, o programa solicita ao usuário um número inteiro e exibe na tela o dobro, triplo e raiz quadrada desse número. Para isso, são utilizados os operadores de multiplicação e exponenciação.

# Assim como antes, utilizamos a função input() para solicitar um valor ao usuário. O valor digitado é convertido para inteiro e armazenado na variável número. Em seguida, exibimos na tela as opções disponíveis: dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))

# Agora, numero é um inteiro e podemos realizar operações matemáticas com ele.
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

# Como dito no vídeo, 1/2 é igual a meio, que também pode ser escrito como .5 (ou 0.5 - omitimos o zero à esquerda).
# Ao usar 1/2 na expressão, precisamos colocar o resultado entre parênteses para garantir a precedência da operação. Já que a exponenciação tem prioridade sobre a divisão, o Python primeiro calcula 1/2 e depois eleva o número a esse resultado.
# Sem os parênteses, a expressão seria interpretada como numero ** 1 dividido por 2, o que não é o que queremos.

# Explicando a matemática:

# Por definição, a raiz quadrada de um número é o valor que, multiplicado por si mesmo, resulta no número original. Ou seja, se x é a raiz quadrada de y, então x * x = y.
# A raiz quadrada na mateḿatica é a operação inversa da exponenciação. Ou seja, se 2 ** 2 = 4, então a raiz quadrada de 4 é 2.
# O recíproco de 2 é 1/2. (2 pode ser escrito como 2/1, então o recíproco é 1/2).
# Portanto, é por isso que a raiz quadrada de um número é o mesmo que elevar o número a 1/2.

# Porém o Python oferece uma função embutida para calcular a raiz quadrada de um número, a função sqrt() do módulo math. Para utilizá-la, precisamos importar o módulo math e chamar a função sqrt() passando o número como argumento.
# A exponenciação também pode ser feita com a função pow(), que recebe dois argumentos: a base e o expoente. Por exemplo, pow(2, 3) é equivalente a 2 ** 3.

# Essas funções são úteis quando precisamos calcular raízes ou potências de números, especialmente quando o expoente não é um número inteiro.

# Para exibir os resultados na tela, utilizamos a função print() com uma string formatada. Os valores do número, dobro, triplo e raiz quadrada são exibidos alinhados e formatados para facilitar a leitura.

print(f'O dobro de {numero} é {dobro}.')
print(f'O triplo de {numero} é {triplo}.')
print(f'A raiz quadrada de {numero} é {raiz:.2f}.')

# A formatação :.2f no f-string garante que o número seja exibido com duas casas decimais. Isso é útil para números reais, como a raiz quadrada, que podem ter muitas casas decimais.
# Outra opção seria usar a função round() para arredondar o número para duas casas decimais. Por exemplo, round(raiz, 2) arredondaria a raiz para duas casas decimais.