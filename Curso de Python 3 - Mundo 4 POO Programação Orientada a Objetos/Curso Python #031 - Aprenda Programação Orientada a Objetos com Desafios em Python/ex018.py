
# Crie a Classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por.

# Consumo: 400g por pessoa / Preço R$ 82,40Kg

class Churrasco():

    def __init__(self, evento, quantidade_pessoas):
        self.nome = evento
        self.participantes = quantidade_pessoas

        self.consumo = (400 * self.participantes) / 1000
        self.preco = (self.consumo * 82.4) / self.participantes
        self.total = self.preco * self.consumo


    def __str__(self):
        return f'\nEvento: {self.nome}\nParticipantes: {self.participantes}\nConsumo calculado: {self.consumo}Kg\nPreço por participante: R$ {self.preco:.2f}\nTotal gasto: {self.total:.2f}'


print(Churrasco('Churras dos amigos', 10))