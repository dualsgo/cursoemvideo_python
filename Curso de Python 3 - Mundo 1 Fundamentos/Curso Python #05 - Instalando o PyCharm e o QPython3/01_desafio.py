# Exercício Python #001 - Deixando tudo pronto - Aula 00 até 04 - Mundo 1
# Crie um programa que escreva 'Olá, mundo!' na tela.

from emoji import emojize  # Importa a função emojize do módulo emoji

# Tarefa 1: Escrever a mensagem na tela

# Método 1: Imprime a mensagem diretamente no console usando a função print() e a formatação ANSI
print('\033[1;32mMensagem direto no console com a função print():\033[m')
print(emojize('Olá, mundo! :globo_mostrando_as_américas:', language='pt'))

# Método 2: Imprime a mensagem no console usando uma variável para armazenar o valor formatado
print('\n\033[1;32mMensagem no console utilizando a variável para exibir o valor:\033[m')
mensagem = emojize('Olá, mundo! :globo_mostrando_as_américas:', language='pt')
print(mensagem)

# Método 3: Solicita ao usuário uma mensagem, atribui o valor a uma variável e imprime no console
print('\n\033[1;32mMensagem no console utilizando o valor passado pelo usuário e atribuindo-o a uma variável:\033[m')
mensagem = input('Digite a mensagem: ')
print(f'Mensagem: {mensagem}')