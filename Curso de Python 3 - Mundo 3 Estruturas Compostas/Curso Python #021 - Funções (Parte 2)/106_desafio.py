# Exercício Python #106 - Sistema interativo de ajuda em Python - Aula 00 até 21 - Mundo 3
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def ajuda():
	while True:
		entrada = input('\033[1;34mDigite o comando que deseja visualizar ou FIM para sair: \033[m').strip().lower()
		if entrada == 'fim':
			print('\033[1;31mFINALIZANDO O PROGRAMA\033[m')
			break

		print('\033[7;37;40m', end='')
		help(entrada)
		print('\033[m')


ajuda()


"""
def ajuda():
    while True:
        entrada = input('\033[1;34mDigite o comando que deseja visualizar ou FIM para sair: \033[m').strip().lower()
        if entrada == 'fim':
            print('\033[1;31mFINALIZANDO O PROGRAMA\033[m')
            break
        
        # Tenta capturar a saída do help() e verificar o conteúdo
        import io
        import sys
        
        # Redireciona a saída padrão para capturar o texto gerado pelo help()
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        
        try:
            help(entrada)
            output = new_stdout.getvalue()
        finally:
            sys.stdout = old_stdout  # Restaura a saída padrão
        
        # Verifica se "No Python documentation found for" está na saída
        if "No Python documentation found for" in output:
            print('\033[1;30;43m', end='')  # Texto preto com fundo amarelo
        else:
            print('\033[7;37;40m', end='')  # Fundo inverso
        
        print(output)
        print('\033[m', end='')  # Reseta as cores

ajuda()

"""

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que criar um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def ajuda():
    # O programa vai continuar em loop até o usuário digitar a palavra 'FIM'
	while True:
		entrada = input('\033[1;34mDigite o comando que deseja visualizar ou FIM para sair: \033[m').strip().lower()
        # Se o usuário digitar 'FIM', o programa vai exibir a mensagem 'FINALIZANDO O PROGRAMA' e vai encerrar o loop
		if entrada == 'fim':
			print('\033[1;31mFINALIZANDO O PROGRAMA\033[m')
			break
        # Se o usuário digitar um comando válido, o programa vai exibir o manual do comando
		print('\033[7;37;40m', end='')
		help(entrada)
		print('\033[m')


ajuda()