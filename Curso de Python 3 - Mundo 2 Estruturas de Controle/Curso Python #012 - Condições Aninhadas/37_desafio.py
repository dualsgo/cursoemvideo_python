# Exercício Python #037 - Conversor de Bases Numéricas - Aula 00 até 12 - Mundo 2
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

import decimal


while True:
    try:
        valor = int(input('Digite um valor: '))
        escolha = int(input('Escolha a base:\n[1] Binária [2] Octal [3] Hexadecimal: '))
        if escolha == 1:
            convertido = f'{valor:b}'
            base = 'binária'
        elif escolha == 2:
            convertido = f'{valor:o}'
            base = 'octal'
        elif escolha == 3:
            convertido = f'{valor:x}'
            base = 'hexadecimal'
        else:
            print('Escolha inválida.')
            continue  # Volta ao início do loop para pedir um novo valor
        print(f'O número {valor} na base {base} é {convertido}')
        break
    except ValueError:
        print('Valor inválido para essa operação. Tente novamente.')

# Versão 2

while True:
    try:
        valor = int(input('Digite um valor: '))
        break
    except ValueError:
        print('Somente números inteiros.')

while True:
    try:
        base = int(input('''Escolha a base:\n[1]Binário\n[2]Octal\n[3]Hexadecimal'''))

        if base == 1:
            print(f'{valor} em binário: {valor:b}')
        elif base == 2:
            print(f'{valor} em octal: {valor:o}')
        elif base == 3:
            print(f'{valor} em hexadecimal: {valor:x}')
        else:
            break

    except ValueError:
        print('Base inválida!')
        
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler um número inteiro qualquer e pedir para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. O programa deve exibir o número convertido na base escolhida pelo usuário.

# A primeira coisa a ser feita é ler um número inteiro qualquer. Para isso, vamos utilizar a função input() para ler o valor e a função int() para converter o valor para inteiro.
valor = int(input('Digite um valor: '))

# Em seguida, vamos pedir para o usuário escolher a base de conversão. Para isso, vamos utilizar a função input() para ler a escolha do usuário e a função int() para converter a escolha para inteiro.
escolha = int(input('Escolha a base:\n[1] Binária [2] Octal [3] Hexadecimal: '))
# O usuário deve escolher entre 1, 2 e 3. Se o usuário escolher 1, o programa deve converter o número para binário. Se o usuário escolher 2, o programa deve converter o número para octal. Se o usuário escolher 3, o programa deve converter o número para hexadecimal.

# Para converter o número para binário, octal ou hexadecimal, vamos utilizar a função format() com a letra 'b' para binário, 'o' para octal e 'x' para hexadecimal.
if escolha == 1:
    convertido = f'{valor:b}'
    base = 'binária'
elif escolha == 2:
    convertido = f'{valor:o}'
    base = 'octal'
elif escolha == 3:
    convertido = f'{valor:x}'
    base = 'hexadecimal'
else:
    print('Escolha inválida.')

# Como não estamos fazendo validações em nossos exercícios, vamos apenas adicionar uma instrução else para exibir uma mensagem de erro caso o usuário escolha uma opção inválida. Com isso o programa será encerrado.

# Outras formas de converter um número para binário, octal e hexadecimal

# 1. Utilizando a função bin(), oct() e hex()
# Para utilizar a função bin(), oct() e hex() para converter um número para binário, octal e hexadecimal, basta passar o número como argumento da função. O retorno será uma string contendo o número convertido na base desejada. Se quisermos eliminar o prefixo '0b', '0o' e '0x', podemos utilizar a função replace() para substituir o prefixo por uma string vazia ou slice para remover os dois primeiros caracteres.
# Exemplo:
valor = 10
binário = bin(valor)[2:] # Converte o número 10 para binário sem o prefixo '0b'

# 2. Utilizando a função format()
# A função format() é uma função embutida do Python que permite formatar uma string de várias maneiras. Para converter um número para binário, octal e hexadecimal, podemos utilizar a função format() com a letra 'b' para binário, 'o' para octal e 'x' para hexadecimal. O retorno será uma string contendo o número convertido na base desejada.
# Exemplo:
valor = 10
binário = format(valor, 'b') # Converte o número 10 para binário

# 3. Utilizando f-string
# A partir da versão 3.6 do Python, podemos utilizar f-string para formatar strings. Para converter um número para binário, octal e hexadecimal, podemos utilizar f-string com a letra 'b' para binário, 'o' para octal e 'x' para hexadecimal. O retorno será uma string contendo o número convertido na base desejada.
# Exemplo:
valor = 10
binário = f'{valor:b}' # Converte o número 10 para binário

# 4. Utilizando a função int()
# A função int() pode ser utilizada para converter um número de uma base para outra. Para isso, basta passar o número como argumento da função e a base desejada como segundo argumento. O retorno será um número inteiro na base desejada.
# Exemplo:
binário = int('1010', 2) # Converte o número binário '1010' para decimal
