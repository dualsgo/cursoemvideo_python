# Exercício Python #051 - Progressão Aritmética - Aula 00 até 13 - Mundo 2
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

while True:
	try:
		primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritimética: '))
		razão = int(input('Digite a razão da prograssão: '))
		décimo_termo = razão*10
		for i, v in enumerate(range(primeiro_termo, décimo_termo+1, razão), 1):
			print(f'{i} ⮕ ' if v < 10 else f'{i} ⮕ FIM!', end='')
		break
	except ValueError:
		print('Tipo de dado inválido!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos ler o primeiro termo e a razão de uma Progressão Aritmética (PA) e mostrar os 10 primeiros termos dessa progressão.
# Uma PA é uma sequência numérica em que cada termo, a partir do segundo, é igual à soma do termo anterior com uma constante, chamada de razão. A fórmula geral de uma PA é an = a1 + (n - 1) * r, onde an é o termo geral, a1 é o primeiro termo, n é a posição do termo na sequência e r é a razão.

# Vamos usar um laço de repetição for para mostrar os 10 primeiros termos da PA. A cada iteração, vamos mostrar o termo da PA. Para isso, vamos usar a função enumerate() para obter o índice e o valor do termo. O índice será a posição do termo na sequência e o valor será o termo da PA.	

primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritimética: '))  # Solicitamos ao usuário que digite o primeiro termo da PA.
razão = int(input('Digite a razão da prograssão: '))  # Solicitamos ao usuário que digite a razão da PA.

# Calculamos o décimo termo da PA, que é o primeiro termo mais a razão multiplicada por 10.
décimo_termo = primeiro_termo + razão * 10

# Usamos um laço de repetição for para mostrar os 10 primeiros termos da PA.
for posição, termo in enumerate(range(primeiro_termo, décimo_termo, razão), 1):  # Começa no primeiro termo, termina no décimo termo e incrementa de acordo com a razão, com o índice começando em 1.
    # posição é o índice do termo na sequência e termo é o valor do termo.
    print(f'{termo} ⮕ ' if posição < 10 else f'{termo} ⮕ FIM!', end='')  # Se o termo for menor que o décimo, mostramos o índice e a seta, senão, mostramos o índice e a seta com a palavra FIM.
    
    # Usamos uma estrutura condicional dentro do print() para decidir se mostramos a seta ou a palavra FIM. Se o termo for menor que 10, mostramos o índice e a seta, senão, mostramos o índice e a seta com a palavra FIM.
    # a sintaxe é bloco_true if condição else bloco_false. Se a condição for verdadeira, o bloco_true é executado, senão, o bloco_false é executado.