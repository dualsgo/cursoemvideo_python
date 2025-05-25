# Curso Python #20 - Funções (Parte 1)
# Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.

# Funções são rotinas - atividade ou ações que são feitas constantemente.
# Algumas funções são built in - existem por padrão como no Python, como print(), len(), input(), int(), float() e etc

# Todas as funções são identificadas por parênteses

# Declaramos uma função com a seguinte sintaxe:
# a palavra-chave def
# o nome da função
# abertura e fechamento de parênteses. Dentro deles podem haver ou não parâmetros
# Bloco de código que será utilizado pela função para retornar ou exibir algo
def mostraLinha():
    print('-' * 30)


# Programa principal - Deve estar a duas linhas de distância da função
mostraLinha()


# Usando parâmetros
def mostraLinha(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))


mostraLinha('Curso em vídeo')


# Os parâmetros serão passados entre os parênteses e o programa irá executar a tarefa com os valores passados
def soma(a, b):
    print(f'A vale {a} e B vale {b}.')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(7, 2)


# O uso de * antes de um parâmetro permite que a função aceite um número variável de argumentos. Isso é chamado de empacotamento de argumentos. No caso da função contador, ela aceita qualquer número de argumentos e os itera.
def contador(*num):
    for valor in num:
        print(valor, end=' - ')
    print()
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)



# A função dobra modifica diretamente a lista passada como argumento. Isso é possível em Python porque as listas são mutáveis. A função faz uma alteração "in-place", evitando a necessidade de retornar uma nova lista.
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)


def somando(*valores):
    s = 0
    for numero in valores:
        s += numero
    print(f'A soma de todos os valores é {s}')


somando(4, 5, 9, 7, 2, 5)