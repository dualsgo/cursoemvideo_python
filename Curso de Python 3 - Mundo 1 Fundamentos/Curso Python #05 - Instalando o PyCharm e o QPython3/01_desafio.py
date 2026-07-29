# Exercício Python #001 - Deixando tudo pronto - Aula 00 até 04 - Mundo 1
# Crie um programa que escreva 'Olá, mundo!' na tela.

# Tarefa 1: Escrever a mensagem na tela


print('\033[1;32mMensagem no console utilizando o valor passado pelo usuário e atribuindo-o a uma variável:\033[m')
mensagem = input('Digite a mensagem: ')
print(f'Mensagem: {mensagem}')