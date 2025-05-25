# Exercício Python #097 - Um print especial - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def exibe_texto_adaptado(texto):
    tamanho_texto = len(texto) + 10
    print(f'{'~' * tamanho_texto}')
    print(f'{texto.center(tamanho_texto)}')
    print(f'{'~' * tamanho_texto}')


exibe_texto_adaptado(input('Digite um texto e veja o resultado: ').strip())

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, precisamos criar uma função chamada escreva() que recebe um texto como parâmetro e exibe o texto com um tamanho adaptável.

# A função escreva() recebe um parâmetro chamado texto. O texto é exibido entre duas linhas de traços. O número de traços é igual ao comprimento do texto mais 10.

def escreva(texto):
    
    # O tamanho do texto é calculado somando o comprimento do texto mais 10 para adicionar espaço em branco.
    tamanho_texto = len(texto) + 10 
    
    # A função center() é usada para centralizar o texto. O texto é centralizado em um campo de tamanho_texto caracteres.
    print(f'{"~" * tamanho_texto}')
    print(f'{texto.center(tamanho_texto)}')
    print(f'{"~" * tamanho_texto}')

# A função escreva() é chamada com o argumento entrada_usuario que é o texto digitado pelo usuário.
entrada_usuario = input('Digite um texto e veja o resultado: ').strip()

escreva(entrada_usuario)
