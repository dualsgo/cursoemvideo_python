# Exercício Python #083 - Validando expressões matemáticas - Aula 00 até 17 - Mundo 3
#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

from ast import Expression


def processar_parenteses(expressao):
    parenteses = []
    for caractere in expressao:
        if caractere == '(':
            parenteses.append('(')
        elif caractere == ')':
            if '(' in parenteses:
                parenteses.remove('(')
    return parenteses


parenteses = processar_parenteses(input('Digite a expressão: ').strip())

print(f'A expressão {'\033[1;31mNÃO\033[m' if parenteses else '\033[1;32mÉ\033[m'} válida!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa onde o usuário digite uma expressão qualquer que use parênteses. O aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 

# A lógica é a seguinte: Cada vez que um parÊntese for aberto, vamos adicionar na lista parenteses. Cada vez que um parêntese for fechado, vamos remover o parêntese aberto da lista parenteses. Se a lista parenteses estiver vazia, a expressão é válida. Se a lista parenteses não estiver vazia, a expressão é inválida. Agora só precisamos implementar a lógica em código.

# Primeiro, é claro, precisamos saber qual é a expressão que o usuário deseja validar. Vamos solicitar a expressão ao usuário.
expressão = input('Digite a expressão: ').strip() # Solicitando a expressão ao usuário e removendo os espaços em branco.

# Em seguida, vamos percorrer cada caractere da expressão. Se o caractere for um parêntese aberto, vamos adicionar na lista parenteses. Se o caractere for um parêntese fechado, vamos remover o parêntese aberto da lista parenteses.
for caractere in expressão:
    if caractere == '(':
        parenteses.append('(')
    elif caractere == ')':
        if '(' in parenteses:
            parenteses.remove('(')

# Por fim, vamos exibir se a expressão é válida ou inválida. Se a lista parenteses estiver vazia, a expressão é válida. Se a lista parenteses não estiver vazia, a expressão é inválida.

print(f'A expressão {"\033[1;31mNÃO\033[m" if parenteses else "\033[1;32mÉ\033[m"} válida!') # Exibindo se a expressão é válida ou inválida. Se a lista parenteses estiver vazia, a expressão é válida. Se a lista parenteses não estiver vazia, a expressão é inválida.

# Não entendeu? Vamos lá: Como if espera True para executar o bloco de código, se a lista parenteses estiver vazia, que é equivalente a False, a expressão é válida e a mensagem é exibida em verde. Se a lista parenteses não estiver vazia, ou seja, tiver qualquer valor diferente de zero, que é equivalente a True, a expressão é inválida e a mensagem será exibida em vermelho.

# Se ficou confuso, você pode fazer dessa forma mais didática:
if len(parenteses) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')