# Exercício Python #028 - Jogo da Adivinhação v.1.0 - Aula 00 até 09 - Mundo 1
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
from emoji import emojize
# Tarefa 1: Fazer o computador pensar em um número entre 0 e 5
computador = randint(0, 5)

# Tarefa 2: O usuário deve tentar descobrir o número
usuario = int(input(emojize('Em qual número o computador está pensando? :rosto_pensativo:', language='pt')))

# Tarefa 3: Escrever na tela se o usuário acertou ou errou
print(f'Você chutou o número {usuario}.')
sleep(1)
print('O computador pensou no número...', end=' ')
sleep(1)
print(f'{computador}')
sleep(1)
acertou = computador == usuario

if acertou:
    print(emojize('ACERTOU! :rosto_pensativo:', language='pt'))
else:
    print(emojize('ERROU! :rosto_furioso:', language='pt'))
    
    
    
# Versão 2 -

print(f'Vou pensar em um número entre 1 e 10 e quero que tente adivinhar. Ok?')
sleep(1)
computador = randint(1, 10)
acertou = True

while acertou:
	try:
		sleep(1)
		jogador = int(input('Palpite: '))
		sleep(1)
		print('Analisando...')
		sleep(1)
		acertou = computador != jogador
		if jogador == computador:
			print(f'Acertou! Era mesmo o número {computador}')
			break
		else:
			print(f'Errou! Não é o número {jogador}. Vamos de novo...')
	except ValueError:
		print('Apenas valores numéricos!')

# Versão 3 - Completo com placar
def palpite(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Opção inválida! Digite um número válido.')


print(f'{'Vamos jogar!':^20}')

computador = randint(1, 100)
tentativa = 1

while True:
	usuário = palpite(f'{tentativa}ª tentativa: ')

	if usuário < 1 or usuário > 100:
		print('Apenas valores entre 1 e 100.')
		continue

	if usuário == computador:
		print(f'Acertou! Era mesmo {computador}. Foram {tentativa} tentativas.')
		break
	else:
		dica = emojize('\033[1;32mMaior :seta_para_cima:\033[m' if usuário < computador else '\033[1;31mMenor :seta_para_baixo:\033[m', language='pt')
		print(f'Errou! É {dica} que {usuário}. Tente novamente...')
		tentativa += 1
		continue

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve fazer o computador "pensar" em um número inteiro entre 0 e 5 e pedir para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deve escrever na tela se o usuário venceu ou perdeu.

# Para criar o efeito de "pensar" em um número, vamos utilizar a função randint() do módulo random. Essa função gera um número inteiro aleatório dentro de um intervalo especificado. Apenas para fins estéticos, vamos adicionar um pequeno delay entre as mensagens com a função sleep() do módulo time.

# Primeiro precisamos importar as funções randint() e sleep() dos módulos random e time, respectivamente.
from random import randint
from time import sleep

# Em seguida, vamos fazer o computador "pensar" em um número entre 0 e 5.
computador = randint(0, 5)

# Agora, vamos pedir para o usuário tentar adivinhar o número escolhido pelo computador.
usuario = int(input('Em qual número o computador está pensando? '))

# Vamos exibir o número escolhido pelo usuário e o número escolhido pelo computador.
print(f'Você chutou o número {usuario}.')
sleep(1)
print('O computador pensou no número...', end=' ')
sleep(1)
print(f'{computador}')

# Por fim, vamos verificar se o usuário acertou ou errou. Podemos salvar o resultado da comparação entre os números em uma variável chamada acertou ou simplesmente fazer a comparação dentro da estrutura condicional. Aqui vamos salvar o resultado da comparação em uma variável.
acertou = computador == usuario

if acertou: # Como if espera um valor booleano e armazenamos o resultado da comparação entre os números em acertou, não precisamos fazer a comparação novamente. Ou seja, se acertou for True, o usuário acertou, caso contrário, errou e o else será executado.
    print('ACERTOU!')
else:
    print('ERROU!')

# Nossa estrutura condicional é simples, pois só precisamos verificar se o número escolhido pelo usuário é igual ao número escolhido pelo computador. Se for, o usuário acertou, caso contrário, errou. 