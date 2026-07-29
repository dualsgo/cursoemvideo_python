# __ double underscore - dunder (double underscore) - método mágico

# print(int.__doc__)

# __doc__ - mostra a documentação da classe

class Gafanhoto():
    # docstring - documentação da classe
    """Classe que representa um gafanhoto, com nome e idade.
    
    Para criar um gafanhoto, basta informar o nome e a idade. Se não for informado, o nome será 'Não informado' e a idade será 0."""
    # Método construtor
    def __init__(self, nome ='Não informado', idade = 0):
        self.nome = nome
        self.idade = idade
        
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
        
    # Método mágico que retorna a representação do objeto em forma de string. Ele é chamado quando o objeto é convertido em string, por exemplo, quando é impresso.    
    def __str__(self):
        return f'Gafanhoto: {self.nome}, Idade: {self.idade}'
    
    # Método mágico que retorna o estado do objeto, ou seja, os atributos e seus valores.
    def _getstate_(self):
        return 'Nome: ' + self.nome + ' Idade: ' + str(self.idade)
        
print(Gafanhoto.__doc__)

g1 = Gafanhoto('João', 20)

# Ao chamar a instancia do objeto, o método __str__ é chamado automaticamente, retornando a representação do objeto em forma de string.
print(g1)

# DICT - método mágico que retorna um dicionário com os atributos e seus valores. Ele é chamado quando o objeto é convertido em um dicionário.
print((g1.__dict__))

# GETSTATE - método mágico que retorna o estado do objeto, ou seja, os atributos e seus valores.
print(g1._getstate_())

print(g1.__class__)