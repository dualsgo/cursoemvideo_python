# Exercício Python #040 - Aquele clássico da Média - Aula 00 até 12 - Mundo 2
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# Tarefa 1: Receber as duas notas e calcular a média
primeira_nota = float(input('Digite a primeira nota: '))
print(f'Nota do primeiro bimestre: {primeira_nota:.1f}')
segunda_nota = float(input('Digite a segunda nota: '))
print(f'Nota do segundo bimestre: {segunda_nota:.1f}')

media = (primeira_nota + segunda_nota) / 2
# Tarefa 2: Definir as condições e mensagens
print(f'\033[1mSua média foi: {media:.1f} - \033[m', end='')
if media < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif media < 7:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')
# Tarefa 3: Mostrar o resultado

# VERSÃO SIMPLIFICADA

while True:
	try:
		media = (float(input('Nota 1: ')) + float(input('Nota 2: '))) / 2
		print(f'Média: {media}', 'APROVADO' if media >= 7 else 'RECUPERAÇÃO' if media >= 5 else 'REPROVADO')
		break
	except ValueError:
		print('Valores inválidos.')


# Versão completa

from emoji import emojize
from time import sleep


def obtem_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print('O valor deve estar entre 0 e 10')
        except ValueError:
            print('Apenas números são aceitos')


notas = [obtem_nota(f'Digite a {i}ª nota: ') for i in range(1, 5)]
média = sum(notas) / len(notas)
avaliação = emojize(f'\033[1;31mREPROVADO :livro_fechado:\033[m' if média < 5 else '\033[1;33mEM RECUPERAÇÃO :livro_azul:\033[m' if média < 7 else '\033[1;32mAPROVADO :livro_verde:\033[m', language='pt')

print(f'{'-'*30}')
for i, nota in enumerate(notas, 1):
	print(f'{f'{i}ª Nota':<10}{nota:>20.2f}')
	sleep(1)
print(f'{'-'*30}')
print(f'{'Situação:':<10}{avaliação:^20}')

# EXTRA - PROGRAMINHA

from time import sleep

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
dias_frequentados = int(input(f'{'\033[1;31m'}Quantos dias frequentou a escola:{'\033[m'} '))

# faz a média das notas
media_nota = (nota1 + nota2) / 2

# valida se o aluno teve uma frequência escolar de mais de 50 dias.
# caso a frequência seja menor que 50 dias, aluno será reprovado
if dias_frequentados >= 50:
    if media_nota < 5: # Condição quando a média do aluno é menor que 5 pontos
        print('\nInfelizmente você foi reprovado, sua nota\n'
              f'foi {media_nota:.2f}')
    elif 5 <= media_nota <= 6.9: # Valida se o aluno teve nota entre 5 e 6.9.
        print(f'\nInfelizmente a sua nota foi {media_nota:.2f} e nesse caso,\n'
              f'será necessário fazer a recuperação.\n')

        validar_repeteco = int(input('Digite 1 para agendar ou 2 para sair: ')) # Confirmando com o aluno.

        print(f'\n{'\033[1;31m'}VALIDANDO INFORMAÇÕES...{'\033[m'}')
        sleep(1) # dellay de 1 segundo

        if validar_repeteco == 1: # se o aluno escolheu agendar a recuperação, cai nessa condição.
            print(f'\nProva agendada para o dia 17, a prova será composta\n'
                  'de 10 questões e cada questão valerá 1 ponto, deverá\n'
                  'tirar uma media de 7 para ser aprovado.')

            sleep(2) # dellay de 2 segundo
            print(f'\n{'\033[1;31m'}Dois mil anos depois...{'\033[m'}')

            sleep(1) # dellay de 1 segundo
            print('\nDia da prova.')

            acertos = int(input('Digite quantas questões acertou das 10: ')) # aqui pergunto quantas quantas
            # questões o aluno acertou.

            print(f'\n{'\033[1;31m'}PROCESSANDO INFORMAÇÃO...{'\033[m'}')
            sleep(1) # dellay de 1 segundo

            # Valida se o aluno acertou 7 ou mais de 7 pontos na prova da recuperação.
            if acertos >= 7:
                print(f'\nParabéns, você foi aprovado, sua nota foi {acertos}')
            else: # Caso ele tenha acertado menos que 7 pontos, será reprovado e cairá nessa condição.
                print(f'\nInfelizmente, você foi reprovado, sua nota foi {acertos}')
        else: # essa condição só será executada caso o aluno selecione a opção 2 para não
              # agendar a prova da recuperação. Na verdade, caso ele escolha qualquer opção
              # diferente de 1, já cai nessa condição.
            print('Tudo bem, lembrando que deverá voltar\n'
                  'antes do dia 13 para agendar a sua recuperação ')

    elif media_nota >= 7: # se a nota do aluno for 7 ou maior que 7, entrará nessa condição.
        print(f'\nParabéns, você foi aprovado com exíto, sua nota foi {media_nota:.2f}.')

else: # Caso o aluno tenha uma frequência menor que 50 dias, será reprovado sem as validações das notas
    print('\nInfelizmente, você foi reprovado, sua frequência escolar\n'
          'foi menor que 50 dias de aula.')
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler duas notas de um aluno e calcular a média entre elas. Em seguida, o programa deve mostrar a média calculada e a situação do aluno, conforme a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# A primeira coisa a ser feita é ler as duas notas do aluno. Para isso, vamos utilizar a função input() para ler as notas e a função float() para converter os valores para ponto flutuante.    
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Em seguida, vamos calcular a média entre as duas notas. Para isso, vamos somar as duas notas e dividir o resultado por 2.
media = (nota1 + nota2) / 2
# Note que utilizamos parenteses para garantir que a soma seja feita antes da divisão, já que a divisão tem prioridade sobre a soma.

# Por fim, vamos verificar a situação do aluno conforme a média atingida. Para isso, vamos utilizar uma estrutura condicional que verifica se a média é menor que 5, se é menor que 7 ou se é maior ou igual a 7.

if media < 5: # Condição quando a média do aluno é menor que 5. Isso exclui o 5.
    print(f'Sua média foi {media:.1f} e você está \033[1;31mREPROVADO\033[m.')

# Este elif verifica se a média do aluno é menor que 7 e maior ou igual a 5. Como o if anterior já verificou se a média é menor que 5, se ele não for atendido, a média é maior ou igual a 5.
elif media < 7: 
    print(f'Sua média foi {media:.1f} e você está de \033[1;33mRECUPERAÇÃO\033[m.')

# Este else é executado quando a média do aluno é maior ou igual a 7. Como os ifs anteriores já verificaram se a média é menor que 5 ou menor que 7, se ele não for atendido, a média é maior ou igual a 7
else:
    print(f'Sua média foi {media:.1f} e você está \033[1;32mAPROVADO\033[m.')