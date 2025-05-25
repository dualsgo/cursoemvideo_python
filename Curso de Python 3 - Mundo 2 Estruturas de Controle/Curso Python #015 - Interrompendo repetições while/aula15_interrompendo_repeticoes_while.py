# Curso Python #15 - Interrompendo repetições while
# Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

# Loop Infinito: Um loop infinito é uma estrutura de controle de fluxo em programação na qual as instruções dentro do loop são executadas indefinidamente, sem uma condição de parada que seja eventualmente avaliada como falsa. Isso pode resultar em um programa que fica preso em execução contínua, sem progredir para as instruções seguintes no código.

# Comando break: O comando break é uma construção em muitas linguagens de programação que permite interromper imediatamente a execução de um loop, mesmo que a condição do loop ainda seja verdadeira. Em outras palavras, o break é utilizado para sair prematuramente de um loop antes que a condição de término natural seja alcançada.

# Inicializamos a variável de controle
contador = 0

# Loop while infinito
while True:
    # Incrementamos o contador
    contador += 1

    print(f'Iteração {contador}')

    # Condição de saída do loop com break
    if contador > 5:
        print('O loop foi interrompido')
        break  # O comando break interrompe imediatamente o loop

# Código após o loop
print('Código fora do loop')

# Forma de fazer sem break

numero = soma = 0  # Inicializa o número e a soma valendo zero
condicao = numero != 999  # Cria uma condição de parada. Se o número for diferente de zero permanece True

while condicao:
    numero = int(input('Digite um número: [999 ENCERRA] '))  # Recebe um número
    if numero == 999:  # Avalia se é diferente de 999. Se não for...
        condicao = False  # Atualiza a condição para False, fazendo que o loop seja parado
    else:  # Se for diferente
        soma += numero  # Soma o número

print(f'A soma é: {soma}')


# Com break

soma = 0
while True:
    numero = int(input('Digite um número: [999 ENCERRA] '))

    if numero == 999:
        break
    else:
        soma += numero

print(f'A soma é: {soma}')