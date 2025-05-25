# Todo arquivo .py pode ser usado como módulo se tiver funções internas


def fatorial(numero_argumento):
	fator_atual = 1  # Iniciamos como 1, pois é o fator nulo da multiplicação
	for fator in range(1, numero_argumento + 1):
		fator_atual *= fator
	return fator_atual


def dobrar(numero_argumento):
	return numero_argumento * 2


def triplicar(numero_argumento):
	return numero_argumento * 3