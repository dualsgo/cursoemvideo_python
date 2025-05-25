# Exercício Python #024 - Verificando as primeiras letras de um texto - Aulas 00 até 09 - Mundo 1
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

# Tarefa 1: Ler o nome de uma cidade.
cidade = str(input('Digite o nome da sua cidade: ')).strip().upper()

# Tarefa 2: Verificar se começa ou não com 'SANTO'
if cidade[:5] == 'SANTO':
    print(f'A cidade {cidade} começa com SANTO!')
else:
    print(f'A cidade {cidade} não começa com SANTO, e sim com {cidade[:5]}.')


# Versão 2

print('\033[1;32mComeça com Santo."\033[m' if input('Digite o nome da cidade: ').strip().title().split()[0] == 'Santo' else '\033[1;31mNão começa com "Santo"\033[m')

print('\033[1;32mComeça com "Santo"\033[m' if input('Nome da cidade: ').strip().title().startswith('Santo') else '\033[1;31mNão começa com "Santo"\033[m')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário que digite o nome de uma cidade e verifica se ela começa com a palavra "SANTO".

# Primiero vamos entender a propósta do exercício.
# O programa deve ler o nome de uma cidade e verificar se ela começa com a palavra "SANTO". Sendo assim, "SANTOS" não é uma cidade que começa com "SANTO".

# Capturar apenas os 5 primeiros caracteres da string não é uma boa ideia, pois a cidade pode ter menos de 5 caracteres ou mais de 5 caracteres. 'SANTO' tem exatamente 5 caracteres, mas 'SANTOS' tem 6 caracteres.

# Então vamos utilizar um método mais eficiente para verificar se a cidade começa com "SANTO".
# Vamos utilizar a função startswith() para verificar se a cidade começa com "SANTO". Essa função retorna True se a string começa com o valor especificado e False caso contrário.

# Vamos solicitar ao usuário que digite o nome da cidade com a função input() e tratar a string, removendo espaços em branco no início e no final com a função strip() e deixando a primeira letra de cada palavra em maiúscula com a função title().
# Em seguida, vamos verificar se a cidade começa com "SANTO" utilizando a função startswith() e exibir a mensagem correspondente.
cidade = str(input('Digite o nome da sua cidade: ')).strip().title()

if cidade.startswith('Santo'):
    print(f'A cidade {cidade} começa com SANTO!')
else:
    print(f'A cidade {cidade} não começa com SANTO.')
    
# Agora, se digitarmos 'SANTOS', o programa irá exibir a mensagem correta, pois a função startswith() verifica se a string começa com o valor especificado. Se digitarmos 'SANTOS', a função startswith() irá retornar False, pois 'SANTOS' não começa com 'SANTO', apesar de conter 'SANTO' no início da string.

# Outra forma de resolver esse exercício é utilizando a função split() para separar o nome da cidade em uma lista de palavras e verificar se a primeira palavra é igual a 'Santo'.

cidade = input('Digite o nome da cidade: ').strip().title().split()[0]
# Nessa instrução, utilizamos a função split() para separar o nome da cidade em uma lista de palavras e pegamos a primeira palavra com o índice [0].
# Em seguida, verificamos se a primeira palavra é igual a 'Santo' e exibimos a mensagem correspondente.
if cidade == 'Santo':
    print('Começa com "Santo"')
else:
    print('Não começa com "Santo"')