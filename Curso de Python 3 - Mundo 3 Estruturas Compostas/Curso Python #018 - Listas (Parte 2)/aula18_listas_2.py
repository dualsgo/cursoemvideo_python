# Curso Python #18 - Listas (Parte 1)
# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# Declarando uma variável composta - lista: Ela pode armazenar vários valores e é mutável
dados = list()

# Adicionando um item a lista
dados.append('Pedro')  # Esse valor será adicionado e receberá o índice zero

# Se adicionar um novo elemento com append, ele será adicionado no fim da lista
dados.append(25)

# Exibindo os dados
print(dados)  # Exibirá a lista inteira
print(dados[0])  # Exibirá o elemento 'Pedro'
print(dados[1])  # Exibirá o elemento 25

# Podemos adicionar uma estrutura de lista dentro de outra
pessoas = list()

# Obs.: Se repetirmos o comando, a mesma lista será adicionada

pessoas.append(dados[:])  # dados[:] gera uma cópia da lista, dessa forma não é criada uma ligação entre as lista. Se a original for alterada não afetará a outra

pessoas.append(['Maria', 19])
pessoas.append(['João', 32])

# Cada sub-lista se tornará um elemento e receberá seu próprio índice
print(pessoas)  # Exibirá a lista completa
print(pessoas[1])  # Exibirá a sub-lista no índice 1
print(pessoas[0][1])  # Exibirá o elemento no índice 1 da sub-lista no índice 0

# Podemos declarar a lista com cada elemento
galera = [['João', 21], ['Ana', 31], ['Joaquim', 22], ['Maria', 45]]

# Percorrendo uma lista com listas: Para cada pessoa (representa uma lista dentro da lista principal) na lista galera (representa a lista principal)
for pessoa in galera:
    # Será exibido o nome que está no índice 0 e a idade que está no índice 1
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

# Podemos solicitar os dados
lista_dados = list()  # Inicializa a lista principal
dado = list()  # Inicializa um elemento que será copiado a cada iteração com dados diferentes

for contador in range(3):
    dado.append(str(input('Nome: ')).strip())  # Solicita o nome que será posicionado no índice 0

    dado.append(int(input('Idade: ')))  # Solicita a idade que será posicionada no índice 1

    lista_dados.append(dado[:])  # Adiciona uma cópia da estrutura a lista principal. Sem [:] a lista seria apagada a cada iteração e seriam geradas listas vazias

    dado.clear()  # Apaga as informações da estrutura para que ela possa ser reutilizada. Sem esse comando, a cada iteração os dados novos e antigos seriam adicionados [['A', 1], ['A', 1, 'B', 2], ['A', 1, 'B', 2, 'C', 3]]

print(lista_dados)  # [['A', 1], ['B', 2], ['C', 3]]

# Buscando dados específicos na lista

# Para cada sub-lista na lista principal
maiores = menores = 0

for pessoa in galera:
# Verifica se o índice que representa a idade [1] é maior que um determinado valor
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} tem {pessoa[1]} anos, portanto é MAIOR de idade!')
        maiores += 1
    else:
        print(f'{pessoa[0]} tem {pessoa[1]} anos, portanto é MENOR de idade!')
        menores += 1


print(f'Ao todo temos {maiores} pessoas maiores de idade.' if maiores > 0 else 'Não há pessoas maiores de idade na lista')
print(f'Ao todo temos {menores} pessoas menores de idade.' if menores > 0 else 'Não há pessoas menores de idade na lista')