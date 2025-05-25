# Exercício Python #003 - Somando dois números - Aula 00 até 06 - Mundo 1
# Crie um script Python que leia dois números e tente mostrar a soma entre eles.

from time import sleep
from emoji import emojize

def obtem_valore(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print(emojize('Valor inválido! Tente novamente. :xis:', language='pt'))


primeiro_termo = obtem_valore(emojize(':ábaco: Digite o primeiro termo: ', language='pt'))
segundo_termo = obtem_valore(emojize(':ábaco: Digite o segundo termo: ', language='pt'))
soma = primeiro_termo + segundo_termo
sleep(1)
print(emojize(':ábaco: Calculando... ', language='pt'))
sleep(1)
print(emojize(f'{primeiro_termo:>10}\n{'+':<1}{segundo_termo:>9}\n{'-' * 10}\n{soma:>10}', language='pt'))