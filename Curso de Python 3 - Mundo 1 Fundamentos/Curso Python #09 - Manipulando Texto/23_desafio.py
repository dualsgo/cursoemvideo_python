# Exercício Python #023 - Separando dígitos de um número - Aulas 00 até 09 - Mundo 1
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from random import randint
from tkinter import N

# Tarefa 1: Ler um número (Irei usar um número aleatório sorteado)
numero = randint(0, 9999)
print(numero // 10)

# Tarefa 2: Mostrar na tela cada um dos dígitos separados
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
unidade_de_milhar = (numero // 1000) % 10

print(f'O número digitado foi: {numero}.')
print(f'{'-' * 23}')
print(f'{'M':^5}|{'C':^5}|{'D':^5}|{'U':^5}')
print(f'{'-' * 23}')
print(f'{unidade_de_milhar:^5}|{centena:^5}|{dezena:^5}|{unidade:^5}')
print(f'{'-' * 23}')
# Versão 2 - Analisando a entrada do usuário

while True:
    número = input('Digite um número entre 0 e 9999: ')

    if número.isdigit() and 0 <= int(número) <= 9999:
        # Preenche com zeros à esquerda até ter 4 caracteres
        editado = número.zfill(4)
        separar = editado.replace('', ' ').split()

        # Exibe os resultados formatados
        print(f'{"Unidade:":10}{separar[-1]}\n'
              f'{"Dezena:":10}{separar[-2]}\n'
              f'{"Centena:":10}{separar[-3]}\n'
              f'{"Milhar:":10}{separar[-4]}\n')
        break
    else:
        print('Por favor, digite um número válido entre 0 e 9999.')

# Versão 3 - Utilizando a função divmod()

while True:
    número = input('Digite um número entre 0 e 9999: ')

    if número.isdigit() and 0 <= int(número) <= 9999:
        # Preenche com zeros à esquerda até ter 4 caracteres
        editado = número.zfill(4)

        # Exibe os resultados formatados
        print(f'{"Unidade:":10}{editado[3]}\n'
              f'{"Dezena:":10}{editado[2]}\n'
              f'{"Centena:":10}{editado[1]}\n'
              f'{"Milhar:":10}{editado[0]}\n')
        break
    else:
        print('Por favor, digite um número válido entre 0 e 9999.')
        
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário que digite um número entre 0 e 9999 e em seguida exibe cada um dos dígitos separados.

# Para resolver esse exercício, vamos utilizar a função input() para ler o número digitado pelo usuário.
# Precisamos decompor o número em suas unidades, dezenas, centenas e milhares.
# Para isso, vamos utilizar a divisão inteira e o resto da divisão.

# Primeiro, vamos ler o número digitado pelo usuário.
# Vamos utilizar a função input() para isso.
número = int(input('Digite um número entre 0 e 9999: '))

# Convertendo o número para inteiro para garantir que seja um número válido.

# Para decompor o número, vamos utilizar a divisão inteira e o resto da divisão.
# Para obter a unidade, vamos calcular o resto da divisão por 10. Por exemplo, se digitarmos 1234, o resto da divisão por 10 é 4 pois multiplos de 10 terminam em 0, sendo assim, o resto da divisão por 10 é o último número.
unidade = número % 10

# Para dezena, primeiro dividimos o número por 10 para remover a unidade e depois calculamos o resto da divisão por 10.
# Por exemplo, se digitarmos 1234, ao dividir por 10, obtemos 123. O resto da divisão por 10 é 3, que é a dezena.
dezena = (número // 10) % 10

# Para centena, dividimos o número por 100 para remover as unidades e dezenas e depois calculamos o resto da divisão por 10.
# Por exemplo, se digitarmos 1234, ao dividir por 100, obtemos 12. O resto da divisão por 10 é 2, que é a centena.
centena = (número // 100) % 10

# Para milhar, dividimos o número por 1000 para remover as unidades, dezenas e centenas.
# Por exemplo, se digitarmos 1234, ao dividir por 1000, obtemos 1, que é o milhar.
unidade_de_milhar = (número // 1000) % 10

# Dessa forma, caso o número tenha menos de 4 dígitos, o resultado será 0 e não haverá erro.

# Por fim, vamos exibir os resultados na tela.
print(f'O número digitado foi: {número}.')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {unidade_de_milhar}')

# É possível realizar o mesmo exercício apenas manipulando a string, sem necessidade de conversão para inteiro. Porém será necessário utilizar métodos que ainda não foram abordados no curso.