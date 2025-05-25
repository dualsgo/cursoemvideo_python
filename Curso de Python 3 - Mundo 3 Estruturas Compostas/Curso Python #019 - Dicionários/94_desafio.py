# Exercício Python #094 - Unindo dicionários e listas - Aula 00 até 19 - Mundo 3
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
mulheres = []
idade_maior_media = []
total_idade = 0

while True:
    pessoa = dict()
    pessoa["nome"] = str(input('Nome: ')).strip().upper()
    pessoa["sexo"] = str(input('Sexo: F/M ')).strip().upper()
    while pessoa["sexo"] not in 'FM':
        pessoa["sexo"] = str(input('ERRO! Sexo deve ser F ou M ')).strip().upper()
    pessoa["idade"] = int(input('Idade: '))

    total_idade += pessoa["idade"]
    pessoas.append(pessoa)

    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

pessoas_cadastradas = len(pessoas)
media_idade = total_idade / pessoas_cadastradas
print(f'A) Foram cadastradas {pessoas_cadastradas} pessoas.')
print(f'B) A média de idade do grupo é {media_idade:.2f}')

for i, v in enumerate(pessoas):
    if v['idade'] > media_idade:
        idade_maior_media.append(v.copy())
    if v['sexo'] == 'F':
        mulheres.append(v.copy())

if len(idade_maior_media) > 0:
    print(f'{"-=" * 20}')
    print(f'{"C) ACIMA DA IDADE MÉDIA DO GRUPO":^40}')
    print(f'{"-=" * 20}')

    print(f'{"Pessoa":^10}|{"Nome":^10}|{"Sexo":^10}|{"Idade":^10}')
    for i, v in enumerate(idade_maior_media):
        print(f"{i+1:^10}|{v['nome']:^10}|{v['sexo']:^10}|{v['idade']:^10}")
if len(mulheres) > 0:
    print(f'{"-=" * 20}')
    print(f'{"D) MULHERES DO GRUPO":^40}')
    print(f'{"-=" * 20}')

    print(f'{"Pessoa":^10}|{"Nome":^10}|{"Sexo":^10}|{"Idade":^10}')
    for i, v in enumerate(mulheres, 1):
        print(f"{i:^10}|{v['nome']:^10}|{v['sexo']:^10}|{v['idade']:^10}")

# v2

def print_divider():
    print('-' * 30)


def print_error(message):
    print(f'\033[1;31m{message}\033[m')


def obtem_nome():
    while True:
       print_divider()
       entrada_nome = input('Digite o nome: ').strip().title()
       if entrada_nome.replace(' ', '').isalpha():
          return entrada_nome
       else:
          print_error('NOME INVÁLIDO! Apenas caracteres alfabéticos.')


def obtem_idade():
    while True:
       try:
          idade = int(input('Digite a idade: '))
          if not (0 < idade < 100):
             print_error('Idade inválida!')
          else:
             return idade
       except ValueError:
          print_error('ERRO! Apenas dados numéricos.')


def obtem_sexo() -> object:
    while True:
       print_divider()
       entrada_sexo = input('Digite o sexo:\n[M] Masculino\n[F] Feminino\n[O] Outro\nSua resposta: ').strip().upper()
       if entrada_sexo in ['M', 'F', 'O']:
          return entrada_sexo
       else:
          print_error('Opção inválida! Tente novamente.')


def continuar():
    while True:
       print_divider()
       entrada = input('Deseja continuar?\n[S] Sim\n[N] Não\nSua resposta: ').strip().upper()
       if entrada in "SN":
          return entrada


def print_pessoa(pessoa):
    print(f"Nome: {pessoa['nome']}, Sexo: {pessoa['sexo']}, Idade: {pessoa['idade']}")


def main():
    pessoas = []
    lista_mulheres = []
    soma_idades = 0

    while True:
        pessoa = {}
        pessoa['nome'] = obtem_nome()
        pessoa['sexo'] = obtem_sexo()
        pessoa['idade'] = obtem_idade()
        soma_idades += pessoa['idade']
        pessoas.append(pessoa.copy())

        if pessoa['sexo'] in ['F', 'O']:
            lista_mulheres.append(pessoa.copy())

        if continuar() == 'N':
            break
        else:
            print('Pessoa adicionada com sucesso!')

    grupo = len(pessoas)
    média_idade = soma_idades / grupo if grupo > 0 else 0

    print(f'Foram cadastradas {grupo} pessoas!' if grupo > 1 else 'Apenas uma pessoa foi cadastrada!')
    print(f'A média de idade do grupo é de {média_idade:.1f} anos')

    if lista_mulheres:
        print('As mulheres do grupo são:')
        for mulher in lista_mulheres:
            print_pessoa(mulher)

    print('Pessoas com idade acima da média:')
    for pessoa in pessoas:
        if pessoa['idade'] > média_idade:
            print_pessoa(pessoa)


if __name__ == "__main__":
    main()
    
    
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o professor pede para criar um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostrar:

# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

# Para resolver esse exercício, vamos criar um dicionário chamado pessoa para armazenar o nome, o sexo e a idade de cada pessoa. Vamos criar uma lista chamada pessoas para armazenar todos os dicionários de pessoas. Vamos criar uma lista chamada mulheres para armazenar as mulheres. Vamos criar uma lista chamada idade_maior_media para armazenar as pessoas com idade acima da média.
pessoa = dict()
pessoas = []
mulheres = []
idade_maior_media = []
total_idade = 0

# Vamos criar um laço de repetição para adicionar várias pessoas à lista pessoas. Dentro do laço, vamos pedir o nome, o sexo e a idade de cada pessoa.
while True:
    pessoa = dict()
    pessoa["nome"] = str(input('Nome: ')).strip().upper()
    pessoa["sexo"] = str(input('Sexo: F/M ')).strip().upper()
    
    # Vamos verificar se o sexo é válido. Se não for, vamos pedir novamente.
    while pessoa["sexo"] not in 'FM':
        pessoa["sexo"] = str(input('ERRO! Sexo deve ser F ou M ')).strip().upper()
    pessoa["idade"] = int(input('Idade: '))

    # Vamos adicionar a idade da pessoa à variável total_idade.
    total_idade += pessoa["idade"]
    
    # Vamos adicionar o dicionário pessoa à lista pessoas.
    pessoas.append(pessoa)

    # Vamos perguntar se o usuário deseja continuar adicionando pessoas.
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        else:
            print('Encerrando...')
            break

# Vamos calcular o total de pessoas cadastradas e a média de idade do grupo.
pessoas_cadastradas = len(pessoas)
media_idade = total_idade / pessoas_cadastradas
print(f'A) Foram cadastradas {pessoas_cadastradas} pessoas.')
print(f'B) A média de idade do grupo é {media_idade:.2f}')

# Vamos percorrer a lista pessoas e adicionar as mulheres à lista mulheres e as pessoas com idade acima da média à lista idade_maior_media.
for i, v in enumerate(pessoas):
    if v['idade'] > media_idade:
        idade_maior_media.append(v.copy())
    if v['sexo'] == 'F':
        mulheres.append(v.copy())
        
# Vamos imprimir as pessoas com idade acima da média e as mulheres do grupo.
if len(idade_maior_media) > 0:
    print(f'{"-=" * 20}')
    print(f'{"C) ACIMA DA IDADE MÉDIA DO GRUPO":^40}')
    print(f'{"-=" * 20}')

    print(f'{"Pessoa":^10}|{"Nome":^10}|{"Sexo":^10}|{"Idade":^10}')
    for i, v in enumerate(idade_maior_media):
        print(f"{i+1:^10}|{v['nome']:^10}|{v['sexo']:^10}|{v['idade']:^10}")
        
if len(mulheres) > 0:
    print(f'{"-=" * 20}')
    print(f'{"D) MULHERES DO GRUPO":^40}')
    print(f'{"-=" * 20}')

    print(f'{"Pessoa":^10}|{"Nome":^10}|{"Sexo":^10}|{"Idade":^10}')
    for i, v in enumerate(mulheres, 1):
        print(f"{i:^10}|{v['nome']:^10}|{v['sexo']:^10}|{v['idade']:^10}")
        