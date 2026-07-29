# Crie a Classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto

class Produto():

    def __init__(self, nome_produto, preco_produto):
        self.nome = nome_produto
        self.preco = preco_produto

    def __str__(self):
        return f'Descrição: {self.nome}\nPreço: {self.preco}'


produto_x = Produto('Teste', 'R$ 2,99')
print(produto_x)