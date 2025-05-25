# Exercício Python #085 - Listas com pares e ímpares - Aula 00 até 18 - Mundo 3
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Versão 1
from random import randint

lista_principal = []
pares = []
impares = []

for i in range(7):
    lista_principal.append(randint(0, 99))

for numero in lista_principal:
    pares.append(numero) if numero % 2 == 0 else impares.append(numero)

print(f'Todos os valores:')
for valor in lista_principal:
    print(valor, end=', ')
    if valor == lista_principal[-1]:
        print(f'{valor}.')

pares.sort()
lista_principal.append(pares[:])

impares.sort()
lista_principal.append(impares[:])

print('PARES')
for par in pares:
    print(par, end=', ')
    if par == pares[-1]:
        print(f'{par}.')

print('ÍMPARES')
for impar in impares:
    print(impar, end=', ')
    if impar == impares[-1]:
        print(f'{impar}.')

# Versão 2 resumida

lista = [[], []]
for _ in range(7):
    try:
        valor = int(input('Digite um valor: '))
        lista[0 if valor % 2 == 0 else 1].append(valor)
    except ValueError:
        print('Valor inválido!')
lista[0].sort()
lista[1].sort()
print(lista)

# Versão atual

from random import randint
valores = []
pares = []
ímpares = []
for v in range(7):
	valor = randint(1, 10)
	lista = ímpares if valor % 2 else pares
	lista.append(valor)
pares.sort()
ímpares.sort()
valores.append(pares)
valores.append(ímpares)
print(valores)

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, vamos exibir os valores pares e ímpares em ordem crescente.

# Vamos fazer uma versão mais resumida. Primeiro vamos criar uma lista com duas sublistas. A primeira lista, de índice 0, vai armazenar os valores pares. A segunda lista, de índice 1, vai armazenar os valores ímpares.
lista_principal = [[], []]

# Em seguida, vamos solicitar ao usuário sete valores numéricos. Se o valor for par, vamos adicionar na lista de índice 0. Se o valor for ímpar, vamos adicionar na lista de índice 1.
for _ in range(7):
    valor = int(input('Digite um valor: ')) # Solicitando um valor numérico ao usuário
    
    # Adicionando o valor na lista de índice 0 se for par, ou na lista de índice 1 se for ímpar.
    lista_principal[0 if valor % 2 == 0 else 1].append(valor)

# Ao final das iterações, vamos ordenar as sublistas.
lista_principal[0].sort()
lista_principal[1].sort()

# Por fim, vamos exibir as sublistas.
print(f'Lista principal: {lista_principal}')
print(f'Pares: {lista_principal[0]}')
print(f'Ímpares: {lista_principal[1]}')
