# Exercício Python #025 - Procurando uma string dentro de outra - Aulas 00 até 09 - Mundo 1
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.4

# Tarefa 1: Ler o nome de uma pessoa
nome = str(input('Digite um nome: ')).strip().upper()

# Tarefa 2: Verificar se ha´silva no nome
if 'SILVA' in nome:
    print(f'SILVA está presente no nome {nome}.')
else:
    print(f'SILVA não está presente no nome {nome}.')
    
# Versão 2 - Simplificada

print(f'\033[1;32mContém "Silva"\033[m' if 'Silva' in input('Digite seu nome completo: ') else '\033[1;31mNão contém "Silva"\033[m')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário que digite um nome e verifica se ele contém a palavra "SILVA".

# Diferente do exercício anterior, onde verificamos se a cidade começa com "SANTO", nesse exercício precisamos verificar se a palavra "SILVA" está presente no nome, independente da posição.

# Vamos utilizar a função in para verificar se a palavra "SILVA" está presente no nome digitado pelo usuário.
nome = str(input('Digite um nome: ')).strip().upper()

if 'SILVA' in nome:
    print(f'SILVA está presente no nome {nome}.')
else:
    print(f'SILVA não está presente no nome {nome}.')
    
# Se digitarmos 'SILVA' no início, no meio ou no final do nome, o programa irá exibir a mensagem correta, pois a função in verifica se a palavra "SILVA" está presente no nome.

# in é o operador de pertencimento, que verifica se um valor está presente em uma sequência. Nesse caso, estamos verificando se a palavra "SILVA" está presente no nome digitado pelo usuário.