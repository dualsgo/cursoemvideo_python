class Gafanhoto():
    # Método construtor
    def __init__(self, nome ='Não informado', idade = 0):
        self.nome = nome
        self.idade = idade
        
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
        

g1 = Gafanhoto('João', 20)
g1.mensagem()

g2 = Gafanhoto('Maria', 25)
g2.mensagem()

g3 = Gafanhoto()
g3.mensagem()