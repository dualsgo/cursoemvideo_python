# Exercício Python #062 - Super Progressão Aritmética v3.0 - Aula 00 até 14 - Mundo 2
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

while True:

    try:
        primeiro_termo = int(input('Digite o primeiro termo: '))
        razão = int(input('Digite a razão da progressão: '))
        acumulador = primeiro_termo
        contador = 0
        termos = 10

        while True:
            while contador < termos:
                print(f'{acumulador}', end=' ⮕ ' if contador < termos - 1 else ' ⮕ PAUSA\n')
                acumulador += razão
                contador += 1
            mais_termos = int(input('Quantos termos deseja visualizar? '))
            if mais_termos == 0:
                print(f'Exibindo {mais_termos} termos...')
                break
            termos += mais_termos

        print(f'Encerrando o programa! {termos} termos exibidos')

        break

    except ValueError:
        print(f'Valor de um tipo inválido para essa operação.')
        
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos melhorar o DESAFIO 061, perguntando ao usuário se ele deseja mostrar mais alguns termos da Progressão Aritmética (PA). O programa encerrará quando o usuário disser que deseja mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo: '))  # Solicita ao usuário que digite o primeiro termo da PA.
razão = int(input('Digite a razão da progressão: '))  # Solicita ao usuário que digite a razão da PA.
acumulador = primeiro_termo  # Inicializa o acumulador com o primeiro termo da PA.
contador = 0  # Inicializa o contador de termos mostrados.
termos = 10  # Inicializa o número de termos a serem mostrados.
condicao = True  # Inicializa a condição para continuar exibindo termos adicionais.

while condicao:  # Laço de repetição principal para controlar a exibição de termos adicionais.
    while contador < termos:  # Laço de repetição para mostrar os termos da PA.
        print(f'{acumulador}', end=' ⮕ ' if contador < termos - 1 else ' ⮕ PAUSA\n')  # Exibe o termo atual e a seta se não for o último termo, senão, exibe o termo atual e a seta com a palavra PAUSA.
        acumulador += razão  # Atualiza o acumulador somando a razão da PA.
        contador += 1  # Incrementa o contador de termos mostrados.
        
    mais_termos = int(input('Quantos termos deseja visualizar? '))  # Pergunta ao usuário quantos termos adicionais deseja visualizar.
    
    if mais_termos == 0:  # Se o usuário deseja visualizar 0 termos adicionais, o programa encerra.
        print(f'Exibindo {mais_termos} termos...')  # Exibe o número total de termos exibidos.
        condicao = False  # Altera a condição para encerrar o programa.

    termos += mais_termos  # Atualiza o número de termos a serem mostrados com os termos adicionais.
    
    # Se o usuário deseja visualizar mais termos, o programa continua exibindo os termos adicionais.
    

print(f'Encerrando o programa! {termos} termos exibidos')  # Exibe uma mensagem de encerramento do programa com o número total de termos exibidos.  

# NOTA: Temos dois laços de repetição aninhados. O laço interno é responsável por exibir os termos da PA, enquanto o laço externo controla a exibição de termos adicionais. O programa só encerra quando o usuário deseja visualizar 0 termos adicionais.