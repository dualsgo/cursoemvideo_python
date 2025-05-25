# Exercício Python #056 - Analisador completo - Aula 00 até 13 - Mundo 2
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Tarefa 1: Inicializar os contadores e acumuladores
membros_grupo = 0  # Inicializa o contador para o número total de membros no grupo
idades_grupo = 0  # Inicializa o acumulador para somar as idades dos membros

idade_homem_mais_velho = 0  # Inicializa a variável para armazenar a idade do homem mais velho
nome_homem_mais_velho = ''  # Inicializa a variável para armazenar o nome do homem mais velho

quantidade_mulheres = 0  # Inicializa o contador para o número de mulheres com menos de 20 anos

# Tarefa 2: Ler nome, idade e sexo
masculino = 'M'  # Atribui 'M' à variável masculino para facilitar comparações
feminino = 'F'  # Atribui 'F' à variável feminino para facilitar comparações

for pessoa in range(1, 5):  # Loop para iterar sobre 4 pessoas (de 1 a 4)
    print(f'{pessoa}º Pessoa')

    # Entrada de dados do usuário
    nome = str(input('Digite o nome da pessoa: ')).strip().title()  # Solicita e formata o nome
    idade = int(input('Digite a idade da pessoa: '))  # Solicita a idade como um número inteiro
    sexo = str(input('Digite o sexo da pessoa: F/M')).strip().upper()  # Solicita e formata o sexo
    membros_grupo += 1  # Incrementa o contador de membros no grupo

    # Verifica se é a primeira pessoa do sexo masculino ou se é mais velho que o homem mais velho atual
    if pessoa == 1 and sexo == masculino:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    else:
        # Verifica se a pessoa é do sexo masculino e se a idade é maior que a do homem mais velho atual
        if sexo == masculino and idade >= idade_homem_mais_velho:
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade

    # Conta mulheres com menos de 20 anos
    if sexo == feminino and idade < 20:
        quantidade_mulheres += 1

    # Acumula as idades para calcular a média posteriormente
    idades_grupo += idade

    # Exibe os dados cadastrados para cada pessoa
    print(f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}')
    print('Cadastro realizado com sucesso!')

# Calcula a média de idade do grupo
media_idade_grupo = idades_grupo / membros_grupo

# Exibe os resultados finais
print(f'A média de idade do grupo é {media_idade_grupo} anos.')
print(f'A homem mais velho do grupo é o {nome_homem_mais_velho} com {idade_homem_mais_velho} anos de idade.')
print(f'Entre os quatro membros do grupo, {quantidade_mulheres} são mulheres com menos de 20 anos.')

# COM VALIDAÇÃO

def valores(n, s, i):
    while True:
        name = input(n).strip().title()
        sex = input(s).upper()
        while 'M' != sex != 'F':
            print(f'Opção inválida. Digite novamente...')
            sex = input('Digite o sexo: M ou F ').upper()
        while True:
            try:
                age = int(input(i))
                break
            except ValueError:
                print('Valor inválido!')
        return name, sex, age


média_idade = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulheres_menos_vinte = 0

for pessoa in range(1, 5):
    print(f'{"-" * 20}')
    print(f'{f"{pessoa}ª pessoa:":^20}')
    print(f'{"-"*20}')

    nome, sexo, idade = valores('Digite o nome: ', 'Digite o sexo: M ou F ', 'Digite a idade: ')

    média_idade += idade

    if sexo == 'M' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade

    if sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1


print(f'A média de idade do grupo é {média_idade / 4} anos')

print(f'O homem mais velho se chama {nome_homem_velho} e tem {idade_homem_velho} anos' if nome_homem_velho else 'Não há homens no grupo')

print(f'Há {mulheres_menos_vinte}' if mulheres_menos_vinte else 'Não há', f'{'mulher' if mulheres_menos_vinte == 1 else 'mulheres'} com menos de 20 anos no grupo')

# EXTRA

# Lista para armazenar as informações das pessoas
lista_pessoas = []


def validar_nome(n):
    return n.isalpha()


def validar_idade(ida):
    return 0 <= ida <= 120


def validar_sexo(s):
    return s in ['MASCULINO', 'FEMININO']


while True:
    try:
        # Loop para coletar informações de três pessoas
        for i in range(3):

            print(f"{'-' * 30}\n{f'{i + 1}ª pessoa:':^30}\n{'-' * 30}")

            while True:
                nome = input('Nome: ').strip().title()
                if validar_nome(nome):
                    break
                else:
                    print("Nome inválido! Por favor, insira apenas letras.")

            while True:
                try:
                    idade = int(input('Idade: '))
                    if validar_idade(idade):
                        break
                    else:
                        print("Idade inválida! Por favor, insira um valor entre 0 e 120.")
                except ValueError:
                    print("Valor inválido! Por favor, insira um número para a idade.")

            while True:
                sexo = input('Sexo (Masculino/Feminino): ').strip().upper()
                if validar_sexo(sexo):
                    break
                else:
                    print("Sexo inválido! Por favor, insira 'Masculino' ou 'Feminino'.")

            pessoa = {
                'nome': nome,
                'idade': idade,
                'sexo': sexo
            }
            # Adiciona o dicionário da pessoa à lista
            lista_pessoas.append(pessoa)
        break
    except ValueError:
        print('Valor inválido!')

# Exibe a lista de pessoas
print("Informações das pessoas:")
print(f'{'-' * 30}')
for pessoa in lista_pessoas:

    print(f'Nome: {pessoa['nome']:>20}'
          f'Idade: {pessoa['idade']:>20}'
          f'Sexo: {pessoa['sexo']:>20}')
    print(f'{'-' * 30}')
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos desenvolver um programa que lê o nome, idade e sexo de 4 pessoas. No final, o programa deve mostrar a média de idade do grupo, o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Como são várias tarefas, vamos dividir o problema em partes menores:

# 1. Inicializar os contadores e acumuladores
# 2. Ler nome, idade e sexo
# 3. Calcular a média de idade do grupo
# 4. Encontrar o homem mais velho
# 5. Contar mulheres com menos de 20 anos
# 6. Exibir os resultados finais

# Vamos começar com a primeira tarefa:
membros_grupo = 0  # Inicializa o contador para o número total de membros no grupo
idades_grupo = 0  # Inicializa o acumulador para somar as idades dos membros

idade_homem_mais_velho = 0  # Inicializa a variável para armazenar a idade do homem mais velho
nome_homem_mais_velho = ''  # Inicializa a variável para armazenar o nome do homem mais velho

quantidade_mulheres = 0  # Inicializa o contador para o número de mulheres com menos de 20 anos

# Agora vamos para a segunda tarefa:
masculino = 'M'  # Atribui 'M' à variável masculino para facilitar comparações
feminino = 'F'  # Atribui 'F' à variável feminino para facilitar comparações

for pessoa in range(1, 5):  # Loop para iterar sobre 4 pessoas (de 1 a 4)
    print(f'{pessoa}º Pessoa')
    
    # Entrada de dados do usuário
    nome = str(input('Digite o nome da pessoa: ')).strip().title()  # Solicita e formata o nome
    idade = int(input('Digite a idade da pessoa: '))  # Solicita a idade como um número inteiro
    sexo = str(input('Digite o sexo da pessoa: F/M')).strip().upper()  # Solicita e formata o sexo
    membros_grupo += 1  # Incrementa o contador de membros no grupo
    
    # Verifica se é a primeira pessoa do sexo masculino ou se é mais velho que o homem mais velho atual
    if pessoa == 1 and sexo == masculino: 
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    
    else:
        # Verifica se a pessoa é do sexo masculino e se a idade é maior que a do homem mais velho atual
        if sexo == masculino and idade >= idade_homem_mais_velho:
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade
    
    # Conta mulheres com menos de 20 anos
    if sexo == feminino and idade < 20:
        quantidade_mulheres += 1
        
    # Acumula as idades para calcular a média posteriormente
    idades_grupo += idade
    
    # Exibe os dados cadastrados para cada pessoa
    print(f'Nome: {nome}\nIdade: {idade}\nSexo: {sexo}')
    print('Cadastro realizado com sucesso!')
    
# Agora vamos para a terceira tarefa:
media_idade_grupo = idades_grupo / membros_grupo  # Calcula a média de idade do grupo

# Exibe os resultados finais
print(f'A média de idade do grupo é {media_idade_grupo} anos.')
print(f'A homem mais velho do grupo é o {nome_homem_mais_velho} com {idade_homem_mais_velho} anos de idade.')
print(f'Entre os quatro membros do grupo, {quantidade_mulheres} são mulheres com menos de 20 anos.')

# Obs.: Não temos validações nesse exercícos, então muitas coisas podem dar errado. Por exemplo, se o usuário digitar um valor inválido para a idade, o programa vai gerar um erro. Para evitar isso, podemos usar estruturas de repetição e condicionais para validar as entradas do usuário. Se não forem digitadas pessoas do sexo feminino, não temos um tratamento para dizer que não há mulheres com menos de 20 anos no grupo. Podemos adicionar uma mensagem para informar isso ao usuário.