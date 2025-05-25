# Exercício Python #066 - Vários números com flag - Aula 00 até 15 - Mundo 2
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando a flag).


quantidade = soma = 0

while True:
    try:
        número = int(input('Digite um valor: '))

        if número != 999:
            soma += número
            quantidade += 1
        else:
            print(f'Programa encerrado!')
            if quantidade >= 1:
                print(f'Apenas o valor {soma} foi digitado')
            else:
                print(f'Foram digitados {quantidade} valores e a soma entre eles é {soma}')
            break

    except ValueError:
        print('Erro')


# Com lista

valores = []
while True:
    try:
        valor = int(input('Digite um valor: 999 Encerra'))
        if valor == 999:
            break
        valores.append(valor)
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')

if not valores:
    print('Nenhum valor foi digitado.')
else:
    print(f'A soma entre todos os {len(valores)} valores é {sum(valores)}')
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, o programa deve mostrar quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).

# Primeiro vamos iniciar a variável condição com True para que o laço while seja executado.
condição = True

# Inicializamos as variáveis quantidade e soma com 0.
quantidade = soma = 0

# Enquanto a condição for verdadeira, o programa vai pedir para o usuário digitar um valor.
while condição:
    número = int(input('Digite um valor: '))

    # Cada valor digitado será verificado se é diferente de 999. 
    if número != 999:
    # Se for, a variável soma vai receber o valor digitado e a variável quantidade vai receber mais 1.
        soma += número
        quantidade += 1
    else:
    # Se não for, o programa vai mostrar a mensagem "Programa encerrado!" e verificar se a quantidade de valores digitados é maior ou igual a 1.
        print(f'Programa encerrado!')
        if quantidade >= 1:
            print(f'Apenas o valor {soma} foi digitado')
        else:
        # Se mais de um valor foi digitado, o programa vai mostrar a quantidade de valores digitados e a soma entre eles.
            print(f'Foram digitados {quantidade} valores e a soma entre eles é {soma}')
            
        # Para finalizar o programa, a variável condição recebe False.
        condição = False