# Curso Python #013 - Estrutura de repetição for
# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o "for", que é uma estrutura versátil e simples de entender. Por exemplo:

# for c in range(0, 4):
#      print(c)
# print('Acabou')

# Laços, repetições ou iterações

# Laços de repetição com variável de controle realizam as instruções repetidamente, uma determinada quantidade de vezes.

# A sintaxe de um laço for é a seguinte:

for contador in range(1, 10):
    # A variável de contador irá guardar o número de repetições
    # O range é o intervalo e recebe os argumentos: início, fim e iteração opcional
    print(f'Repita isso: {contador}')
    # A instrução será executada no intervalo indicado de 1 a 10 (excluindo o 10). Serão 9 repetições
print('Pare')

# O fluxo é simples. O contador inicia no valor informadono inicio do range, executa a instrução do bloco de código, incrementa o seu valor de acordo com a iteração que por padrão é 1 e repete o processo até o valor do contador ser igual ao valor informado no fim do range.

# Se adicionarmos a iteração no range() a contagem muda

for contador in range(1, 10, 2):
    # Após o primeiro, iremos pular a cada dois
    print(f'Repita isso iterando a cada 2: {contador}')
print('Pare')

# Podemos utilizar as estruturas condicionais aninhadas num loop usando a indentação (recuo) para estruturar o código.

for contador in range(1, 10):
    print(f'Contagem: {contador}')

    # Aqui se o número for par ou ímpar, retorna o texto correspondente
    if contador % 2 == 0:
        print(f'{contador} é par.')
    elif contador % 2 == 1:
        print(f'{contador} é ímpar.')
print('Pare')

# O laço inicia em zero e termina no número anterior ao argumento. Nesse exemplo finaliza no 5
for c in range(0, 6):
    print(c)

# Se quisermos fazer em contagem regressiva, devemos começar com o maior algarismo e terminar no menor, além de usar a iteração negativa.
for c in range(6, -1, -1):
    print(c)
# Da mesma forma que antes, o algarismo do fim é desconsiderado

# Podemos entrar com os valores para o laço utilizando input() e usando as variáveis como valores dos argumentos para o range()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
iteracao = int(input('Iteração: '))

for c in range(inicio, fim, iteracao):
    print(f'Contando: {c}')
print('FIM!')

# O método enumerate() retorna uma tupla com o índice e o valor de cada elemento da lista. Podemos usar o desempacotamento para atribuir cada valor a uma variável.

for indice, valor in enumerate(range(0, 10)):
    print(f'{indice} - {valor}')
