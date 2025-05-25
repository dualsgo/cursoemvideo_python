# Curso Python #10 - Condições (Parte 1)
# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

# As estruturas condicionais oferecem possibilidades distintas para situações distintas. Assim os nossos programas se tornam mais inteligentes e tomam decisões, dependendo das condições apresentadas.

# if (se) é a condicional inicial. Ela espera que a condição seja atendida, retornando True.
# else (senão) é a condicional final. Ela não necessita de uma condição própria, pois será a resposta padrão caso nenhuma condição seja atendida, retornando False.
# As estruturas condicionais utilizam a indentação para destacar seus blocos de código

# A sintaxe de uma estrutura condicional é a seguinte

if True:
    # Bloco True
    print('Bloco de código que será executado caso a condição seja atendida.')
else:
    # Bloco False
    print("Bloco de código que será executado caso a condição não seja atendida.")

# Exemplo de programa
tempo = int(input('Quantos anos tem o carro: '))

# Condicional - Utilizando uma comparação
if tempo <= 3: # O programa irá verificar se o valor da variável é menor ou igual a 3 e retornará True ou False
    print('Carro novo')
else:
    print('Carro velho')

# A mesma estrutura pode ser simplificada
print('Carro novo' if tempo <= 3 else 'Carro velho')

# Exemplo 1 - Condição simples

nome = str(input('Qual é o seu nome: ')).strip().title()

# A estrutura utiliza o valor da variável para fazer uma comparação
if nome == 'Gustavo':
    # A instrução com indentação faz parte do bloco de código da estrutura condicional e só será executada s e a condição for atendida
    print('Que nome lindo!')

    # else oferece uma possibilidade extra
else:
    print('Seu nome é normal')

# A instrução fora da indentação será exibida, independente da condição ser atendida ou não
print(f'Bom dia, {nome}.')

# Exemplo 2 - Condição composta

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
print(f'Sua média foi {media}.')

if media >= 6:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média foi ruim. Estude mais!')