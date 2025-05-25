# Exercício Python #077 - Contando vogais em Tupla - Aula 00 até 16 - Mundo 3
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Tupla de palavras
palavras = ("abacaxi", "banana", "carro", "dente", "elefante", "futebol", "gato", "hotel", "igreja", "janela", "ketchup", "limonada", "macaco", "navio", "olho", "pizza", "quarto", "roda", "sapato", "tigre")

for palavra in palavras:
	print(f'\nPalavra: {palavra}', end=' - ')
	for vogal in palavra:
		print(vogal if vogal in 'aeiou' else ' ', end='')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, o programa deve mostrar, para cada palavra, quais são as suas vogais.

# Primeiro vamos criar uma tupla com várias palavras.
palavras = ("abacaxi", "banana", "carro", "dente", "elefante", "futebol", "gato", "hotel", "igreja", "janela", "ketchup", "limonada", "macaco", "navio", "olho", "pizza", "quarto", "roda", "sapato", "tigre")

# Vamos percorrer a tupla com um laço for.

# Para cada palavra na tupla, vamos exibir a palavra e as suas vogais.
for palavra in palavras:
	print(f'\nPalavra: {palavra}', end=' - ') # Exibindo a palavra. O \n serve para pular uma linha, para aparecer cada palavra em uma linha diferente.	Precisamos dele pois o end do próximo print está definido como '', fazendo com que as vogais sejam exibidas na mesma linha.
	for vogal in palavra:
		print(vogal if vogal in 'aeiou' else ' ', end='') # Exibindo as vogais. Se a vogal estiver contida na string 'aeiou', exibimos a vogal, senão, exibimos um espaço em branco. O end='' serve para não pular uma linha após exibir a vogal.

# O laço for vai percorrer a tupla palavras. Para cada palavra na tupla, vamos exibir a palavra e as suas vogais. O laço for vai percorrer a palavra e verificar se a vogal está contida na string 'aeiou'. Se estiver, exibimos a vogal, senão, exibimos um espaço em branco. O resultado será algo como: