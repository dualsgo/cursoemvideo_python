# Exercício Python #067 - Tabuada v3.0 - Aula 00 até 15 - Mundo 2
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    try:
        valor = int(input('Tabuada de qual valor? '))
        if valor < 0:
            print('Programa encerrado!')
            break
        for i in range(1, 11):
            print(f'{valor:2} X {i:2} = {valor*i:3}')

    except ValueError:
        print(f'Valor de um tipo inválido para essa operação.')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

# Vamos juntar dois laços, for e while, para resolver esse problema.

# Primeiro vamos criar um laço while True para que o programa fique em loop até que o usuário decida encerrá-lo.
condição = True

# Dentro do laço while, vamos pedir para o usuário digitar um valor.
while condição:
    print('-' * 30)
    número = int(input('Tabuada de qual valor? '))
    print('-' * 30)
    
    # Se o usuário digitar um valor negativo, o programa será encerrado.
    if número < 0:
        print('Programa encerrado!')
        condição = False

    else:
            # Se o valor digitado for positivo, o programa vai mostrar a tabuada desse valor.
        for i in range(1, 11):
            print(f'{número:2} X {i:2} = {número * i:2}')
            
# A notação :2 dentro das chaves do f-string serve para alinhar os números à direita. Se o número tiver mais de 2 dígitos, ele será alinhado à esquerda. Para alinhar à direita, basta adicionar um sinal de maior > antes do número 2. Exemplo: {número: >2}.