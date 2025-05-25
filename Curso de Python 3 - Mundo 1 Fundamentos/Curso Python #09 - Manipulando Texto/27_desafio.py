# Exercício Python #027 - Primeiro e último nome de uma pessoa - Aulas 00 até 09 - Mundo 1
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Tarefa 1: Ler o nome completo pelo teclado
nome = str(input('Digite o seu nome completo: ')).strip().upper()

# Tarefa 2: Mostrar o primeiro e o último nome separadamente
nome_separado = nome.split()

# Primeiro nome
primeiro_nome = nome_separado[0]
print(f'O primeiro nome é {primeiro_nome}.')

# Ultimo nome
ultimo_nome = nome_separado[-1]
print(f'O último nome é {ultimo_nome}.')

# Versão 2 - Simplificada

nome = input('Digite o seu nome: ').strip().title().split()

print(f'{' '.join(nome):<{len(nome)}}')
print(f'{nome[0]:.<{len(' '.join(nome))}}')
print(f'{nome[-1]:.>{len(' '.join(nome))}}')

# Versão 3 - Mais completa e com validação

# Laço infinito
while True:
    # Tratamento de exceções
	try:
        # Ler o nome completo
		nome = input('Digite o seu nome completo: ').strip().title()
        # Verificar se o nome é composto apenas por letras e espaços
		if nome.replace(' ', '').isalpha():
            # Separar o nome - Primeiro e último
			primeiro, último = nome.split()[0], nome.split()[-1]
			print(
				f'{'Nome:':<10}{nome:^{len(nome)}}\n'
				f'{'Primeiro:':<10}{primeiro:.<{len(nome)}}\n'
				f'{'Último:':<10}{último:.>{len(nome)}}')
		else:
			print('Somente caracteres alfabéticos e espaço (Não pode estar em branco ou conter somente espaço)')
			continue
        
		break
	except Exception:
		print('ERRO! Tente novamente.')
  
  
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário que digite o nome completo e em seguida exibe o primeiro e o último nome separadamente.
# Vamos utilizar a função input() para ler o nome completo digitado pelo usuário e a função strip() para remover espaços em branco no início e no final do nome e a função title() para deixar a primeira letra de cada palavra em maiúscula.
nome = str(input('Digite o seu nome completo: ')).strip().upper()

# Em seguida, vamos separar o nome completo em uma lista de palavras com a função split().
# Dessa forma, podemos acessar o primeiro e o último nome facilmente.
nome_separado = nome.split()

# Vamos criar uma variável para armazenar o primeiro nome e outra para armazenar o último nome.
# Para isso, utilizamos o índice [0] para acessar o primeiro nome e o índice [-1] para acessar o último nome.
primeiro_nome = nome_separado[0]
último_nome = nome_separado[-1]

# Por fim, vamos exibir o primeiro e o último nome separadamente.
print(f'O primeiro nome é {primeiro_nome}.')
print(f'O último nome é {último_nome}.')
