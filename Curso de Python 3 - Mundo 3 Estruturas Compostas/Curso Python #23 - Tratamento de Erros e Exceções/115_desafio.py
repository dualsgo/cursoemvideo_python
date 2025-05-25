# Exercício Python #115a - Criando um menu em Python
# ___________________________________
#         MENU PRINCIPAL
# ___________________________________
# 1 - Ver pessoas cadastradas
# 2 - Cadastrar pessoas
# 3 - Sair do sistema
# ___________________________________
# Escolha a opção desejada:

# Se for um tipo diferente mostra uma mensagem de erro e pergunta novamente
# Se for um número fora do intervalo mostra o menu e pergunta novamente

# Se escolher uma opção correta mostra

# ___________________________________
#         OPÇÃO ESCOLHIDA
# ___________________________________
import json


def ver_pessoas_cadastradas():
    try:  # Tenta abrir o arquivo
        with open("pessoas.txt", "r") as arquivo:  # Abre o arquivo
            pessoas = arquivo.readlines()  # Lê o arquivo

        if not pessoas:  # Se não tiver nenhuma pessoa cadastrada
            print("Nenhuma pessoa cadastrada ainda.")  # Mostra essa mensagem
        else:  # Se tiver pessoas cadastradas
            print('--------------------------------------')
            print("Pessoas cadastradas:")  # Mostra essa mensagem
            for pessoa_json in pessoas:  # Para cada pessoa no arquivo
                pessoa = json.loads(pessoa_json)  # Carrega a pessoa
                print(f"{'Nome:':<6}{pessoa['nome']:^15}{'Idade:':<10}{pessoa['idade']:^10}")  # Mostra o nome e a idade da pessoa
            print('--------------------------------------')
    except FileNotFoundError:  # Se o arquivo não existir
        print("Nenhuma pessoa cadastrada ainda.")  # Mostra essa mensagem


def menu():  # Função para mostrar o menu
    try:  # Tenta converter o input para inteiro
        escolha_user = int(input('Digite o número da opção desejada: '))  # Pergunta a opção desejada
        return escolha_user  # Retorna a opção desejada
    except ValueError:  # Se não for possível converter para inteiro
        print('\033[1;31mErro! Digite um número inteiro válido!\033[m')  # Mostra essa mensagem
    return None  # Retorna None para mostrar o menu novamente


def cadastrar_pessoa():   # Função para cadastrar uma pessoa
    print('--------------------------------------')
    nome = input("Digite o nome da pessoa: ").strip().title()  # Pergunta o nome da pessoa
    idade = int(input("Digite a idade da pessoa: "))     # Pergunta a idade da pessoa
    pessoa = {"nome": nome, "idade": idade}   # Cria um dicionário com o nome e a idade da pessoa
    salvar_pessoa(pessoa)   # Chama a função para salvar a pessoa
    print('--------------------------------------')


def salvar_pessoa(pessoa):   # Função para salvar a pessoa
    with open("pessoas.txt", "a") as arquivo:   # Abre o arquivo
        arquivo.write(json.dumps(pessoa) + "\n")     # Escreve a pessoa no arquivo
    print("""--------------------------------------
\033[1;32mPessoa cadastrada com sucesso!\033[m
--------------------------------------""")  # Mostra essa mensagem


def escolha():   # Função para mostrar o menu e perguntar a opção desejada
    while True:  # Enquanto for verdade
        titulo('SISTEMA DE GESTÃO DE PESSOAS')   # Mostra o título
        print("""--------------------------------------
# 1 - Ver pessoas cadastradas  
# 2 - Cadastrar pessoas
# 3 - Sair do sistema
--------------------------------------""")

        num_escolhido = menu()  # Chama a função para mostrar o menu e perguntar a opção desejada

        if num_escolhido is not None:  # Se a opção for válida
            if num_escolhido == 1:  # Se a opção for 1
                ver_pessoas_cadastradas()  # Chama a função para ver as pessoas cadastradas
            elif num_escolhido == 2:  # Se a opção for 2
                cadastrar_pessoa()   # Chama a função para cadastrar uma pessoa
            elif num_escolhido == 3:     # Se a opção for 3
                titulo('SAIR DO SISTEMA')    # Mostra o título
                print('Saindo do sistema... Obrigado por utilizar!')     # Mostra essa mensagem
                break    # Para o loop
            else:    # Se a opção não for 1, 2 ou 3
                print(f'Selecione uma das opções do menu acima. {num_escolhido} não é válido!')  # Mostra essa mensagem


def titulo(frase):   # Função para mostrar o título
    print(f'-' * (len(frase) + 10))  # Mostra o traço
    print(f'\033[1;32m{frase:^35}\033[m')    # Mostra o título
    print(f'-' * (len(frase) + 10))  # Mostra o traço


escolha()  # Chama a função para mostrar o menu e perguntar a opção desejada