# Exercício Python #047 - Contagem de pares - Aula 00 até 13 - Mundo 2
#  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Tarefa 1: Mostrar os números pares entre 1 e 50
inicio = int(input('Digite o início do intervalo: '))  # Solicita e converte o início do intervalo para inteiro
fim = int(input('Digite o fim do intervalo: '))  # Solicita e converte o fim do intervalo para inteiro

# Para qualquer número no intervalo selecionado
print('Mostrando os números pares em verde:')
for numero in range(inicio, fim + 1):
    # Se o número for par, mostre em verde, senão, mostre em vermelho
    if numero % 2 == 0:
        print(f'\033[1;32m{numero}\033[m', end=', ')
    else:
        print(f'\033[1;31m{numero}\033[m', end=', ')

print('fim da lista.')
# Também poderíamos colocar o intervalo começando em 2 e terminando no 51, com uma iteração a cada 2 em vez de utilizar a condicional.


# Versão simplificada
print('Números pares entre 1 e 50: ', end='')
for i in range(2, 51, 2):
	print(i, end=', ' if i < 50 else '.')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos mostrar todos os números pares entre 1 e 50.
# Se você entendeu como funciona o laço de repetição for, vai perceber que é muito simples fazer essa tarefa usando a função range().

# Podemos definir o intervalo de 1 a 51 (pois se definirmos de 1 a 50, o 50 não será incluído) e incrementar de 2 em 2. Assim, teremos todos os números pares entre 1 e 50.
for numero in range(1, 51, 2):  # Começa em 1, termina em 50 e incrementa de 2 em 2
    print(numero, end=', ')  # Mostra o número par

# Outra forma de resolver o exercício é verificar se o número é par dentro do laço de repetição. Desse modo, todos os números serão verificados e apenas os pares serão mostrados.
for numero in range(1, 51):
    if numero % 2 == 0:  # Se o número for par, o resto da divisão por 2 é zero
        print(numero, end=', ')  # Mostra o número par