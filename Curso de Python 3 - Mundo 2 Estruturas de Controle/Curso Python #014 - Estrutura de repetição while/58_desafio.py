# Exercício Python #058 - Jogo da Adivinhação v2.0 - Aula 00 até 14 - Mundo 2
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from emoji import emojize
from random import randint
from time import sleep


def palpite(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Opção inválida! Digite um número válido.')


print(emojize(f'{':videogame: Vamos jogar! :videogame:':^30}', language='pt'))
print(emojize('Sou o seu computador... :rosto_de_robô:\nAcabei de pensar em um número entre 0 e 10. :rosto_pensativo:\nTente adivinhar!', language='pt'))
palpites = 1  # Inicializa o contador de palpites
computador = randint(0, 10)  # Gera um número aleatório entre 0 e 10

jogador = palpite(f'{palpites}ª tentativa: ')  # Solicita e converte o palpite do jogador para inteiro

while jogador != computador:
    palpites += 1  # Incrementa o contador de palpites
    print(emojize('ERROU! :xis:', language='pt'))  # Exibe mensagem de erro
    print(emojize(':seta_para_cima: Mais...', language='pt') if jogador < computador else emojize(':seta_para_baixo: Menos...', language='pt'))
    jogador = palpite(f'{palpites}ª tentativa: ')  # Solicita outro palpite ao jogador

print(emojize(f'Acertou com {palpites} palpites! :cone_de_festa:', language='pt'))  # Exibe mensagem de acerto com o número de palpites realizados

if palpites < 2:
    print('Você lê mentes')
elif palpites < 3:
    print('Essa foi sorte!')
elif palpites < 4:
    print('Você foi bem!')
elif palpites < 5:
    print('Esse é o mínimo de tentativas se utilizar a estratégia certa!')
else:
    print('Reveja sua estratégia!')

# Versão do computador

def adivinhacao_computador(numero):
	limite_inferior = 1
	limite_superior = 1000
	palpite = limite_superior // 2

	tentativas = 1

	while palpite != numero:
		print(f"O computador palpita {palpite}.")
		sleep(1)
		if palpite < numero:
			limite_inferior = palpite + 1
		else:
			limite_superior = palpite - 1

		palpite = (limite_inferior + limite_superior) // 2
		tentativas += 1

	print(f"O computador acertou o número {numero} em {tentativas} tentativas.")

numero_escolhido = int(input("Escolha um número entre 1 e 1000: "))
adivinhacao_computador(numero_escolhido)

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos melhorar o jogo da adivinhação do DESAFIO 028. Agora, o computador vai "pensar" em um número entre 0 e 10 e o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Vamos usar a mesma estrutura do exercíco 28, mas vamos incrementar o contador de palpites e exibir uma mensagem de acerto com o número de palpites realizados.

# Primeiro precisamos importar as funções randint() e sleep() dos módulos random e time, respectivamente.
from random import randint
from time import sleep

# Em seguida, vamos fazer o computador "pensar" em um número entre 0 e 10. Essa parte do código é a mesma do exercício 28 e deve ficar fora do loop pois senão o computador escolherá um novo número a cada iteração.
computador = randint(0, 10)

# Temos que implementar um contador de palpites para saber quantas tentativas o jogador fez até acertar o número escolhido pelo computador.
palpites = 1  # Inicializa o contador de palpites

# Primeiro definiremos uma condição de controle para o loop. Vamos inicializar o contador de palpites com 1 e pedir para o usuário tentar adivinhar o número.
condição_de_controle = True 

# Agora, vamos pedir para o usuário tentar adivinhar o número escolhido pelo computador. Essa aprte deverá ficar dentro de um estrutura de repetição para que o usuário possa tentar adivinhar até acertar.

while condição_de_controle:

	# Vamos pedir para o usuário tentar adivinhar o número escolhido pelo computador.
	usuario = int(input('Em qual número o computador está pensando? '))

	# Vamos exibir o número escolhido pelo usuário.
	print(f'Você chutou o número {usuario}.')
	sleep(1)

	# Vamos verificar se o usuário acertou ou errou. Podemos salvar o resultado da comparação entre os números em uma variável chamada acertou ou simplesmente fazer a comparação dentro da estrutura condicional. Aqui vamos salvar o resultado da comparação em uma variável.
	acertou = computador == usuario

	if acertou: # Como if espera um valor booleano e armazenamos o resultado da comparação entre os números em acertou, não precisamos fazer a comparação novamente. Ou seja, se acertou for True, o usuário acertou, caso contrário, errou e o else será executado.
    
        # Se o usuário acertou, vamos exibir uma mensagem de sucesso e o número de palpites realizados.
		print('ACERTOU!')
		print(f'Você acertou com {palpites} palpites!')
		
		# Atualizamos a condição de controle para encerrar o loop.
		condição_de_controle = False

	else:
		# Se o usuário errou, vamos exibir uma mensagem de erro.
		print('ERROU!')
		print('Tente novamente...') # O loop reiniciará e o usuário poderá tentar adivinhar o número novamente.
		palpites += 1  # Incrementa o contador de palpites