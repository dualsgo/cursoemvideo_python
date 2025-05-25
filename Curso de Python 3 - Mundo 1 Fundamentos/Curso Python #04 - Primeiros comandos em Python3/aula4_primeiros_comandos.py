# Curso Python #04 - Primeiros comandos em Python3
# Agora chegou a hora de aprender os comandos básicos do Python e fazer os primeiros programas em Linguagem Python.

# Os dados de texto são delimitados por aspas simples ou duplas. Podem conter letras, números e caracteres especiais.
# Todos os comandos são funções e devem ter parênteses após seu nome.

# FUNÇÃO print():
# A função print() exibe no console o texto desejado.
# A sintaxe é o nome da função, um par de abertura e fechamento de parênteses envolvendo o valor que deseja exibir.
# print('Seu texto')

print('Olá, mundo!')  # Ao executar o programa o texto será exibido no console.

# A função exibe seu resultado em uma linha diferente, mas é possível controlar esse comportamento utilizando caracteres de escape ou atributos.

# Por exemplo, a função print() possui um atributo chamado end. O atributo end permite que você especifique o que deve ser exibido após o último caractere da função print().

# End, na verdade, é um parâmetro da função print(). Um parâmetro é um valor que a função espera receber quando é chamada. Nesse caso, end é um parâmetro opcional, pois possui um valor padrão.

# O valor padrão de end é uma quebra de linha(\n), isso faz com que a próxima instrução seja exibida em uma nova linha. Se mudarmos o valor para qualquer outro, a próxima instrução será exibida ao lado, separada pelo valor escolhido.
print('Olá, mundo!', end=' % ')
print('Olá, mundo!', end='\n')

# ERROS:
# Se uma das aspas for omitida, o programa irá apresentar um erro de sintaxe.
# Caso as duas aspas sejam omitidas o programa irá exibir um erro diferente, pois irá interpretar cada palavra como uma variável e não irá encontrá-las(além do erro de sintaxe).

# Também podemos exibir números.
# Números entre aspas são considerados textos!
# Os números são usados para cálculos matemáticos, por exemplo:
print('Dois dados numéricos são somados ao utilizar o operador de adição (+): 7 + 4 =', 7 + 4)  # Irá exibir a soma que é 11

# Se colocarmos os números entre as aspas e utilizarmos o operador de adição (+), o programa não irá apresentar um erro, mas não irá exibir a soma entre os números e sim unir os dois textos.
# Essa ação é chamada de concatenação - O operador + une strings e soma valores numéricos.
print('Duas strings são unidas ao utilizar o operador +: "7" + "4" =', '7' + '4')  # Exibe '74'

# Também é possível utilizar a vírgula para concatenar os valores. A diferença é que o operador de soma + só funciona com valores do mesmo tipo, por exemplo, string + string ou número + número.
# A vírgula permite utilizar valores de tipos diferentes:
print('Usando vírgula para concatenar um dado string ("7") e um dado numérico (4):', '7', 4)  # Irá exibir '7' 4 - haverá um espaço, pois é o separador padrão ao utilizar vírgula na concatenação.

# O separador também é um atributo de print(). O atributo sep permite que você especifique o que deve ser exibido entre os valores passados para a função print. A sintaxe é sep='separador'.

# VARIÁVEIS:
# Variáveis são úteis para armazenar os valores. Recomenda-se utilizar letras minúsculas para nomeá-las.
# Toda variável é um objeto em Python. Isso significa que ela possui atributos e métodos.
# O símbolo de = é chamado de operador de atribuição. A sintaxe da atribuição é nome da variável - operador de atribuição - valor.
# Podemos ler o operador de atribuição como 'recebe'.
nome = 'Guanabara'  # nome recebe Guanabara
idade = 25  # idade recebe 25
peso = 75.8  # peso recebe 75.8

# Se utilizarmos as variáveis nas funções print() o seu valor será exibido. Concatenamos os valores com a vírgula, pois seus valores são de tipos diferentes.
print(nome, idade, peso)

# FUNÇÃO input():
# Se quisermos criar uma interatividade com o usuário utilizamos a função input(). Essa função recebe os dados pelo teclado, digitados pelo usuário.
# A sintaxe é input('Texto que será exibido')
# Vamos sobrescrever os valores das variáveis declaradas anteriormente usando input(). Isso é possível pois o computador lê o script de cima para baixo, portanto é possível atualizar o valor de uma variável criada anteriormente.

nome = input('Digite o nome: ')
idade = input('Digite a idade: ')
peso = input('Digite o peso: ')

# Exibindo os novos valores
print(nome, idade, peso)

# Podemos mudar o separador padrão da vírgula que é um espaço para outro caractere de preferência usando o atributo sep.
print(nome, idade, peso, sep=' - ')

# Os dados recebidos pelo input() são sempre do tipo string. Para converter o tipo de dado utilizamos as funções int(), float() e str().