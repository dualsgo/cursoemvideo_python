# Exercício Python #022 - Analisador de Textos - Aulas 00 até 09 - Mundo 1
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome_completo = input('Digite o seu nome: ').strip().title()
nome_separado = nome_completo.split()

maiúsculas = nome_completo.upper()
minúsculas = nome_completo.lower()
tamanho_nome = len(''.join(nome_separado))
tamanho_primeiro_nome = len(nome_separado[0])

print(f'{'Em MAIÚSUCULAS:':<20}{maiúsculas:>30}')
print(f'{'Em minúsuculas:':<20}{minúsculas:>30}')
print(f'{'Tamanho do nome completo:':<30}{tamanho_nome:>20}')
print(f'{'Tamanho do primeiro nome:':<30}{tamanho_primeiro_nome:>20}')

# Versão 2

nome = input('Digite o seu nome para analise: ').strip().title().split()

print(f'{'Nome digitado:':<20}{' '.join(nome):>30}')
print(f'{'Quantidade letras:':<20}{len(''.join(nome)):>30}')
print(f'{'Nome MAIÚSCULO:':<20}{' '.join(nome).upper():>30}')
print(f'{'Nome MINÚSCULO:':<20}{' '.join(nome).lower():>30}')
print(f'{'Primeiro nome:':<20}{nome[0]:>30}')
print(f'{'Quantidade letras:':<20}{len(nome[0]):>30}')


"""nome = input('Digite o seu nome para analisarmos: ').strip()

tamanho_nome = len(nome) - nome.count(' ')
primeiro_nome = nome[:nome.find(' ')].title()

print(f'{'O seu nome completo é:':<25}{nome.title():>25}')
print(f'Seu nome tem {tamanho_nome} letras')
print(f'{'Em maiúsculas:':<25}{nome.upper():>25}')
print(f'{'Em minúsculas:':<25}{nome.lower():>25}')
print(f'{'Seu primeiro nome é:':<25}{primeiro_nome:>25}')
print(f'Seu primeiro nome tem {len(primeiro_nome)} letras')
"""

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário que digite o nome completo e em seguida exibe algumas informações sobre o nome digitado.

# Primeiro, solicitamos ao usuário que digite o nome completo utilizando a função input().
# Vamos tratar o nome nessa mesma instrução, removendo espaços em branco no início e no final do nome com a função strip() e deixando a primeira letra de cada palavra em maiúscula com a função title().
nome_completo = input('Digite o seu nome: ').strip().title()

# Em seguida, vamos separar o nome completo em uma lista de palavras com a função split().
nome_separado = nome_completo.split()

# Dessa forma, podemos tratar o nome de forma mais fácil e eficiente.
# Vamos criar uma variável para armazenar o nome em maiúsculas e outra para armazenar o nome em minúsculas.
# Para isso, utilizamos as funções upper() e lower().
maiúsculas = nome_completo.upper()
minúsculas = nome_completo.lower()

# Para saber quantas letras o nome tem, vamos utilizar a função len() para contar o número de caracteres.
# No entanto, queremos contar apenas as letras, sem considerar os espaços em branco.
# Como o nome está separado em uma lista de palavras, podemos juntar todas as palavras em uma única string com a função join() e contar o número de caracteres.
tamanho_nome = len(''.join(nome_separado))

# nome_separado é uma lista de palavras, então podemos acessar o primeiro nome digitado com nome_separado[0].
primeiro_nome = nome_separado[0]
# Para saber quantas letras o primeiro nome tem, utilizamos a função len().
tamanho_primeiro_nome = len(nome_separado[0])

# Obviamente, essa não é a única forma de resolver o exercício.
# Podemos simplificar o código e obter o mesmo resultado.
# Vamos solicitar ao usuário que digite o nome completo e em seguida separar o nome em uma lista de palavras. Tudo isso em uma única instrução.
nome = input('Digite o seu nome para analise: ').strip().title().split()

# Para que fique claro, essa instrução resulta em uma lista de palavras, onde cada palavra é uma parte do nome digitado. Por exemplo, se o usuário digitar "João da Silva", a lista será ['João', 'Da', 'Silva'].

# Agora, vamos exibir as informações solicitadas usando f-strings e a função join() para juntar as palavras da lista em uma única string.
# Primeiro, exibimos o nome digitado pelo usuário.
print(f'Nome digitado: {" ".join(nome)}')

# Com essa instrução, estamos exibindo a lista, mas juntando as palavras com um espaço em branco.
# As palavras serão exibidas assim: "João Da Silva" e não assim: ['João', 'Da', 'Silva'].

# Depois, exibimos a quantidade de letras do nome completo. Como separamos as palavras, novamente podemos usar join() para juntar as palavras em uma única string e contar o número de caracteres.
print(f'Quantidade letras: {len("".join(nome))}')
# Dessa vez não precisamos remover os espaços em branco, pois a função len() já conta apenas as letras, pois juntamos as palavras em uma única string sem espaços.

# Para exibir o nome em maiúsculas e minúsculas, utilizamos as funções upper() e lower() e a função join() para juntar as palavras em uma única string.
print(f'Nome MAIÚSCULO: {" ".join(nome).upper()}')
print(f'Nome MINÚSCULO: {" ".join(nome).lower()}')

# Para exibir o primeiro nome, acessamos o primeiro elemento da lista com nome[0].
# Em seguida, exibimos a quantidade de letras do primeiro nome.
print(f'Primeiro nome: {nome[0]}')
print(f'Quantidade letras: {len(nome[0])}')