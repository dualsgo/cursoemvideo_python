# Curso Python #07 - Operadores Aritméticos
# Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.

# OPERADORES ARITIMÉTICOS:

# Além do operador de Adição (+) temos os operadores:
print(f'Adição: 5 + 2 == {5 + 2}')

# Subtração (-)
print(f'Subtração: 5 - 2 == {5 - 2}')
# Multiplicação (*)
print(f'Multiplicação: 5 * 2 == {5 * 2}')
# Potência (**)
print(f'Potência: 5 ** 2 == {5 ** 2}')
# Divisão (/)
print(f'Divisão: 5 / 2 == {5 / 2}')
# Divisão inteira (//)
print(f'Divisão inteira: 5 // 2 == {5 // 2}')
# Resto da divisão (%)
print(f'Resto da divisão: 5 % 2 == {5 % 2}')

# Operador de Atribuição (=) - como vimos é utilizado para atribuir um valor a uma variável.

# Operador Relacional de Igualdade (==) - utilizado para comparar se dois valores são iguais.

# Ordem de precedência - Prioridades dentro de expressões - Como na matemática, o Python também segue uma ordem de precedência para realizar as operações.

# 1. Primeiro - Operações entre parênteses ().
# 2. Segundo - Potências **.
# 3. Terceiro - Multiplicação * e Divisões / // %, na ordem em que aparecem.
# 4. Quarto - Adição + e Subtração -, na ordem em que aparecem.

# Exemplos:

print(f'5 + 3 * 2 == {5 + 3 * 2}')  # Resposta: 5 + 6 == 11
print(f'3 * 5 + 4 ** 2 == {3 * 5 + 4 ** 2}')  # Resposta: 3 * 5 + 16 == 15 + 16 == 31
print(f'3 * (5 + 4) ** 2 == {3 * (5 + 4) ** 2}')  # Resposta: 3 * 9 ** 2 == 3 * 81 == 243

print('OPERADORES ARITIMÉTICOS')
print(f'5 + 3 * 2 == {5 + 3 * 2}')
print(f'5 ** 2 == {5 ** 2}')
print(f'5 ** 3 == {5 ** 3}')
print(f'19 // 2 == {19 // 2}')
print(f'19 / 2 == {19 / 2}')
print(f'365 ** 522 == {365 / 522}')
print(f'18 % 2 == {18 % 2}')
print(f'122 % 3 == {122 % 3}')
print(f'4 ** 3 == {4 ** 3}')
print(f'Com a função interna pow(base, potência): 4 ** 3 == {pow(4, 3)}')
# pow(base, potência, módulo) - Se o módulo for especificado, o resultado será (base ** potência) % módulo.

print(f'Podemos chegar a uma raiz quadrada elevando um número a meio. Exemplo: 81 ** (1/2) == {81 ** (1/2)}')
print(f'Podemos chegar a uma raiz cubica elevando um número a um terço. Exemplo: 127 ** (1/3) == {127 ** (1/3)}')


# Podemos salvar o resultado de uma operação em uma variável
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
multiplica = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2

# Podemos exibir os resultados diretamente em vez de salvar o resultado em uma variável
print(f'A soma vale {n1 + n2}.')
print(f'O produto é {multiplica}.')

# Podemos formatar o número de casas decimais que queremos com o método :.quantidadef onde quantidade é o número de casas decimais que queremos exibir.

print(f'A divisão é {divisao:.3f}.')
# A motação de dois pontos : indica uma máscara de formatação. O ponto . indica que queremos formatar um número real. O número 3 indica que queremos 3 casas decimais. O f indica que queremos um número real (float).

# Podemos exibir o conteúdo de uma instrução print() ao lado da outra em vez de em uma nova linha, substituindo o valor padrão que é uma quebra de linha (\n) pra vazio (ou outro caractere) com end='' ao final da instrução, separado por vírgula
print(f'A divisão inteira é {divisao_inteira}.', end=' ')
print(f'A potência é {exponenciacao}.')
# \n pode ser utilizado a qualquer momento para quebrar uma linha

print('\nOPERADORES EM STRINGS\n')

print('Oi' + 'Olá')  # + Concatenação
print('Oi' * 5)  # * Multiplica o texto

nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome:~^20}!')
# Com a notação de dois pontos : podemos formatar o texto. No exemplo acima reservamos 20  espaços de caracteres para o texto. Se utilizar menos será preenchido por espaços após.
# Podemos usar os símbolos <, > e ^ para escolher o alinhamento, a direita, esquerda ou centralizado. Podemos escolher o caractere específico que irá preencher os espaços em branco, o indicando antes do símbolo de alinhamento.

