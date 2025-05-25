# Exercício Python #113 - Funções aprofundadas em Python - Aula 00 até 23 - Mundo 3
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido...')
        except KeyboardInterrupt:
            print(f'Programa foi interrompido!')


def leia_float(msg):
    while True:
        try:
            return float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido...')
        except KeyboardInterrupt:
            print(f'Programa foi interrompido!')


inteiro = leia_int('Digite um número inteiro: ')
flutuante = leia_float('Digite um número float: ')

print(f'Você digitou o número INTEIRO {inteiro}')
print(f'Você digitou o número FLOAT {flutuante}')