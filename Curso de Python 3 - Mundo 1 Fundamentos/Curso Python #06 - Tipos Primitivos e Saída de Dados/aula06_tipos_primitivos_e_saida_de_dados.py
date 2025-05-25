# Curso Python #06 - Tipos Primitivos e Saída de Dados
# Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). Além disso, veremos como fazer as primeiras operações com a função print() do Python.

# A função input() retorna um valor do tipo string por padrão, mesmo que um número seja digitado.
print('Saída do input() padrão sem conversão:')
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

# Devido a isso o sinal + não irá somar os valores e sim concatenar (unir).
soma = n1 + n2
print('A soma entre', n1, 'e', n2, 'é igual a', soma)

# A função type() é útil para verificar os tipos de dados dos valores. A sintaxe é type(valor) - pode ser uma variável, assim seu valor será verificado, ou um valor direto.

print(type(n1))  # Será exibido no console o tipo do valor contido na variável n1 que é uma string, mesmo que um número seja digitado, mas como dito antes, um input retorna por padrão um valor string.

print(type(n2))  # O mesmo ocorre com a variável n2
print(type(soma))  # E com a soma, sendo a concatenação de duas variáveis do tipo string
print('Saída do input() convertido:')

# Existem funções que convertem os valores para tipos de dados diferentes. Nesse exemplo usamos int() para converter o input() de string - str para integer - int.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2 # Agora a soma será de dois valores inteiros

print('Concatenação com vírgulas: A soma entre ', n1, ' e ', n2, ' é igual a ', soma, '.', sep='')

# Podemos exibir valores de variáveis em um print() usando uma formatação especial. Em vez de concatenar com vírgula, usamos uma máscara {} e um método .format() para substituir a máscara por um valor
print('Concatenação com .format: A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))

# A outra forma e mais recente são as f-strings. Utilizamos um f antes da string para indicar que é uma f-string e colocamos o valor dento das chaves.
print(f'Concatenação com f-string: A soma entre {n1} e {n2} é igual a {soma}.')

# Os resultados são os mesmos!

print('Saída do console da função type():')
# Os principais tipos primitivos são:
inteiros = 2  # int - Números inteiros
print(type(inteiros))
ponto_flutuante = 2.0  # float - Números com casas decimais após a vírgula
print(type(ponto_flutuante))
boolean = True  # bool - Valores lógicos, True ou False
print(type(boolean))
strings = 'Caracteres entre aspas'  # str - Cadeias de caracteres
print(type(strings))

# Se convertermos qualquer valor para str, o valor será exibido entre aspas
print(str(True))
print(str(2.0))

# Se convertermos um valor inteiro para float, um ponto seguido de um zero serão adicionados ao número
print(float(1))

# Se convertermos um valor float para int, o ponto e as casas decimais serão removidas. Não é um arredondamento, apenas deixaremos de exibir a parte decimal
print(int(3.1415))

# Ao converter uma string para bool, será exibido True. Se a string estiver vazia '' o valor é False
print(bool(''))
print(bool(' '))  # Se a string possuir um espaço, será True

# Ao converter um número int ou float para bool, zero será equivalente a False e 1 (ou mais) será True
print(bool(0))
print(bool(1.0))
print(bool(42))

# ANÁLISE DE STRINGS:
# Como sabemos, variáveis são objetos e possuem métodos. Os métodos são funções que podem ser executadas por um objeto.
# Existem métodos para analisar as strings
algo = input('Digite algo: ')


print(algo.isnumeric())  # Verifica se o valor é um número para dizer se é possível converter para int ou float
print(algo.isalpha())  # Verifica se o valor é alfabético
print(algo.isalnum())  # Verifica se o valor possui letras e números