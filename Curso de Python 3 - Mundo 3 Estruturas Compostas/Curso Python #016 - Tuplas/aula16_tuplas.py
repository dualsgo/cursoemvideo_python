# Curso Python #16 - Tuplas
# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# Variáveis simples - Toda variável simples é um espaço na memória. Quando atribuímos um valor a variável, o espaço é preenchido. Quando desejamos atribuir um novo valor, ele substitui o valor anterior
lanche = 'hambúrguer'
print(lanche)

lanche = 'suco'
print(lanche)

# Variáveis compostas - Se quisermos atribuir mais de um valor a uma variável, devemos criar uma variável composta. Temos quatro possibilidades
# Tuplas, listas, dicionários e conjuntos

# Tuplas são identificadas por parênteses.
# Seus valores são cercados por parênteses (ou não) sendo separados por vírgulas. Cada um deles é um elemento possuindo seu próprio índice, iniciando em zero.
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche)

# Observação: strings tecnicamente são variáveis compostas. Cada caractere tem um índice!
# Podemos usar o fatiamento nas tuplas, como nas strings

# Exibir o elemento no índice 2
print(lanche[2])  # Este é o índice do valor 'pizza'

# Exibir os elementos de um intervalo
print(lanche[0:2])  # Acessando um intervalo com final determinado, do primeiro até valor anterior ao índice 2
print(lanche[1:])  # Indicando o início, mas não o fim. Será considerado até o final.
print(lanche[-1])  # Acessando o último elemento. Se diminuírmos, serão exibidos o penúltimo, antepenúltimo e assim por diante.

# O método len() exibe a quantidade de elementos da Tupla
print(len(lanche))

# Podemos usar um laço para iterar através dos elementos de uma tupla.

for elemento in lanche:  # Para cada elemento na tupla lanche - elemento será o valor
    print(f'Eu vou beber {elemento}' if elemento == 'suco' else f'Eu vou comer {elemento}')  # Exiba essa mensagem formatada.

# As tuplas em Python tem uma limitação. Elas são imutáveis!
# Não podemos atualizá-las durante a execução do programa.

# Iterando de outra forma - Caso precise do índice
for contador in range(len(lanche)):  # O contador será o índice
    print(f'{contador}: Eu vou comer {lanche[contador]}')  # lanche[contador] exibirá o valor naquele índice

# UTILIZANDO enumerate()
# enumerate() mostra a posição e o valor, então podemos usar dois contadores.
for indice, elemento in enumerate(lanche):
    print(f'{indice}: Eu vou beber {elemento}' if elemento == 'suco' else f'{indice}: Eu vou comer {elemento}')

# Podemos usar o método sorted() para organizar a tupla em ordem alfabética
print(sorted(lanche))
nova_lista = sorted(lanche)

# O método não altera a tupla, a ordenação é mostrada somente naquela instância. Mas podemos atribuir os elementos ordenados a outra variável ou atualizar a própria variável original
print(lanche)
print(nova_lista)

# Ao unir tuplas com o operador + elas serão exibidas na ordem em que forem colocadas.

tupla_a = (2, 5, 4)
tupla_b = (5, 8, 1, 2)

tupla_a_b = tupla_a + tupla_b
print(tupla_a_b)

tupla_b_a = tupla_b + tupla_a
print(tupla_b_a)

# Além do len() temos outros métodos que podem ser utilizados nas tuplas.

# .count(elemento) verifica as ocorrências de um elemento dentro da tupla
print(tupla_a_b.count(2))

# .index(elemento) verifica o índice de um elemento. Havendo mais de uma, exibe a primeira ocorrência
print(tupla_a_b.index(5))

# Podemos definir um intervalo pré-determinado com fatiamento.
print(tupla_b_a.index(5, 1))

# Tuplas aceitam valores de todos os tipos
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

# O método 'del' elimina as variáveis