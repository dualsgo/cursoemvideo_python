# Exercício Python #096 - Função que calcula área - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def valor(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Valor inválido para essa operação!')


largura = valor('Digite a largura do terreno: ')
comprimento = valor('Digite o comprimento do terreno: ')
área_do_terreno = largura * comprimento

print(f'{f'LARGURA (m)':^15}{f'COMPRIMENTO (m)':^15}{f'ÁREA (m²)':^15}')
print(f'{largura:^15}{comprimento:^15}{área_do_terreno:^15}')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o precisamos criar uma função chamada área() que recebe dois parâmetros: largura e comprimento. A função deve retornar a área do terreno, que é calculada multiplicando a largura pelo comprimento.

# Uma função é um bloco de código que executa uma tarefa específica. Para criar uma função em Python, usamos a palavra-chave def seguida do nome da função e dos parênteses. Os parâmetros são passados entre os parênteses. O corpo da função é definido por um bloco de código indentado.
def área(largura, comprimento):
	return largura * comprimento

# def é a palavra-chave usada para definir uma função.
# área é o nome da função.
# largura e comprimento são os parâmetros da função. São os valroes que a função recebe para realizar a tarefa.
# O corpo da função é a expressão largura * comprimento. A função retorna o valor da expressão.

# Para chamar uma função, basta digitar o nome da função seguido dos parâmetros entre parênteses. O valor retornado pela função pode ser armazenado em uma variável.
área_do_terreno = área(5, 10)

# Obs: A função área() é chamada com os argumentos 5 e 10. Esses valores são passados para os parâmetros largura e comprimento da função. Se forncecermos menos ou mais argumentos do que o número de parâmetros, o Python exibirá um erro.

# O valor retornado pela função é armazenado na variável área_do_terreno.
# O valor retornado pela função é calculado multiplicando 5 por 10, que é igual a 50.

print(f'A área do terreno é {área_do_terreno} m²')

# Essa versão é mais simples apenas para introduzir o conceito de funções. No entanto, podemos melhorar, como aqui que temos uma função que pede um valor ao usuário e verifica se o valor é válido. E outra função que calcula a área do terreno. Desse modo, o código fica mais organizado e fácil de entender além de prevenir erros.

def valor(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Valor inválido para essa operação!')


def área():
	largura = valor('Digite a largura do terreno: ')
	comprimento = valor('Digite o comprimento do terreno: ')
	return largura * comprimento

print(f'LARGURA (m){"COMPRIMENTO (m)":>15}{"ÁREA (m²)":>15}')
print(f'{largura:>15}{comprimento:>15}{área():>15}')