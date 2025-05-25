# Exercício Python #105 - Analisando e gerando Dicionários - Aula 00 até 21 - Mundo 3
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

"""def notas(*valores):
    boletim = dict()
    quantidade_notas = soma_notas = maior_nota = menor_nota = 0

    while True:
        boletim['notas'] = float(input('Digite a nota do aluno: '))

        quantidade_notas += 1

        if quantidade_notas == 1:
            maior_nota = menor_nota = boletim['notas']
        elif quantidade_notas > 1:
            if boletim['notas'] > maior_nota:
                maior_nota = boletim['notas']
            if boletim['notas'] < menor_nota:
                menor_nota = boletim['notas']

        soma_notas += boletim['notas']

        continuar = str(input('Continuar S/N')).strip().upper()
        while continuar not in 'SN':
            continuar = str(input('Comando inválido. Tente novamente')).strip().upper()
        if continuar in 'N':
            media_turma = soma_notas / quantidade_notas
            print(f'Foram cadastradas {quantidade_notas} notas.')
            print(f'A maior nota foi {maior_nota} e a menor {menor_nota}')
            print(f'A média da turma é {media_turma:.2f}')
            break
        else:
            print('Seguindo...')


notas()"""


# V2
def valor_valido():
    while True:
        entrada = input('Digite uma nota ou S para sair: ').strip().upper()
        if entrada == 'S':
            print('Saindo...')
            return None
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print('Valor inválido! Por favor, digite um número válido.')


def notas(*notas_alunos):
    if not notas_alunos:
        print('Nenhuma nota foi inserida.')
        return

    print(f'Maior nota: {max(notas_alunos)}')
    print(f'Menor nota: {min(notas_alunos)}')
    media = sum(notas_alunos) / len(notas_alunos)
    print(f'Média: {media:.2f}')
    situacao = 'REPROVADO' if media < 5 else 'RECUPERAÇÃO' if media < 7 else 'APROVADO'
    print(f'Situação: {situacao}')


notas_alunos = []
while True:
    nota = valor_valido()
    if nota is None:
        break
    notas_alunos.append(nota)


notas(*notas_alunos)

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que criar uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

# Primeiro vamos criar uma função chamada valor_valido() que vai receber uma nota do usuário e vai retornar um valor válido. Se o usuário digitar S, o programa vai encerrar. Se o usuário digitar um valor inválido, o programa vai exibir uma mensagem de erro e pedir para digitar novamente.
def valor_valido():
    while True:
        entrada = input('Digite uma nota ou S para sair: ').strip().upper()
        if entrada == 'S':
            print('Saindo...')
            return None # Se o usuário digitar S, o programa vai exibir a mensagem 'Saindo...' e vai retornar None para encerrar a função.
        
        # Se o usuário digitar um valor, o programa vai tentar converter esse valor para float para verificar se é um número válido. Se o valor for inválido, o programa vai exibir a mensagem 'Valor inválido! Por favor, digite um número válido.' e vai pedir para digitar novamente.
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print('Valor inválido! Por favor, digite um número válido.')
            
# Agora vamos criar a função notas() que vai receber várias notas de alunos e vai retornar um dicionário com as informações solicitadas.
def notas(*notas_alunos):
    if not notas_alunos:
        print('Nenhuma nota foi inserida.')
        return # Se nenhuma nota foi inserida, o programa vai exibir a mensagem 'Nenhuma nota foi inserida.' e vai encerrar a função.

    # Se notas foram inseridas, o programa vai exibir a maior nota, a menor nota, a média da turma e a situação do aluno.
    print(f'Maior nota: {max(notas_alunos)}')
    print(f'Menor nota: {min(notas_alunos)}')
    media = sum(notas_alunos) / len(notas_alunos)
    print(f'Média: {media:.2f}')
    situacao = 'REPROVADO' if media < 5 else 'RECUPERAÇÃO' if media < 7 else 'APROVADO'
    print(f'Situação: {situacao}')

# Por fim, vamos criar uma lista chamada notas_alunos que vai armazenar as notas dos alunos. Vamos criar um loop infinito que vai pedir para o usuário digitar uma nota. Se o usuário digitar S, o programa vai encerrar. Se o usuário digitar um valor válido, o programa vai adicionar a nota na lista notas_alunos.
# Quando o usuário digitar S, o programa vai chamar a função notas() passando a lista notas_alunos como argumento.
notas_alunos = []

# Vamos criar um loop infinito para pedir as notas dos alunos. Cada nota será adicionada na lista notas_alunos.
while True:
    nota = valor_valido()
    
    # Se o usuário digitar S, o programa vai encerrar o loop.
    if nota is None: # Se a função valor_valido() retornar None, o programa vai encerrar o loop. Isso ocorrerá se o usuário digitar S para sair na primeira pergunta. None é um valor especial em Python que representa a ausência de valor
        break
    notas_alunos.append(nota)
    
notas(*notas_alunos) # Por fim, vamos chamar a função notas() passando a lista notas_alunos como argumento. Se nenhuma nota foi inserida, a função vai exibir a mensagem 'Nenhuma nota foi inserida.' e vai encerrar. Se notas foram inseridas, a função vai exibir a maior nota, a menor nota, a média da turma e a situação do aluno.