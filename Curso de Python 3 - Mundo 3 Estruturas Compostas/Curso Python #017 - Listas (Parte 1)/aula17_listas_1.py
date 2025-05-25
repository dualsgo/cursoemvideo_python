# Curso Python #17 - Listas (Parte 1)
# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# Assim como as Tuplas, as listas armazenam elementos em índices chamados de chaves que iniciam em zero.

# As listas são mutáveis! Podemos atualizar determinados valores acessando pela chave

lanches = ['hambúrguer', 'suco', 'pizza', 'pudim']
print(lanches)

# Atualizando o valor no índice 3 'pudim'
lanches[3] = 'picolé'
print(lanches)

# Adicionando um valor - Usamos o método .append() para adicionar um novo elemento a lista. Ele será adicionado no final por padrão
lanches.append('cookie')
print(lanches)

# Para adicionar em uma posição específica usamos o método .insert(indice, valor)
lanches.insert(0, 'cachorro quente')
print(lanches)

# Deletando valores - Podemos usar o método del para eliminar pelo índice
del lanches[0]
print(lanches)

# O método .pop() deleta o último elemento se passado sem parâmetro. O parâmetro é o índice que deseja remover
metodo_pop = lanches.pop()
print(f'Valor removido pelo método pop sem parâmetro: {metodo_pop}')
print(lanches)

metodo_pop = lanches.pop(3)
print(f'Valor removido pelo método pop com parâmetro: {metodo_pop}')
print(lanches)

# O método .remove(valor) remove um elemento indicando o valor
lanches.remove('hambúrguer')
# Se utilizarmos o índice a primeira ocorrência será removida

# Se o valor não pertencer à lista, um erro será exibido. Para contornar isso, usamos uma estrutura condicional para verificar se o valor está presente ou não
print(lanches)

# Usamos in para verificar
if 'hambúrguer' in lanches:
    lanches.remove('hambúrguer')
    print('Valor removido')
else:
    print('Valor não encontrado')

# Criando lista com range()
valores = list(range(0, 10))
print(valores)

# Colocar os valores em ordem
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)

valores.sort()
print(f'Lista ordenada: {valores}')
# Os valores permanecem organizados
print(valores)

valores.sort(reverse=True)
print(f'Lista ordenada invertida: {valores}')
print(valores)

# Quantidade de elementos
print(len(valores))

# Iterando listas - Podemos percorrer os elementos de uma lista
for elemento in valores:
    print(elemento, end=', ')
print('Fim.')

# Mostrando índice e valor com enumerate
for indice, elemento in enumerate(valores):
    print(f'No índice {indice} temos o elemento "{elemento}"')

# Recebendo elementos com loop
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Continuar? S/N '))

    if continuar in 'Nn':
        break
    elif continuar in 'Ss':
        print('Continuando...')
print(lista)

# Lista são ligadas se forem uma cópia da outra
lista_a = [2, 3, 4, 7]
lista_b = lista_a
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')

# Ambas são alteradas
lista_b[2] = 8
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')

# Para contornar isso atribuímos os elementos de uma lista a outra, não a própria lista

lista_a = [2, 3, 4, 7]
lista_b = lista_a[:]
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
# Cópias
lista_b[2] = 8
print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')