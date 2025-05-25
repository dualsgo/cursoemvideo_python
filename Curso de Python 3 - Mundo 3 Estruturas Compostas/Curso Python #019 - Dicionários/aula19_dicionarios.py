# Curso Python #19 - Dicionários
# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

# Listas compostas comportam um ou mais valores. Cada valor receberá um índice numérico, iniciando em zero para identificar sua posição. Os valores são elementos.
# Com isso, podemos acessar os valores indicando sua posição

# Com dicionários, podemos acessar os dados através das chaves. Isso facilita a identificação dos dados

# Dicionários são identificados pelas chaves que envolvem os elementos.
# Inicializando um dicionário com dados = dict() ou podemos declarar como dados = {}

# Dentro das chaves, em vez de índices numéricos usamos chaves personalizadas
dados = {'nome': 'Pedro', 'idade': 25}

# Para visualizar um determinado elemento declaramos da seguinte forma:
print(dados['nome'])  # Usamos a chave em vez do índice numérico

# Para adicionar dados, é necessário somente declarar a lista, a nova chave entre colchetes e atribuir o valor
dados['sexo'] = 'M'
print(dados)

# Podemos modificar da mesma forma:
dados['sexo'] = 'F'

# Para remover elementos utilizamos o comando del
del dados['idade']
print(dados)

# Considerando a seguinte estrutura
filme = {'titulo': 'Star Wars',
         'ano': 1997,
         'diretor': 'George Lucas'}

# Podemos acessar itens, chaves ou valores

print(filme.values())  # Retorna os valores:
# dict_values(['Star Wars', 1997, 'George Lucas'])

print(filme.keys())  # Retorna as chaves:
# dict_keys(['titulo', 'ano', 'diretor'])

print(filme.items())  # Retorna chaves e valores:
# dict_items([('titulo', 'Star Wars'), ('ano', 1997), ('diretor', 'George Lucas')])

# Utilizando em laços

for chave, valor in filme.items():
    # O titulo é Star Wars
    # O ano é 1997
    # O diretor é George Lucas
    print(f'O {chave} é {valor}')

# Podemos utiliza listas, tuplas e dicionários em conjunto
locadora = [
        {'titulo': 'Star Wars',
         'ano': 1997,
         'diretor': 'George Lucas'},
        {'titulo': 'Avengers',
         'ano': 2012,
         'diretor': 'Joss Whedon'},
        {'titulo': 'Matrix',
         'ano': 1999,
         'diretor': 'Wachowski'}]

# Cada dicionário é um elemento e recebe seu índice dentro da lista, assim como cada par de chave e valor do dicionário é um elemento.

# Acessamos primeiro o elemento da lista e depois a chave desejada ou até mesmo o dicionário completo
print(locadora[0]['ano'])  # 1997
print(locadora[2]['titulo'])  # Matrix
print(locadora[1])  #  {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
# Ao utilizar em uma string formatada, deve-se ter atenção ao uso de aspas simples e duplas
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())  # dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values())  # dict_values(['Gustavo', 'M', 22])
print(pessoas.items())  # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

# Dicionários não suportam fatiamento como as lista. Utilizamos o método interno .copy() para contornar essa limitação
brasil = []
estados = {}
for loop in range(3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla: '))
    brasil.append(estados.copy())

# Laço para a lista
for e in brasil:
    # laço para o dicionario
    for v in e.values():
        print(v, end=' - ')
    print()