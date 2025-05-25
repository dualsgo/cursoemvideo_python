# Exercício Python #055 - Maior e menor da sequência - Aula 00 até 13 - Mundo 2
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Simples
import random
pesos = [round(random.uniform(60.0, 180.0), 1) for h in range(5)]
for pessoa, peso in enumerate(pesos, 1):
	print(f'Pessoa {pessoa}: {peso:>8}kg')

# Completo
from random import randint
from time import sleep

pesado = float('-inf')
leve = float('inf')

while True:
    try:
        print(f'{"-"*33}')
        print(f'|{"PESSOA":^15}|{"PESO KG":^15}|')
        print(f'{"-"*33}')
        for pessoa in range(1, 6):
            sleep(1)
            peso = randint(40, 200)
            print(f'|{pessoa:^15}|{peso: ^15.2f}|')
            if peso > pesado:
                pesado = peso
            if peso < leve:
                leve = peso
        print(f'{"-"*31}')
        print(f'A pessoa mais pesada pesa: \033[1;32m{pesado:>10.2f}Kg\033[m')
        print(f'A pessoa mais leve pesa: \033[1;31m{leve:>10.2f}Kg\033[m')
        break
    except Exception as e:
        print(f'ERRO: {e}')
        
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos ler o peso de cinco pessoas e mostrar qual foi o maior e o menor peso lidos.

# Quando quiser comparar valores, é uma boa prática inicializar as variáveis com o menor valor possível (para o menor peso) e o maior valor possível (para o maior peso). Isso garante que qualquer valor que você encontrar será maior ou menor que o valor inicial.

# Em vez de digitar um valor arbritariamente grande ou pequeno, podemos usar os valores float('-inf') e float('inf') para representar o menor e o maior valor possível, respectivamente. Essa tecnica é útil para evitar erros de comparação e se chamam de sentinela.

maior = float('-inf')  # Inicializamos a variável maior com o menor valor possível.
menor = float('inf')  # Inicializamos a variável menor com o maior valor possível.

# Entenda essa técnica. Pense no maior valor que vier na sua cabeça. Agora, pense em um valor maior que esse. Não importa o valor que você pensou, o valor float('inf') é maior que ele. O mesmo vale para o float('-inf').

# Se definirmos o maior e menor valores antes do laço, evitamos a necessidade de verificar se é a primeira iteração. Se for a primeira iteração, o valor será substituído pelo valor lido. Se não for, o valor será comparado com o valor lido e substituído se necessário.

for pessoa in range(1, 6):  # Vamos ler o peso de cinco pessoas.
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))  # Solicitamos ao usuário que digite o peso da pessoa.
    
    # Como usamos a tecnica da sentinela, não precisamos verificar se é a primeira iteração. Qualquer valor que for digitado será maior ou menor que o valor inicial. A partir daí, atualizamos os valores em cada iteração.
    
    if peso > maior:  # Se o peso for maior que o maior peso
        maior = peso  # Substituímos o maior peso pelo peso lido.
        
    if peso < menor:  # Se o peso for menor que o menor peso
        menor = peso  # Substituímos o menor peso pelo peso lido.

# Após as cinco iterações, mostramos o maior e o menor peso lidos.
print(f'O maior peso lido foi {maior:.2f}Kg')  # Mostramos o maior peso lido.
print(f'O menor peso lido foi {menor:.2f}Kg')  # Mostramos o menor peso lido.