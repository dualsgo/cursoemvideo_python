# Curso Python #09 - Manipulando textos
# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

# Uma cadeia de caracteres, ou string, é um texto entre aspas simples ou duplas.

# Ao atribuir uma frase a uma variável, a frase é dividida em espaços na memória e cada um desses espaços recebe um índice que identifica sua posição, iniciando em zero. Os caracteres da frase, incluindo os espaços entre as palavras, ocupam essas posições. Esse é o comportamento de uma lista; Uma string é uma lista de caracteres.
frase = 'Curso em Vídeo Python'
# Podemos realizar operações - Fatiamento
# Tecnicamente, uma string é uma lista de caracteres. Sendo assim, podemos acessar os seus índices da mesma forma que faríamos com uma lista.

print(frase[9])
# Exibe o caractere que está posicionado no índice 9, que nesse caso é V

print(frase[9:13])
# Utilizando os dois pontos podemos indicar intervalo entre os índices que queremos buscar. Nesse caso será buscado do índice 9 e irá até o 12 (sempre exclui a última posição). Retornará Víde

print(frase[9:23])
# O primeiro dígito representa o início e o segundo o fim do intervalo. Se utilizarmos um valor para o final maior que o comprimento da string, será exibido até o final. Nesse caso Vídeo Python

print(frase[9:23:2])
# O terceiro valor é a iteração, nesse caso, pulando a cada dois e retornando VdoPto

print(frase[:5])
# Podemos omitir o início se quisermos começar do primeiro caractere. Nesse caso retorna Curso

print(frase[15:])
# Da mesma forma, podemos omitir o final se não soubermos. Nesse caso retorna Python

print(frase[9::3])
# Seguindo a mesma lógica, podemos omitir o final e indicar a iteração. Retorna VePh

# Análise

# O método len() mostra o comprimento da cadeia de caracteres
print(len(frase))

# O método .count('valor') mostra a quantidade de ocorrências de um valor informado entre as aspas

print(frase.count('o'))
# Irá exibir a quantidade de ocorrências de o minúsculo.

print(frase.count('0', 0, 13))
# Esse método aceita a indicação de um intervalo em seus argumentos

# O método .find(valor) exibe a primeira posição de um caractere ou de um conjunto
print(frase.find('deo'))
# Exibe 11, que é a posição do caractere d
# Se o valor não for encontrado, o retorno será -1

# O operador in pode ser utilizado para retornar um boolean ao verificar se há uma correspondência dentro da string
print('Curso' in frase)

# Transformação

# Uma string é imutável, mas podemos utilizar alguns métodos para alterá-la

# O método .replace(valor, novo_valor) altera um valor por outro, mas não altera a string original, apenas exibe a mudança
frase.replace('Python', 'Android')

print(frase)
# Isso não exibirá a mudança, pois a string é imutável. Mas podemos salvar o novo valor em outra variável

nova_frase = frase.replace('Python', 'Android')
print(nova_frase)

# Os métodos .upper() e .lower() transformam os caracteres em maiúsculas e minúsculas respectivamente.
print(frase.upper())
print(frase.lower())

# O método .title() transforma apenas o primeiro caractere de cada palavra em maiúsculo.
print(frase.title())

# O método .capitalize() transforma apenas o primeiro caractere em maiúsculo
print(frase.capitalize())

# Divisão de strings

# O método split() utiliza os espaços entre as palavras e divíde a string, criando uma lista com as palavras.
# Cada palavra será um elemento e terá sua própria indexação e cada caractere das palavras receberão seus próprios índices.
print(frase.split())
frase_dividida = frase.split()
print(frase_dividida[2][0])
# Nesse exemplo, o primeiro valor indica a palavra e o segundo o caractere
# Exibindo o primeiro caractere da terceira palavra

# Junção
# O método 'separador'.join(valor) reúne os itens de um conjunto separado utilizando o separador indicado.
print('-'.join(frase_dividida))

# Ou somente separa os caracteres com o separador indicado
print('-'.join(frase))


# Nesse exemplo a string recebeu espaços excedentes
frase = '   Aprenda Python   '
print(frase)

# O método .strip() irá remover os espaços desnecessários, na esquerda de na direita, mas não os espaços entre as palavras.
print(frase.strip())
# Há duas variações: Somente da direita rstrip() e somente da esquerda lstrip()