# Exercício Python #046 - Contagem regressiva - Aula 00 até 13 - Mundo 2
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

# Tarefa 1: Importar os módulos
from time import sleep
from emoji import emojize
fogos = ':fogos_de_artifício:'
print('CONTAGEM REGRESSIVA!')
# Tarefa 2: Criar a contagem regressiva
for contagem_regressiva in range(10, -1, -1):
    print(emojize(f':tecla_{contagem_regressiva}:', language='pt'))
    sleep(1)

print(emojize(f'{fogos * 10}', language='pt'))


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício vamos criar uma contagem regressiva para o estouro de fogos de artifício.

# Primeiro, vamos importar as bibliotecas necessárias. Usaremos a função sleep da biblioteca time para dar um intervalo de 1 segundo entre os números da contagem regressiva.
from time import sleep as pausa # Usamos o comando as para renomear a função sleep para pausa. Isso é útil quando queremos usar um nome mais curto ou mais fácil de lembrar. as define um apelido para a função ou módulo importado. Isso é chamado de aliasing.	

# Vamos usar um laço de repetição for para fazer a contagem regressiva. O laço for é usado quando sabemos quantas vezes queremos repetir um bloco de código. No caso, queremos repetir 11 vezes, de 10 até 0, tendo em vista que queremos incluir o 0 na contagem regressiva.

# É importante compreender como o Python faz a contagem. 

# Sintaxe de um laço for é:
# for variável in range(início, fim, passo):
#     bloco de código

# Vamos entender cada parte do código:
# for é a palavra-chave que indica o início de um laço de repetição.
# depois da palavra-chave for, temos uma variável (que pode ter qualquer nome) que vai receber os valores do intervalo. Essa á a variável de controle do laço de repetição.
# in é a palavra-chave que indica que a variável de controle vai receber os valores do intervalo. O intervalo é definido pela função range(), mas poderia ser uma lista, tupla, conjunto ou string.
# range() é uma função que gera uma sequência de números. Ela pode receber até três argumentos: início, fim e passo. O início é o primeiro número da sequência, o fim é o último número da sequência e o passo é a diferença entre os números da sequência. Se o passo não for informado, o padrão é 1. Se o início não for informado, o padrão é 0. Se o passo for negativo, a contagem é decrescente, mas o início deve ser maior que o fim.
# : é o caractere que indica o início de um bloco de código.
# bloco de código é o conjunto de instruções que serão executadas a cada iteração do laço de repetição. O bloco de código é indentado, ou seja, está recuado em relação ao início do laço de repetição.

# Vamos entender a função range():
# O primeiro número é o início da contagem, o segundo número é o fim da contagem e o terceiro número é o passo da contagem. No caso, queremos começar a contagem em 10, terminar em 0 e decrementar de 1 em 1. Por isso, usamos range(10, -1, -1). O intervalo é fechado a esquerda e aberto a direita. Isso significa que o número 10 está incluído na contagem, mas o número -1 não está incluído.

for contagem_regressiva in range(10, -1, -1):
    print(contagem_regressiva)
    pausa(1) # Vamos usar a função pausa para dar um intervalo de 1 segundo entre os números da contagem regressiva.

