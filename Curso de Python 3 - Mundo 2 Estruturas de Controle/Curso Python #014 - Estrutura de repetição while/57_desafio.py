# Exercício Python #057 - Validação de Dados - Aula 00 até 14 - Mundo 2
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

condição = True
while condição:
	sexo = input('F ou M ').strip().upper()
	condição = sexo == 'F' or sexo == 'M'
	if condição:
				# Sendo F ou M
		print('\033[1;35mSexo feminino registrado com sucesso!\033[m' if sexo == 'F' else '\033[1;34mSexo masculino registrado com sucesso!\033[m')
		print('Programa finalizado!')
		condição = False
		print('Encerrando...')
	else:
		print('Sexo inválido. Digite novamente: M ou F ')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que leia o sexo de uma pessoa e só aceite os valores 'M' ou 'F'. Caso esteja errado, o programa deve pedir a digitação novamente até ter um valor correto.

# Vamos usar um laço de repetição while para pedir a digitação do sexo. O laço de repetição while é usado quando não sabemos quantas vezes queremos repetir um bloco de código. O laço de repetição while executa um bloco de código enquanto uma condição for verdadeira.

# Em nosso caso, vamos repetir a solicitação de sexo enquanto o valor digitado não for 'M' ou 'F'. Para isso, vamos usar a estrutura de decisão if para verificar se o valor digitado é 'M' ou 'F'. Se for, o programa deve exibir uma mensagem de sucesso e encerrar. Se não for, o programa deve exibir uma mensagem de erro e pedir a digitação novamente.

# Vamos entender o código:

# Iniciamos um loop "infinito" com a palavra-chave while. O loop "infinito" é um loop que não tem um número fixo de iterações. Ele executa um bloco de código enquanto uma condição for verdadeira. No caso, a condição é True, que é sempre verdadeira.
condição = True

# Definimos uma variavel condição como True para iniciar o loop.
while condição:
    
    # Dentro do loop, pedimos a digitação do sexo. Usamos o método strip() para remover os espaços em branco do início e do fim da string e o método upper() para converter a string para letras maiúsculas.
    sexo = input('Sexo (M/F): ').strip().upper()
    
    # Verificamos se o sexo é 'M' ou 'F'. Se for, exibimos uma mensagem de sucesso e encerramos o programa. Se não for, exibimos uma mensagem de erro e pedimos a digitação novamente.
    if sexo == 'M' or sexo == 'F':
        print('Sexo registrado com sucesso!')
        
        # Se a condição do bloco if for verdadeira, precisamos encerrar o loop. Para isso, definimos a variável condição como False.
        condição = False
    
    # Se o sexo não for 'M' ou 'F', exibimos uma mensagem de erro e pedimos a digitação novamente.
    else:
        print('Sexo inválido! Por favor, insira M ou F.')
        
    # Uma mensagem informa que o sexo é inválido e a estrutura de repetição iniciará novamente.    

# Em caso de sucesso, o loop é finalizado e a mensagem de sucesso fora do loop é exibida.
print('Programa finalizado!')