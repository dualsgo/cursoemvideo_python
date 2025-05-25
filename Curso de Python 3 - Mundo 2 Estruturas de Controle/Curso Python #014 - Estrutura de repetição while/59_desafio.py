# Exercício Python #059 - Criando um Menu de Opções - Aula 00 até 14 - Mundo 2
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from emoji import emojize
from numpy import result_type
continuar = True  # Inicializa a variável de controle para continuar o programa

print(emojize('Aplicativos :telefone_celular:', language='pt'))
primeiro_numero = int(input(emojize(':teclado: Escolha o primeiro número: ', language='pt')))  # Solicita e converte o primeiro número para inteiro
segundo_numero = int(input(emojize(':teclado: Escolha o segundo número: ', language='pt')))  # Solicita e converte o segundo número para inteiro
while continuar:
    print(emojize('Escolha uma das opções:\n:tecla_1: Somar :símbolo_de_adição:\n:tecla_2: Multiplicar :sinal_de_multiplicação:\n:tecla_3: Maior :régua_reta:\n:tecla_4: Novos números :teclado:\n:tecla_5: Sair do programa :botão_ejetar:', language='pt'))
    escolha = int(input(''))  # Solicita e converte a escolha para inteiro
    resultado = 0

    if escolha == 1:
        print(emojize(':símbolo_de_adição: Somando', language='pt'))
        resultado = primeiro_numero + segundo_numero
        print(f'\033[7;30;47mA soma entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 2:
        print(emojize(':sinal_de_multiplicação: Multiplicando', language='pt'))
        resultado = primeiro_numero * segundo_numero
        print(f'\033[7;30;47mO produto entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 3:
        print(emojize(':régua_reta: Maior entre eles', language='pt'))
        if primeiro_numero == segundo_numero:
            print('\033[7;30;47mOs números são iguais!\033[m')
        else:
            resultado = primeiro_numero if primeiro_numero > segundo_numero else segundo_numero
            print(f'\033[7;30;47mEntre {primeiro_numero} e {segundo_numero}, {resultado} é o maior!\033[m')

    elif escolha == 4:
        print('Escolha novos números:')
        primeiro_numero = int(input(''))  # Solicita e converte o novo primeiro número para inteiro
        segundo_numero = int(input(''))  # Solicita e converte o novo segundo número para inteiro

    elif escolha == 5:
        print('\033[1;41mEncerrando...\033[m')
        continuar = False

    else:
        print('Escolha inválida!')

    if escolha:
        continuar = input('Continuar? S/N').strip().upper()  # Solicita se o usuário deseja continuar
        if continuar == 'N':
            continuar = False
        elif continuar != 'S':
            print('Comando inválido!')
            continuar = input('S/N').strip().upper()

print('Programa finalizado!')  # Exibe mensagem de encerramento do programa

"""# VERSÃO 2

from emoji import emojize

continuar = True  # Inicializa a variável de controle para continuar o programa

print(emojize('Aplicativos :telefone_celular:', language='pt'))

primeiro_numero = int(input(emojize(':teclado: Escolha o primeiro número: ', language='pt')))
# Solicita e converte o primeiro número para inteiro

segundo_numero = int(input(emojize(':teclado: Escolha o segundo número: ', language='pt')))
# Solicita e converte o segundo número para inteiro


while continuar:
    print(emojize('Escolha uma das opções:\n:tecla_1: Somar :símbolo_de_adição:\n:tecla_2: Multiplicar :sinal_de_multiplicação:\n:tecla_3: Maior :régua_reta:\n:tecla_4: Novos números :teclado:\n:tecla_5: Sair do programa :botão_ejetar:', language='pt'))

    escolha = int(input(''))  # Solicita e converte a escolha para inteiro
    resultado = 0

    if escolha == 1:
        print(emojize(':símbolo_de_adição: Somando', language='pt'))
        resultado = primeiro_numero + segundo_numero
        print(f'\033[7;30;47mA soma entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 2:
        print(emojize(':sinal_de_multiplicação: Multiplicando', language='pt'))
        resultado = primeiro_numero * segundo_numero
        print(f'\033[7;30;47mO produto entre {primeiro_numero} e {segundo_numero} é igual a {resultado}\033[m')

    elif escolha == 3:
        print(emojize(':régua_reta: Maior entre eles', language='pt'))
        if primeiro_numero == segundo_numero:
            print('\033[7;30;47mOs números são iguais!\033[m')
        else:
            resultado = primeiro_numero if primeiro_numero > segundo_numero else segundo_numero
            print(f'\033[7;30;47mEntre {primeiro_numero} e {segundo_numero}, {resultado} é o maior!\033[m')

    elif escolha == 4:
        print('Escolha novos números:')
        primeiro_numero = int(input(''))  # Solicita e converte o novo primeiro número para inteiro
        segundo_numero = int(input(''))  # Solicita e converte o novo segundo número para inteiro

    elif escolha == 5:
        print('\033[1;41mEncerrando...\033[m')
        continuar = False

    else:
        print('Escolha inválida!')

    if escolha:
        continuar = input('Continuar? S/N').strip().upper()  # Solicita se o usuário deseja continuar
        if continuar == 'N':
            continuar = False
        elif continuar != 'S':
            print('Comando inválido!')
            continuar = input('S/N').strip().upper()

print('Programa finalizado!')  # Exibe mensagem de encerramento do programa

# VERÃO 3

def continuar():
    pergunta = input('Deseja continuar? [S] ou [N] ').upper().strip()
    while pergunta not in 'SN':
        print('Digite S para continuar ou N para encerrar')
        pergunta = input('... ').strip().upper()
    if pergunta == 'S':
        return 0
    elif pergunta == 'N':
        return 5

def obter_valores(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Este valor não é válido para essa operação.')

def menu():
    opções = [1, 2, 3, 4, 5]
    opção = 0
    while opção != 5:
        try:
            print('-'*50)
            print('Digite o número correspondente à opção desejada:'.center(50))
            print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
            print('-'*50)

            opção = int(input('Sua escolha foi: '))
            if opção == 1:
                print('-' * 50)
                print('Somar dois valores'.center(50))
                print('-' * 50)
                valor1 = obter_valores('Digite o primeiro valor: ')
                valor2 = obter_valores('Digite o segundo valor: ')
                resultado = valor1 + valor2
                print('Seu resultado:'.center(50))
                print(f'{valor1} + {valor2} = {resultado}')
                print('-' * 50)
                opção = continuar()

            elif opção == 2:
                print('-' * 50)
                print('Multiplicar dois valores'.center(50))
                print('-' * 50)
                valor1 = obter_valores('Digite o primeiro valor: ')
                valor2 = obter_valores('Digite o segundo valor: ')
                resultado = valor1 * valor2
                print('Seu resultado:'.center(50))
                print(f'{valor1} x {valor2} = {resultado}')
                print('-' * 50)
                opção = continuar()

            elif opção == 3:
                print('-' * 50)
                print('Comparar dois valores'.center(50))
                print('-' * 50)
                valor1 = obter_valores('Digite o primeiro valor: ')
                valor2 = obter_valores('Digite o segundo valor: ')
                print('-' * 50)
                print('Seu resultado:'.center(50))
                if valor1 == valor2:
                    print('Valores iguais!')
                else:
                    resultado = valor1 if valor1 > valor2 else valor2
                    print(f'Menor: {min(valor1, valor2)}, Maior: {max(valor1, valor2)} | O maior é {resultado}')
                print('-' * 50)
                opção = continuar()

            elif opção == 4:
                print('-' * 50)
                print('Digitar novos valores'.center(50))
                print('Primeiro escolha a operação')
                print('-' * 50)
                opção = 0

            elif opção == 5:
                break

        except ValueError:
            print('O valor digitado não é válido para essa operação. Tente novamente.')

    print('-' * 50)
    print('Operação encerrada!')
    print('-' * 50)

while menu() != 5:
    menu()"""
    
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que leia dois valores e mostre um menu na tela. O programa deve realizar a operação solicitada em cada caso.

# Vamos dividir o problema em partes menores:

# 1. Inicializar as variáveis de controle e os números
# 2. Exibir o menu com as opções
# 3. Realizar a operação solicitada
# 4. Solicitar novos números
# 5. Encerrar o programa

# Inicializamos a variável de controle continuar como True para iniciar o programa.
variavel_de_controle = True

# Solicitamos e convertemos os dois números para inteiros.
numero1 = int(input('Escolha o primeiro número: '))
numero2 = int(input('Escolha o segundo número: '))

# Iniciamos um loop while para continuar o programa enquanto a variável de controle continuar for True.

while variavel_de_controle:
    # Exibimos o menu com as opções para o usuário escolher.
    print('''Escolha uma das opções:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')

    # Solicitamos e convertemos a escolha para inteiro.
    escolha = int(input(''))

    # Inicializamos a variável resultado como 0.
    resultado = 0

    # Verificamos a escolha do usuário e realizamos a operação correspondente.

    # Se a escolha for 1, somamos os números e exibimos o resultado.
    if escolha == 1:
        print('Somando...')
        resultado = numero1 + numero2
        print(f'A soma entre {numero1} e {numero2} é igual a {resultado}')
        
    # Se a escolha for 2, multiplicamos os números e exibimos o resultado.
    elif escolha == 2:
        print('Multiplicando...')
        resultado = numero1 * numero2
        print(f'O produto entre {numero1} e {numero2} é igual a {resultado}')
        
    # Se a escolha for 3, verificamos qual número é maior e exibimos o resultado.
    elif escolha == 3:
        print('Maior número...')
        if numero1 == numero2:
            print('Os números são iguais!')
        else:
            resultado = numero1 if numero1 > numero2 else numero2
            print(f'Entre {numero1} e {numero2}, {resultado} é o maior!')
            
    # Se a escolha for 4, solicitamos novos números.
    elif escolha == 4:
        print('Escolha novos números:')
        numero1 = int(input(''))
        numero2 = int(input(''))
        # Após a escolha dos novos números, o programa volta para o início do loop para escolher uma nova opção.
    
    # Se a escolha for 5, encerramos o programa.
    elif escolha == 5:
        print('Encerrando...')
        variavel_de_controle = False

    # Se a escolha for inválida, exibimos uma mensagem de erro.
    else:
        print('Escolha inválida!')
