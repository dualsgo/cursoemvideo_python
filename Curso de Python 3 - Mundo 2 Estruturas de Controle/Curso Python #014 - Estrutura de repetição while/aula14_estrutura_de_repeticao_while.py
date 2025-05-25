# Curso Python #014 - Estrutura de repetição while
# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:

# c=1
# while c !=10:
#      print(c)
#      c+=1
# print('Acabou')

# Diferente da estrutura for que precisa de um limite definido, a estrutura while executa o código enquanto uma condição for verdadeira.

# Laço com for - O contador é atualizado automaticamente dentro do intervalo selecionado.

for c in range(1, 11):
    print(c)

# Mesmo laço com while - Precisamos de um contador e o atualizamos dentro do loop a cada repetição para usar seu valor como comparação

c = 1  # Inicializamos o contador fora do loop
while c < 11:  # Usamos o valor para criar uma estrutura condicional
    print(c)
    c += 1  # Incrementamos o contador
    
# Na contagem com um loop while, o contador é inicializado fora do loop, a condição de parada é definida no while e o contador é atualizado dentro do loop. A posição do contador é importante, pois se for colocado antes do print() o contador será incrementado antes de ser exibido na tela.

# No exemplo de cima o contador é exibido e depois atualziado. Assim a contagem começa em 1 e termina em 10.
# Se colocarmos o contador antes do print() a contagem começa em 2 e termina em 11.
    

# O laço while é mais flexível que o for, mas é mais complexo e propenso a erros. O for é mais simples e mais seguro.

# O laço while pode ser usado para criar um menu de opções, pois pode executar o código enquanto o usuário não digitar uma opção de saída entre as opções disponíveis. Isso é conhecido como loop infinito.