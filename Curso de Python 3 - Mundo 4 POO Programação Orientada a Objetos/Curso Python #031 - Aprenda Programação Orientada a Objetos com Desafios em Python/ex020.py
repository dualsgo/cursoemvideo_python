
# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer


class Gamer():

    def __init__(self, nome_real, apelido, top_games):

        self.nome = nome_real
        self.nick = apelido
        self.favoritos = list(top_games)


    def fichaGamer(self):

        return f'Fiicha Gamer\n\nNome: {self.nome}\nNick: {self.nick}\nJogos Favoritos: {self.favoritos}'


    def __str__(self):

        return f'Ficha Gamer\n\nNome: {self.nome}\nNick: {self.nick}\nJogos Favoritos: {self.favoritos}'


jogador1 = Gamer('Maycon', 'MD', ['Lat of Us', 'God of War'])
print(jogador1.fichaGamer())

jogador2 = Gamer('Douglas', 'DUALSGO', ['Mario', 'Sonic'])
print(jogador2)
