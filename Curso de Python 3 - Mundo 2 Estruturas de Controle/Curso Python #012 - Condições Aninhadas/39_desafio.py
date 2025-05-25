# Exercício Python #039 - Alistamento Militar - Aula 00 até 12 - Mundo 2
#  Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
from math import e

ano_atual = date.today().year

# Tarefa 1: Ler o ano de nascimento
while True:
    try:
        ano_nascimento = int(input('Digite o seu ano de nascimento: '))
        idade = ano_atual - ano_nascimento
        if idade <= 0 or idade > 100:
            print('Idade inválida!')
            continue
        else:
            break

    except ValueError:
        print('Valor de tipo inválido!')


# Tarefa 2: Verificar as condições de alistamento
print(f'Você nasceu em {ano_nascimento} e tem atualmente, em {ano_atual}, \033[1;32m{idade} anos de idade\033[m.')
idade_alistamento = 18
ano_alistamento = ano_nascimento + idade_alistamento

# Tarefa 3: Mostrar o tempo que falta ou se passou do prazo
if idade < idade_alistamento:
    print(f'Seu alistamento deverá ser feito em \033[1m{ano_alistamento}\033[m.')
    print(f'Faltam \033[1m{ano_alistamento - ano_atual} anos\033[m.')
    print('STATUS: \033[1;33mAinda não está na hora de se alistar\033[m.')

elif idade > idade_alistamento:
    print(f'Seu alistamento deveria ter sido feito em \033[1;31m{ano_alistamento}\033[m.')
    print(f'Passaram-se \033[1;31m{ano_atual - ano_alistamento} anos\033[m.')
    print('STATUS: \033[1;31mPassou da hora de se alistar\033[m.')

else:
    print('STATUS: \033[1;32mAliste-se já!\033[m')
    
# Versão 2 - Com validação

from datetime import date

ano_atual = date.today().year

while True:
	try:
		ano_nascimento = int(input('Digite o seu ano de nascimento: '))
		idade = ano_atual - ano_nascimento
		ano_alsitamento = ano_nascimento + 18

		if ano_alsitamento < ano_atual:
			print(f'Você completou 18 anos em {ano_alsitamento} deveria ter se apresentado ao serviço militar obrigatório!')
		elif ano_alsitamento > ano_atual:
			print(f'Você ainda tem {idade} anos. Só deverá se apresentar daqui a {ano_alsitamento - ano_atual} anos, em {ano_alsitamento}.')
		else:
			print(f'Você que completa 18 anos em {ano_atual} deve se apresentar ao serviço militar obrigatório!')
		break
	except ValueError:
		print('Você está utilizando um tipo de dao inválido para essa operação!')

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve ler o ano de nascimento de um jovem e informar, conforme a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. O programa também deve mostrar o tempo que falta ou que passou do prazo.

# Primeiro vamos definir o ano atual. Para isso, vamos importar a função date da biblioteca datetime e utilizar a função today() para obter a data atual. Em seguida, vamos utilizar o método year para obter o ano atual.
from datetime import date

ano_atual = date.today().year

# Em seguida, vamos ler o ano de nascimento do jovem. Para isso, vamos utilizar a função input() para ler o ano de nascimento e a função int() para converter o valor para inteiro.
ano_nascimento = int(input('Digite o seu ano de nascimento: '))

# Vamos calcular a idade do jovem subtraindo o ano de nascimento do ano atual.
idade = ano_atual - ano_nascimento

# Em seguida, vamos verificar se o jovem ainda vai se alistar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Para isso, vamos verificar se a idade do jovem é menor que 18 anos, se é igual a 18 anos ou se é maior que 18 anos.
idade_alistamento = 18
ano_alistamento = ano_nascimento + idade_alistamento

# Por fim, vamos mostrar o tempo que falta ou que passou do prazo para o alistamento. Se a idade do jovem for menor que 18 anos, vamos mostrar o ano em que ele deverá se alistar e o tempo que falta para o alistamento. Se a idade do jovem for maior que 18 anos, vamos mostrar o ano em que ele deveria ter se alistado e o tempo que passou do prazo. Se a idade do jovem for igual a 18 anos, vamos mostrar a mensagem "Aliste-se já!".
if idade < idade_alistamento:
    print(f'Seu alistamento deverá ser feito em {ano_alistamento}.')
    print(f'Faltam {ano_alistamento - ano_atual} anos.')
    print('STATUS: Ainda não está na hora de se alistar.')
elif idade > idade_alistamento:
    print(f'Seu alistamento deveria ter sido feito em {ano_alistamento}.')
    print(f'Passaram-se {ano_atual - ano_alistamento} anos.')
    print('STATUS: Passou da hora de se alistar.')
else:
    print('STATUS: Aliste-se já!')