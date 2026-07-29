# Crie a Classe Caneta, que simule o funcionamento de uma caneta colorida podendo escrever frases na cor relativa

from rich import print

class Caneta():

    def __init__(self, cor_escolhida, frase):
        self.cor = cor_escolhida
        self.frase = frase

    def cores(self):
        print(f'[{self.cor}]{self.frase}')

escolha = Caneta('red', 'Testando a cor vermelha')
escolha.cores()

escolha = Caneta('blue', 'Testando a cor azul')
escolha.cores()

escolha = Caneta('green', 'Testando a cor verde')
escolha.cores()
