# Exercício Python #065 - Maior e Menor valores - Aula 00 até 14 - Mundo 2
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = soma = maior = menor = 0
condição = True
while condição:
		try:
			print(f'{'-' * 30}')
			número = int(input('\033[1mDigite um valor:\033[m '))

			contador += 1
			soma += número

			if contador == 1:
				maior = menor = número
			else:
				if número > maior:
					maior = número
				elif número < menor:
					menor = número

			while True:
				print(f'Você digitou o valor {número}')
				print(f'{'-' * 30}')
				continuar = input('[S] Sim [N] Não').strip().upper()
				if continuar == 'S':
					break
				elif continuar == 'N':
					condição = False
					break
				else:
					continue


		except ValueError:
			print('Este valor não e válido para essa operação.')

média = soma / contador
print(f'{'-' * 30}')
if contador == 1:
	print(f'Apenas o valor {contador} foi digitado.')
	print(f'A média é ele mesmo, além de ser o maior e o menor.')
else:
	print(f'Foram digitados {contador} valores.')
	print(f'A média entre eles é {média}')
	print(f'O maior valor digitado foi {maior}')
	print(f'O menor valor digitado foi {menor}')
print(f'{'-' * 30}')


# Usando lista
valores = []
while True:
    try:
        valor = int(input('Digite um valor: '))
        valores.append(valor)
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')

    while True:
        continuar = input('Deseja continuar? (S/N): ').strip().upper()
        if continuar not in ('S', 'N'):
            print('Resposta inválida. Por favor, digite S ou N.')
        else:
            break

    if continuar == 'N':
        break

if valores:
    print(f'A média entre todos os {len(valores)} valores digitados é {sum(valores) / len(valores)}')
    print(f'O maior valor digitado foi {max(valores)}, enquanto o menor foi {min(valores)}.')
else:
    print('Nenhum valor foi digitado.')
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que lê vários números inteiros pelo teclado. No final da execução, o programa deve mostrar a média entre todos os valores, além de exibir o maior e o menor valor lidos. O programa deve perguntar ao usuário se ele deseja continuar a digitar valores.

# Inicializamos as variáveis contador, soma, maior e menor com zero. O contador é usado para contar quantos números foram digitados, a soma é usada para acumular a soma dos números, o maior e o menor são usados para armazenar o maior e o menor valor lidos.
contador = soma = maior = menor = 0

condição = True  # Inicializamos a condição como True para iniciar o laço de repetição.

while condição:
    
    # Dentro do laço de repetição, solicitamos ao usuário que digite um valor inteiro.
    numero = int(input('Digite um valor: '))
    
    # Incrementamos o contador e a soma dos números a cada iteração do laço de repetição.
    contador += 1
    soma += numero
    
    # Verificamos se o número digitado é o primeiro valor lido. Se for, o maior e o menor valor são atualizados com o número digitado.
    if contador == 1:
        maior = menor = numero
        # Se for o primeiro valor lido, o maior e o menor valor são iguais ao número digitado.
        
    else:
		# Se não for o primeiro valor lido, comparamos o número digitado com o maior e o menor valor.
        if numero > maior:
            maior = numero

        elif numero < menor:
            menor = numero
            
    # Agora precisamos perguntar se o usuário de seja continuar a digitar valores.
    # Temos que garantir que a resposta seja 'S' ou 'N'. Vamos aprender uma forma de parar um laço de repetição com uma condição.
    
    resposta = '' # Inicializamos a variável resposta com uma string vazia. Como ela será usada dentro de outro loop, precisamos inicializá-la fora do loop para que ela exista no escopo externo. Assim ela fica com o escopo global.
    
    # break e continue são comandos que podem ser usados para controlar a execução de um laço de repetição.
    
    # O laço de repetição possui a condição True, então ele continuará executando até que a condição seja alterada para False. Nesse caso não conseguimos alterar a condição diretamente, então usamos o comando break para sair do laço de repetição.
    while True:
        resposta = input('Deseja continuar? [S/N] ').strip().upper()
        
        # Se a resposta estiver correta (ou seja, estiver dentro das opções válidas), o laço de repetição interno é interrompido com o comando break.
        if resposta in 'SN':
            break
        
        # Se não estiver correta, o laço de repetição interno continua executando até que a resposta seja correta.
        else:
            continue
	
	# Aqui estamos fora do laço de repetição que verifica a resposta do usuário.

	# Se a resposta for 'N', a condição do loop principal é alterada para False e o laço de repetição principal é encerrado.
    if resposta == 'N':
        condição = False

	# Senão, o laço de repetição principal continua executando e o usuário pode digitar mais valores.
    else:
        print('continuando...')

# Calculamos a média dos valores digitados e exibimos o resultado.
print(f'Foram digitados {contador} valores.')
print(f'A média entre eles é {soma / contador}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
print('Fim do programa')