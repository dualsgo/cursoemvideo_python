# Exercício Python #053 - Detector de Palíndromo - Aula 00 até 13
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

from matplotlib.pylab import f


frase = str(input('Digite sua frase ou palavra: ')).strip().upper()  # Solicita e converte a frase para maiúsculas e remove espaços extras
# Remove espaços da frase original
frase = frase.split() # Separa a frase em palavras
nova_frase = []  # Inicializa a variável para armazenar a nova frase invertida

# Inverte a frase
for palavra in frase: # Percorre cada palavra da frase
    nova_palavra = '' # Inicializa a variável para armazenar a nova palavra invertida
    for letra in palavra[::-1]: # Percorre cada letra da palavra de trás para frente
        nova_palavra += letra  # Adiciona cada letra invertida à nova frase
    nova_frase.append(nova_palavra) # Adiciona cada palavra invertida à nova frase

print(f'A frase digitada foi: {' '.join(frase)}') # Imprime a frase original
print(f'O inverso da frase é: {' '.join(nova_frase)}') # Imprime a frase invertida

# Verifica se é um palíndromo
if nova_frase == frase:
    print('A frase é um palíndromo!') # Imprime se for um palíndromo
else: 
    print('A frase não é um palíndromo!') # Imprime se não for um palíndromo
    

# Simplificação do código
frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
print('Palíndromo' if frase == frase[::-1] else 'Não é palíndromo')

# Outra versão
frase = input('Frase: ').strip().upper().replace(' ', '')
frase_invertida = frase[::-1]

if frase == frase_invertida:
	print(f'\033[1;32m{frase}\n{frase_invertida}\033[m')
else:
	print(f'\033[1;31m{frase}\n{frase_invertida}\033[m')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos ler uma frase e verificar se ela é um palíndromo. Um palíndromo é uma palavra, frase ou número que se lê da mesma forma de trás para frente. Exemplos de palíndromos são: "ovo", "arara", "Ame o poema", "A sogra má e amargosa", "A mala nada na lama", "A torre da derrota", "A cara rajada da jararaca", "Ame o poema", "A base do teto desaba", "A cara rajada da jararaca", "A dama admirou o rim da amada", "A grama é amarga", "A mala nada na lama

# Como aprendemos, o laço for pode ser usado para percorrer uma sequência de elementos. Uma string é uma sequência de caracteres, então podemos usar o laço for para percorrer cada letra da frase. Para inverter a frase, podemos usar o fatiamento de strings.

# Primeiro solicitamos ao usuário que digite uma frase. Em seguida, removemos os espaços extras da frase e convertemos para letras maiúsculas. Depois, usamos o método split() para separar a frase em palavras. Em seguida, criamos uma lista vazia para armazenar a nova frase invertida.
frase = str(input('Digite sua frase ou palavra: ')).strip().upper().replace(' ', '')  # Nesse comando, usamos três métodos
# .strip() remove espaços extras no início e no final da string.
# .upper() converte a string para letras maiúsculas.
# .replace(' ', '') remove todos os espaços da string.

# Podemos inverter a frase com slicing. Para isso, usamos o fatiamento de strings. O fatiamento de strings é uma técnica que permite acessar partes de uma string. O fatiamento de strings é feito com colchetes e dois pontos. O primeiro número é o índice inicial e o segundo número é o índice final. Se o índice final for omitido, o fatiamento será feito até o final da string. Se o índice inicial for omitido, o fatiamento será feito a partir do início da string. Se ambos forem omitidos, o fatiamento será feito em toda a string. O terceiro número é o passo, que indica quantos caracteres serão pulados. Se o passo for negativo, a string será invertida.
frase_invertida = frase[::-1]  # Inverte a frase

# Exibimos a frase original e a frase invertida. Usamos o método .center() para centralizar a frase na tela ou a notação de f-string com o alinhamento central (^) para centralizar a frase invertida.
print(f'Frase original: {frase.center(31)}')
print(f'Frase invertida: {frase_invertida:^30}')

# Obs.: A quantidade de caracteres foi diferente (31 e 30) pois 'Frase original:' tem 14 caracteres e 'Frase invertida:' tem 15 caracteres. Por isso, a quantidade de caracteres foi ajustada para centralizar as frases de forma simétrica. Se quiser pode aumentar a quantidade de caracteres para frases maiores.

# Para verificar se a frase é um palíndromo, comparamos a frase original com a frase invertida. Se forem iguais, a frase é um palíndromo, senão, não é um palíndromo. Usamos uma estrutura condicional if/else para verificar se a frase é um palíndromo.
if frase == frase_invertida:  # Se a frase original for igual à frase invertida
    print('A frase é um palíndromo!')  # Mostramos que a frase é um palíndromo
else:  # Senão
    print('A frase não é um palíndromo!')  # Mostramos que a frase não é um palíndromo
    
# Como o objetivo do exercício é treinar laço for, vamos fazer outra versão.

frase = str(input('Digite sua frase ou palavra: ')).strip().upper()

frase_sem_espaco = ''.join(frase.split()) # Remove os espaços da frase usando o método .split() que separa a frase em palavras e o método .join() que junta as palavras sem espaços
frase_invertida = '' # Inicializa a variável para armazenar a frase invertida
for palavra in frase_sem_espaco[::-1]: # Percorre cada letra da frase de trás para frente
    # omitimos o inicio e o fim do fatiamento, indicando que queremos percorrer a frase inteira e com passo -1, indicando que queremos percorrer a frase de trás para frente
    
    for letra in palavra: 
        frase_invertida += letra
        
print(f'A frase digitada foi: {frase_sem_espaco}')
print(f'O inverso da frase é: {frase_invertida}')

if frase_sem_espaco == frase_invertida:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')





"""# Tarefa 1: Ler a palavra ou frase
frase = str(input('Digite a palavra ou frase: ')).strip().upper()
frase_palavras = frase.split()
frase_sem_espaco = ''.join(frase_palavras)
frase_invertida = frase_sem_espaco[::-1]
print(f'A frase {frase_sem_espaco} ao contrário é {frase_invertida}')
palindromo = frase_sem_espaco == frase_invertida
if palindromo:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')"""