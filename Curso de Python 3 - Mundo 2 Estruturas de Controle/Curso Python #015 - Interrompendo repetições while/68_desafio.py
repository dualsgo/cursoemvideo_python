# Exercício Python #068 - Jogo do Par ou Ímpar - Aula 00 até 15 - Mundo 2
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
from random import randint
from emoji import emojize

vitorias = 0

def obter_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Valor inválido. Digite apenas números inteiros.')

# Loop principal do jogo
while True:
    jogador = obter_inteiro(emojize(':teclado: Digite o valor: ', language='pt'))

    # Solicitação para o jogador escolher ímpar (1) ou par (2)
    par_ou_impar = obter_inteiro(emojize(':tecla_1: Ímpar\n:tecla_2: Par\n', language='pt'))

    # Loop para garantir que o jogador escolha apenas entre 1 ou 2
    while True:
        if 1 != par_ou_impar != 2:
            print('Somente 2 para PAR ou 1 para ÍMPAR')
            par_ou_impar = int(input(''))
        else:
            break

    # Exibe a escolha do jogador
    print(emojize(f':moai: Jogador: É {"par" if par_ou_impar == 2 else "ímpar"} e jogou {jogador}...', language='pt'))
    sleep(1)

    # O computador escolhe aleatoriamente entre 1 e 2
    computador = randint(1, 2)
    print(emojize(f':rosto_de_robô: Computador: É {'par' if jogador == 1 else 'ímpar'} e jogou {computador}...', language='pt'))
    sleep(1)

    # Calcula a soma dos valores jogados
    soma = jogador + computador
    print(f'Total é: {soma}. ', end='')
    sleep(1)

    # Verifica se a soma é par ou ímpar
    par = soma % 2 == 0
    impar = not par
    print('Deu par!' if par else 'Deu ímpar!')
    sleep(1)

    # Determina o vencedor com base na escolha do jogador e no resultado
    if par and par_ou_impar == 2 or impar and par_ou_impar == 1:
        print(emojize(':marca_de_seleção: Vitória!', language='pt'))
        vitorias += 1
    else:
        print(emojize(':xis: Derrota!', language='pt'))
        break  # Encerra o jogo se o jogador perder

# Exibe o número de vitórias consecutivas
sleep(1)
print(emojize(f':troféu: Vitórias consecutivas: {vitorias}', language='pt'))

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um jogo de par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Primeiro vamos importar as bibliotecas necessárias para o jogo.
from time import sleep
from random import randint

# Vamos criar uma variável vitorias para armazenar o número de vitórias consecutivas do jogador.
vitorias = 0

# Vamos criar um laço while True para que o jogo fique em loop até que o jogador perca. A variável perdeu será usada para controlar o laço.
jogar = True


while jogar:
    # Dentro do laço while, vamos pedir para o jogador digitar um valor.
    jogador = int(input('Digite o valor: '))

    # Vamos pedir para o jogador escolher entre par (2) ou ímpar (1).
    par_ou_impar = int(input('1 para ÍMPAR\n2 para PAR\n'))

    # Vamos criar um laço while para garantir que o jogador escolha apenas entre 1 ou 2.
    while True:
        if 1 != par_ou_impar != 2:
            print('Somente 2 para PAR ou 1 para ÍMPAR')
            par_ou_impar = int(input(''))
        else:
            break

    # Vamos exibir a escolha do jogador.
    print(f'Jogador: É {"par" if par_ou_impar == 2 else "ímpar"} e jogou {jogador}...')
    sleep(1)

    # O computador escolhe aleatoriamente entre 1 e 2.
    computador = randint(1, 2)
    print(f'Computador: É {"par" if jogador == 1 else "ímpar"} e jogou {computador}...')
    sleep(1)

    # Vamos calcular a soma dos valores jogados.
    soma = jogador + computador
    print(f'Total é: {soma}. ', end='')
    sleep(1)

    # Vamos verificar se a soma é par ou ímpar.
    par = soma % 2 == 0
    impar = not par
    print('Deu par!' if par else 'Deu ímpar!')
    sleep(1)

    # Vamos determinar o vencedor com base na escolha do jogador e no resultado.
    if par and par_ou_impar == 2 or impar and par_ou_impar == 1:
        print('Vitória!')
        vitorias += 1
    else:
        print('Derrota!')
        jogar = False  # Encerra o jogo se o jogador perder 

# Vamos exibir o número de vitórias consecutivas.
sleep(1)
print(f'Vitórias consecutivas: {vitorias}')
