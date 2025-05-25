# Exercício Python #005 - Antecessor e Sucessor - Aula 00 até 07 - Mundo 1
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

from emoji import emojize

while True:
	try:
		número = int(input(emojize(':memorando: Digite um valor: ', language='pt')))
		sucessor = número + 1
		antecessor = número - 1
		print(emojize(f':seta_para_a_esquerda:\033[1;31m{antecessor:^5}\033[m:seta_para_a_esquerda:\033[1;33m{número:^5}\033[m:seta_para_a_direita:\033[1;32m{sucessor:^5}\033[m:seta_para_a_direita:', language='pt'))
		break
	except ValueError:
		print(emojize(':xis: Apenas números inteiros! :xis:', language='pt'))

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício a propósta é mostrar o funcionamento de operadores aritméticos. O programa solicita ao usuário um número inteiro e exibe na tela o seu antecessor e sucessor. Para isso, são utilizados os operadores de adição e subtração.

# Usaremos como sempre a função input() para solicitar um valor ao usuário. O valor digitado será convertido para inteiro e armazenado na variável número. Em seguida, criamos duas variáveis, sucessor e antecessor, que armazenam o valor do número mais um e menos um, respectivamente.

# É recomendável salvar os valores das operações em variáveis para facilitar a leitura do código e a manutenção futura. Por fim, exibimos na tela os valores do antecessor, número e sucessor, utilizando a formatação de strings para centralizar os valores e colorir os números.

# O Professor utiliza nomes de variáveis abreviados, como n, s e a, para economizar espaço e facilitar a digitação. No entanto, é recomendável utilizar nomes mais descritivos para facilitar a leitura e compreensão do código.

# Lembrando que precisamos  converter o valor digitado para inteiro, pois a função input() sempre retorna uma string. Caso contrário, o programa não conseguirá realizar as operações matemáticas.

numero = int(input('Digite um número: '))

# Agora, numero é um inteiro e podemos realizar operações matemáticas com ele.
antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.')

# A operação pode ser feita diretamente na função print() sem a necessidade de armazenar os valores em variáveis. Nesse caso, a leitura do código pode ficar um pouco confusa, mas o resultado é o mesmo.

print(f'O antecessor de {numero} é {numero - 1} e o sucessor é {numero + 1}.')