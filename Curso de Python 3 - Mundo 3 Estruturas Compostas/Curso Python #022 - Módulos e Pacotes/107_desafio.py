# Exercício Python #107 - Exercitando módulos em Python - Aula 00 até 22 - Mundo 3
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

numero_valido = moeda.obter_valor_inteiro('Digite um valor: ')
taxa = moeda.obter_valor_inteiro('Digite a taxa: ')

aumentado = moeda.aumentar(numero_valido, taxa)
diminuido = moeda.diminuir(numero_valido, taxa)

dobro = moeda.dobrar(numero_valido)
metade = moeda.metade(numero_valido)

print(f"{'Valor:':<15}{f'R$ {numero_valido:>10.2f}'}")
print(f"{'Aumentado 10%:':<15}{f'R$ {aumentado:>10.2f}'}")
print(f"{'Diminuído 10%:':<15}{f'R$ {diminuido:>10.2f}'}")
print(f"{'Dobro:':<15}{f'R$ {dobro:>10.2f}'}")
print(f"{'Metade:':<15}{f'R$ {metade:>10.2f}'}")

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que criar um módulo chamado moeda.py que vai ter as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Depois, vamos criar um programa que importe esse módulo e use algumas dessas funções.

# Aqui irei compartilhar todas as funções. Posteriormente você pode copiar e colar no arquivo moeda.py.

# Primeiro vamos criar a função que será responsável por obter um valor inteiro válido.

def obter_valor_inteiro(mensagem):
    # Vamos usar um loop infinito para garantir que o usuário digite um valor válido.
    while True:
        # Vamos tentar converter a entrada do usuário para um número.
        try:
            entrada = float(input(mensagem)) # Vamos usar a função float() para converter a entrada para um número.
            return entrada  # Se a conversão for bem sucedida, retornamos o valor.
        # Se a conversão falhar, vamos tratar o erro.
        except ValueError:
            # Se o erro for do tipo ValueError, vamos exibir uma mensagem de erro.
            print('Apenas valores numéricos!')
        # Para tratar erros em geral, vamos usar a cláusula except sem especificar o tipo de erro.
        except:
            # Se o erro for de qualquer outro tipo, vamos exibir uma mensagem de erro.
            print('Erro inesperado!')


# NOTA: A função acima é uma demostração de validação de entrada. Ela não é a melhor forma de fazer isso, mas é uma forma simples e didática.

# Agora vamos criar as funções que vão aumentar e diminuir um valor em uma taxa percentual.
def aumentar(valor, taxa):
    return valor + (valor * taxa / 100)


def diminuir(valor, taxa):
    return valor - (valor * taxa / 100)


# Agora vamos criar as funções que vão dobrar e dividir pela metade um valor.
def dobrar(valor):
    return valor * 2


def metade(valor):
    return valor / 2

# Agora vamos criar o programa que vai importar o módulo moeda.py e usar algumas dessas funções. Lembrando que o módulo moeda.py deve estar na mesma pasta que esse arquivo. Crie o aqruivo e copie e cole as funções nele.

# import moeda
numero_valido = obter_valor_inteiro('Digite um valor: ') # Quando importamos um módulo, precisamos usar o nome do módulo antes da função. No caso, moeda.obter_valor_inteiro(), mas aqui não farei isso pois estou usando a função no mesmo arquivo.

valor_taxa = obter_valor_inteiro('Digite a taxa: ')

# Vamos usar as funções
aumentado = aumentar(numero_valido, valor_taxa)
diminuido = diminuir(numero_valido, valor_taxa)

dobro = dobrar(numero_valido)
meio = metade(numero_valido)

# Vamos exibir os resultados
print(f"{'Valor:':<15}{f'R$ {numero_valido:>10.2f}'}")
print(f"{'Aumentado 10%:':<15}{f'R$ {aumentado:>10.2f}'}")
print(f"{'Diminuído 10%:':<15}{f'R$ {diminuido:>10.2f}'}")
print(f"{'Dobro:':<15}{f'R$ {dobro:>10.2f}'}")

